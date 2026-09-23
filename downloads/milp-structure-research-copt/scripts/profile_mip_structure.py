#!/usr/bin/env python3
"""Emit a compact, read-only structural profile of an MPS model with COPT.

The script never calls optimize() or presolve().  Its classifications are
matrix signals for research routing, not claims about application semantics.
"""

from __future__ import annotations

import argparse
import collections
import gzip
import hashlib
import json
import math
import platform
import re
import sys
from pathlib import Path
from typing import Iterable

import coptpy as cp
from coptpy import COPT


TOL = 1e-12


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_model_text(path: Path) -> str:
    """Hash decompressed bytes for .gz inputs and raw bytes otherwise."""
    digest = hashlib.sha256()
    opener = gzip.open if path.suffix.lower() == ".gz" else Path.open
    if opener is gzip.open:
        handle = gzip.open(path, "rb")
    else:
        handle = path.open("rb")
    with handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def finite_or_text(value: float):
    if math.isinf(value):
        return "+inf" if value > 0 else "-inf"
    if math.isnan(value):
        return "nan"
    return value


def name_prefix(name: str) -> str:
    match = re.match(r"([^0-9]+)", name)
    return match.group(1) if match else "<numeric>"


def quantiles(values: Iterable[int | float]) -> dict[str, int | float]:
    ordered = sorted(values)
    if not ordered:
        return {}
    n = len(ordered)
    return {
        "min": ordered[0],
        "q25": ordered[(n - 1) // 4],
        "median": ordered[(n - 1) // 2],
        "q75": ordered[(3 * (n - 1)) // 4],
        "max": ordered[-1],
        "mean": sum(ordered) / n,
    }


def is_close(value: float, target: float) -> bool:
    return abs(value - target) <= TOL


def reverse_sense(sense: str) -> str:
    return {"<": ">", ">": "<", "=": "="}[sense]


def copt_linear_row(constraint) -> tuple[str, float]:
    """Return a canonical sense and RHS without collapsing ranged rows."""
    lower = float(constraint.getInfo(COPT.Info.LB))
    upper = float(constraint.getInfo(COPT.Info.UB))
    infinity = float(COPT.INFINITY)
    lower_infinite = math.isinf(lower) or lower <= -0.999 * infinity
    upper_infinite = math.isinf(upper) or upper >= 0.999 * infinity
    if lower_infinite and upper_infinite:
        return "F", 0.0
    if lower_infinite:
        return "<", upper
    if upper_infinite:
        return ">", lower
    if is_close(lower, upper):
        return "=", (lower + upper) / 2.0
    return "R", upper


class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return
        if self.size[root_left] < self.size[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        self.size[root_left] += self.size[root_right]


def expected_check(label: str, actual: int, expected: int | None) -> None:
    if expected is not None and actual != expected:
        raise RuntimeError(f"{label} mismatch: expected {expected:,}, read {actual:,}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path, help="Original .mps or .mps.gz path")
    parser.add_argument("--output", type=Path, required=True, help="Output JSON path")
    parser.add_argument("--expect-vars", type=int)
    parser.add_argument("--expect-rows", type=int)
    parser.add_argument("--expect-nnz", type=int)
    parser.add_argument(
        "--local-row-max-nnz",
        type=int,
        default=100,
        help="Rows wider than this are treated as possible coupling rows for component profiling",
    )
    parser.add_argument(
        "--ignore-row-prefix",
        action="append",
        default=[],
        help=(
            "Regex for a semantically checked coupling-row family to remove during component "
            "profiling; repeat as needed"
        ),
    )
    args = parser.parse_args()

    source = args.model.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)

    environment = cp.Envr()
    model = environment.createModel(source.stem)
    model.read(str(source))
    model.update()
    variables = list(model.getVars())
    constraints = list(model.getConstrs())
    matrix = model.getA().tocsr()
    csc = matrix.tocsc()

    num_vars = int(model.getAttr(COPT.Attr.Cols))
    num_rows = int(model.getAttr(COPT.Attr.Rows))
    num_nonzeros = int(model.getAttr(COPT.Attr.Elems))
    expected_check("variables", num_vars, args.expect_vars)
    expected_check("rows", num_rows, args.expect_rows)
    expected_check("nonzeros", num_nonzeros, args.expect_nnz)
    expected_check("variable objects", len(variables), num_vars)
    expected_check("constraint objects", len(constraints), num_rows)

    vtypes = [variable.getType() for variable in variables]
    variable_names = [variable.getName() for variable in variables]
    variable_lbs = [float(variable.getInfo(COPT.Info.LB)) for variable in variables]
    variable_ubs = [float(variable.getInfo(COPT.Info.UB)) for variable in variables]
    variable_objs = [float(variable.getInfo(COPT.Info.Obj)) for variable in variables]
    variable_prefixes = [name_prefix(name) for name in variable_names]
    binary = [
        vtype == COPT.BINARY
        or (
            vtype == COPT.INTEGER
            and is_close(lower, 0.0)
            and is_close(upper, 1.0)
        )
        for vtype, lower, upper in zip(vtypes, variable_lbs, variable_ubs)
    ]
    row_nnz = [int(value) for value in matrix.indptr[1:] - matrix.indptr[:-1]]
    col_nnz = [int(value) for value in csc.indptr[1:] - csc.indptr[:-1]]
    objective_support = [index for index, value in enumerate(variable_objs) if not is_close(value, 0.0)]
    objective_support_set = set(objective_support)
    ignored_patterns = [re.compile(pattern) for pattern in args.ignore_row_prefix]

    row_classes: collections.Counter[str] = collections.Counter()
    constraint_senses: collections.Counter[str] = collections.Counter()
    row_algebra_signatures: collections.Counter[str] = collections.Counter()
    implication_rows = 0
    suspected_big_m_rows = 0
    mixed_binary_continuous_rows = 0
    binary_control_bound_like_rows = 0
    objective_integer_definition_rows: list[str] = []
    coefficient_ratios: list[float] = []
    wide_rows: list[int] = []
    explicitly_ignored_rows: list[int] = []
    dsu = DisjointSet(num_vars)

    for row_index, constraint in enumerate(constraints):
        row_name = constraint.getName()
        sense, rhs = copt_linear_row(constraint)
        constraint_senses[sense] += 1
        start, end = matrix.indptr[row_index], matrix.indptr[row_index + 1]
        indices = matrix.indices[start:end]
        coefficients = matrix.data[start:end]
        width = len(indices)

        local_vtypes = [vtypes[int(index)] for index in indices]
        local_prefix_counts = collections.Counter(variable_prefixes[int(index)] for index in indices)
        coefficient_shape = collections.Counter(
            "+1"
            if is_close(float(value), 1.0)
            else "-1"
            if is_close(float(value), -1.0)
            else "+other"
            if float(value) > 0
            else "-other"
            for value in coefficients
        )
        rhs_class = "range" if sense == "R" else "free" if sense == "F" else (
            "0"
            if is_close(rhs, 0.0)
            else "1"
            if is_close(rhs, 1.0)
            else "-1"
            if is_close(rhs, -1.0)
            else "+other"
            if rhs > 0
            else "-other"
        )
        algebra_key = "|".join(
            [
                f"sense={sense}",
                f"rhs={rhs_class}",
                f"nnz={width}",
                "types=" + ",".join(f"{key}:{value}" for key, value in sorted(collections.Counter(local_vtypes).items())),
                "prefixes=" + ",".join(f"{key}:{value}" for key, value in sorted(local_prefix_counts.items())),
                "coef=" + ",".join(f"{key}:{value}" for key, value in sorted(coefficient_shape.items())),
            ]
        )
        row_algebra_signatures[algebra_key] += 1

        has_binary = any(binary[int(index)] for index in indices)
        has_continuous = any(vtypes[int(index)] == COPT.CONTINUOUS for index in indices)
        if has_binary and has_continuous:
            mixed_binary_continuous_rows += 1
            if sense in ("<", ">") and width <= 4:
                binary_control_bound_like_rows += 1

        objective_continuous = [
            int(index)
            for index in indices
            if int(index) in objective_support_set and vtypes[int(index)] == COPT.CONTINUOUS
        ]
        other_indices = [int(index) for index in indices if int(index) not in objective_continuous]
        if (
            sense == "="
            and len(objective_continuous) == 1
            and other_indices
            and all(vtypes[index] != COPT.CONTINUOUS for index in other_indices)
        ):
            if len(objective_integer_definition_rows) < 20:
                objective_integer_definition_rows.append(row_name)

        explicitly_ignored = any(pattern.search(row_name) for pattern in ignored_patterns)
        if explicitly_ignored:
            explicitly_ignored_rows.append(row_index)
        if width > args.local_row_max_nnz:
            wide_rows.append(row_index)
        elif not explicitly_ignored and width >= 2:
            anchor = int(indices[0])
            for index in indices[1:]:
                dsu.union(anchor, int(index))

        magnitudes = [abs(float(value)) for value in coefficients if abs(float(value)) > TOL]
        if magnitudes:
            ratio = max(magnitudes) / min(magnitudes)
            coefficient_ratios.append(ratio)
            if ratio >= 1e4:
                suspected_big_m_rows += 1

        if width == 2 and all(binary[int(index)] for index in indices):
            ordered = sorted(float(value) for value in coefficients)
            if is_close(ordered[0], -1.0) and is_close(ordered[1], 1.0):
                if sense in ("<", ">") and is_close(rhs, 0.0):
                    implication_rows += 1

        if not width or not all(binary[int(index)] for index in indices):
            continue
        if sense not in ("<", ">", "="):
            continue
        values = [float(value) for value in coefficients]
        if all(is_close(value, 1.0) for value in values):
            pass
        elif all(is_close(value, -1.0) for value in values):
            sense = reverse_sense(sense)
            rhs = -rhs
        else:
            continue
        if sense == "=" and is_close(rhs, 1.0):
            row_classes["set_partitioning_eq_1"] += 1
        elif sense == "<" and is_close(rhs, 1.0):
            row_classes["set_packing_le_1"] += 1
        elif sense == ">" and is_close(rhs, 1.0):
            row_classes["set_covering_ge_1"] += 1
        else:
            row_classes["other_unit_binary"] += 1

    roots = collections.Counter(dsu.find(index) for index in range(num_vars))
    component_sizes = sorted(roots.values(), reverse=True)
    coefficient_values = collections.Counter(float(value).hex() for value in matrix.data)
    var_prefixes = collections.Counter(name_prefix(name) for name in variable_names)
    row_prefixes = collections.Counter(name_prefix(row.getName()) for row in constraints)
    objective_sense = int(model.getAttr(COPT.Attr.ObjSense))

    payload = {
        "audit_kind": "copt_read_only_structure_profile",
        "optimization_called": False,
        "presolve_called": False,
        "source": str(source),
        "archive_sha256": sha256_file(source),
        "canonical_model_bytes_sha256": sha256_model_text(source),
        "host": platform.node(),
        "python": sys.version.split()[0],
        "copt_version": ".".join(
            str(value)
            for value in (COPT.VERSION_MAJOR, COPT.VERSION_MINOR, COPT.VERSION_TECHNICAL)
        ),
        "model_name": source.name.removesuffix(".gz").removesuffix(".mps"),
        "objective_sense": "min" if objective_sense == COPT.MINIMIZE else "max",
        "dimensions": {
            "variables": num_vars,
            "linear_constraints": num_rows,
            "quadratic_constraints": int(model.getAttr(COPT.Attr.QConstrs)),
            "sos": int(model.getAttr(COPT.Attr.Soss)),
            "indicator_constraints": int(model.getAttr(COPT.Attr.Indicators)),
            "second_order_cones": int(model.getAttr(COPT.Attr.Cones)),
            "exponential_cones": int(model.getAttr(COPT.Attr.ExpCones)),
            "affine_cones": int(model.getAttr(COPT.Attr.AffineCones)),
            "psd_constraints": int(model.getAttr(COPT.Attr.PsdConstrs)),
            "lmi_constraints": int(model.getAttr(COPT.Attr.LmiConstrs)),
            "nonlinear_constraints": int(model.getAttr(COPT.Attr.NLConstrs)),
            "nonzeros": num_nonzeros,
        },
        "variable_types": dict(sorted(collections.Counter(vtypes).items())),
        "constraint_senses": dict(sorted(constraint_senses.items())),
        "objective": {
            "nonzero_count": len(objective_support),
            "support_fraction": len(objective_support) / num_vars if num_vars else 0.0,
            "supported_variable_types": dict(
                sorted(collections.Counter(vtypes[index] for index in objective_support).items())
            ),
            "coefficient_values_top20_hex": collections.Counter(
                variable_objs[index].hex() for index in objective_support
            ).most_common(20),
            "constant": float(model.getAttr(COPT.Attr.ObjConst)),
        },
        "row_width": quantiles(row_nnz),
        "column_degree": quantiles(col_nnz),
        "coefficient_magnitude_ratio_by_row": quantiles(coefficient_ratios),
        "candidate_matrix_signals": {
            "unit_binary_rows": dict(sorted(row_classes.items())),
            "two_binary_implication_like_rows": implication_rows,
            "suspected_big_m_rows_ratio_ge_1e4": suspected_big_m_rows,
            "mixed_binary_continuous_rows": mixed_binary_continuous_rows,
            "small_binary_control_bound_like_rows": binary_control_bound_like_rows,
            "objective_continuous_defined_by_integer_equality_examples": objective_integer_definition_rows,
            "possible_coupling_rows_above_width_threshold": len(wide_rows),
            "semantically_selected_coupling_rows": len(explicitly_ignored_rows),
            "ignored_row_prefix_regexes": args.ignore_row_prefix,
            "local_row_width_threshold": args.local_row_max_nnz,
            "components_after_ignoring_possible_coupling_rows": {
                "count": len(component_sizes),
                "singletons": sum(size == 1 for size in component_sizes),
                "largest_20": component_sizes[:20],
            },
        },
        "bounded_descriptive_hints": {
            "coefficient_values_top20_hex": coefficient_values.most_common(20),
            "variable_name_prefixes_top20": var_prefixes.most_common(20),
            "row_name_prefixes_top20": row_prefixes.most_common(20),
            "row_algebra_signatures_top30": row_algebra_signatures.most_common(30),
            "warning": (
                "Name prefixes, row signatures, width/regex-based coupling rows, implication rows, "
                "mixed binary-continuous templates, and big-M ratios are hypothesis signals only. "
                "Confirm semantics from full row algebra and authoritative sources."
            ),
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    environment.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

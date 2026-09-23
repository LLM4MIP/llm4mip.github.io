#!/usr/bin/env python3
"""Site build entry point; current catalogue uses build_campaign_data.

<<<<<<< Updated upstream
The helpers below document the legacy September 18 archive packaging. The
default build uses the checked-in September 21 inputs, preserving those
historical bundles and the separately frozen skill comparison downloads.
=======
The benchmark source of truth is the adjacent MIPLIB_openproblem working tree;
solver-specific skill sources are versioned under this site's downloads tree.
The script deliberately excludes the historical rmine14 calibration and
official raw MPS inputs. Every omission is recorded, with hashes, in the
package manifest; derived proof models and large proof traces remain included.
>>>>>>> Stashed changes
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import re
import shutil
import tarfile
from pathlib import Path


SITE = Path(__file__).resolve().parents[1]
SOURCE = SITE.parent / "MIPLIB_openproblem"
SOURCE_README = SOURCE / "README.md"
PUBLICATION_REPORT = SITE / "technical-report.tex"
DETAILS = SITE / "instances" / "details"
DOWNLOADS = SITE / "downloads"
NUMERICALLY_OPTIMAL_1E10 = {
    "genus-g31-8",
    "genus-sym-g31-8",
}
NO_FEASIBLE = {
    "datt256",
    "neos-3355323-arnon",
    "neos-3603137-hoteo",
    "supportcase30",
}
EVIDENCE_GROUPS = {
    "PE": {
        "label": "Portable exact certificate",
        "instances": {
            "assign1-10-4", "cvrpp-n16k8vrpi", "dfn-bwin-DBE",
            "fhnw-binschedule0", "fhnw-binschedule1", "fhnw-binschedule2",
            "fhnw-schedule-paira100", "fhnw-schedule-paira200",
            "fhnw-schedule-pairb200", "fhnw-schedule-paira400",
            "fhnw-schedule-pairb400", "neos-3009394-lami",
            "neos-2629914-sudost", "allcolor58", "graph40-80-1rand",
            "graph40-40-1rand", "neos-4355351-swalm", "fhnw-binpack4-58",
        },
    },
    "HP": {"label": "Checked exact proof with large trace retained externally by hash", "instances": {"bppc6-06"}},
    "EX": {"label": "Specialized exact exhaustive computation without a standalone trace", "instances": {"neos-4360552-sangro", "ns1631475", "genus-sym-grafo5708-48"}},
    "LT": {"label": "Exact crosswalk plus published theorem or exhaustive result", "instances": {"circ10-3", "a2864-99blp", "pythago7825"}},
    "NS": {"label": "Strict primal audit plus floating-point zero-gap solver run", "instances": {"neos-3594536-henty", "neos-2978205-isar", "minutedispatchstrategy"}},
    "MX": {"label": "Mixed database and commercial-solver verification", "instances": {"cvrpb-n45k5vrpi", "cvrpa-n64k9vrpi"}},
}
FHNW_EXACT_SCHEDULES = {
    "fhnw-schedule-paira100",
    "fhnw-schedule-paira200",
    "fhnw-schedule-pairb200",
    "fhnw-schedule-paira400",
    "fhnw-schedule-pairb400",
}

LEADING_BOUND = re.compile(
    r"^([+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?)(?:\.{3})?(?:\s+(.*))?$"
)

# These entries need more than mechanical separation of a leading number and
# its qualifier. In particular, progress counters and structural quantities
# are not objective bounds, and xmas10-2 is reported in a negated MPS objective.
BOUND_DISPLAY_OVERRIDES: dict[tuple[str, str], dict[str, str | None]] = {
    ("d20200", "dual"): {
        "value": "12,232",
        "note": "solver bound; independently checked exact bound: 12,230",
    },
    ("datt256", "primal"): {"value": "—", "note": "no feasible point"},
    ("datt256", "dual"): {"value": "—", "note": "local infeasibility certificates"},
    ("fhnw-binpack4-58", "primal"): {"value": "—", "note": "infeasible"},
    ("fhnw-binpack4-58", "dual"): {"value": "—", "note": "geometric contradiction"},
    ("genus-g31-8", "primal"): {
        "value": "-23",
        "note": "candidate; native genus 3; literal-MPS residual 1e-15",
    },
    ("genus-sym-g31-8", "primal"): {
        "value": "-23",
        "note": "candidate; native genus 3; literal-MPS residual 1e-15",
    },
    ("neos-3355323-arnon", "primal"): {"value": "—", "note": "no feasible witness"},
    ("neos-3355323-arnon", "dual"): {"value": "—", "note": "no infeasibility certificate"},
    ("neos-3603137-hoteo", "primal"): {"value": "—", "note": "no feasible point"},
    ("neos-3603137-hoteo", "dual"): {"value": "—", "note": "CP and SAT status unknown"},
    ("polygonpack4-15", "primal"): {
        "value": "-63,613,612.4112532",
        "note": "rounded display; full precision in source bundle; strict repair",
    },
    ("polygonpack5-15", "primal"): {
        "value": "-55,494,687.6476067",
        "note": "rounded display; full precision in source bundle; strict repair",
    },
    ("pythago7825", "primal"): {"value": "—", "note": "infeasible"},
    ("pythago7825", "dual"): {"value": "—", "note": "published UNSAT theorem"},
    ("s82", "dual"): {
        "value": "—",
        "note": "exact structural bound: max sum(A8) = 36; not an objective bound",
    },
    ("set3-09", "primal"): {
        "value": "176,497.1524256825",
        "note": "rounded display; full precision in source bundle; strict repair",
    },
    ("sorrell7", "dual"): {
        "value": "-210",
        "note": "published coding-theory bound; study solver bound: -216",
    },
    ("supportcase30", "primal"): {
        "value": "—",
        "note": "no feasible point; best partial coverage: 987/1,024",
    },
    ("supportcase30", "dual"): {
        "value": "—",
        "note": "37 covering rows remain; not an objective bound",
    },
    ("xmas10-2", "dual"): {
        "value": "-511",
        "note": "objective equivalent of the official 511-cell upper bound; study solver bound: -515",
    },
}


def section(text: str, heading: str) -> str:
    start = text.index(f"## {heading}")
    end = text.find("\n## ", start + 3)
    return text[start:] if end < 0 else text[start:end]


def markdown_rows(block: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in block.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] != "Instance":
            rows.append(cells)
    return rows


def instance_name(cell: str) -> str:
    match = re.search(r"\[`?([^`\]]+)`?\]\(instances/[^)]+\)", cell)
    if not match:
        raise ValueError(f"Cannot parse instance name from {cell!r}")
    return match.group(1)


def plain(value: str) -> str:
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", value).strip()


def academic_wording(value: str) -> str:
    return (
        value.replace("campaign's", "benchmark's")
        .replace("mixed database/computational evidence", "mixed database/computational verification")
        .replace("solver-based global-optimality evidence", "solver-based global-optimality verification")
        .replace("computational global conclusion", "computational optimality verification")
    )


def bound_display(instance: str, kind: str, value: str) -> dict[str, str | None]:
    """Split a table measure into a numeric line and a qualifying note.

    Values remain strings so long integer and decimal representations are not
    rounded by JSON or JavaScript. Only a number anchored at the start of the
    source field can become the primary display value.
    """
    override = BOUND_DISPLAY_OVERRIDES.get((instance, kind))
    if override:
        return override.copy()
    if value == "—":
        return {"value": "—", "note": None}
    match = LEADING_BOUND.fullmatch(value)
    if not match:
        return {"value": "—", "note": value}
    note = (match.group(2) or "").strip()
    if note.startswith("(") and note.endswith(")"):
        note = note[1:-1].strip()
    return {"value": match.group(1), "note": note or None}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def add_bytes(tar: tarfile.TarFile, name: str, payload: bytes) -> None:
    info = tarfile.TarInfo(name)
    info.size = len(payload)
    info.mode = 0o644
    info.mtime = 0
    info.uid = info.gid = 0
    info.uname = info.gname = ""
    tar.addfile(info, io.BytesIO(payload))


def add_file(tar: tarfile.TarFile, path: Path, arcname: str) -> None:
    info = tar.gettarinfo(str(path), arcname=arcname)
    info.mtime = 0
    info.uid = info.gid = 0
    info.uname = info.gname = ""
    with path.open("rb") as handle:
        tar.addfile(info, handle)


def status_for(name: str, globals_by_name: dict[str, list[str]]) -> tuple[str, str]:
    if name in globals_by_name:
        return "concluded", "Certified optimality / infeasibility"
    if name in NO_FEASIBLE:
        return "no-feasible", "No feasible point found"
    if name in NUMERICALLY_OPTIMAL_1E10:
        return "numeric-optimal", "Numerically optimal up to 1e-10 tolerance"
    return "verified-open", "Verified feasible; open"


def evidence_grade(name: str) -> tuple[str, str]:
    for code, group in EVIDENCE_GROUPS.items():
        if name in group["instances"]:
            return code, str(group["label"])
    raise KeyError(f"No reconciled evidence grade for global conclusion {name}")


def reconciled_conclusions() -> dict[str, tuple[str, str]]:
    rows: dict[str, tuple[str, str]] = {}
    pattern = re.compile(r"^\\texttt\{\\detokenize\{([^}]+)\}\} & (.*?) & ([A-Z]{2})")
    for line in PUBLICATION_REPORT.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            rows[match.group(1)] = (match.group(2), match.group(3))
    if len(rows) != 30:
        raise RuntimeError(f"Expected 30 reconciled report rows, found {len(rows)}")
    return rows


def current_global_method(name: str, global_row: list[str]) -> str:
    if name in FHNW_EXACT_SCHEDULES:
        return (
            "portable exact branch-and-dual certificate with frozen or rebuilt strengthening, "
            "untouched-original-MPS audit, and paired-formulation cross-check where available"
        )
    return plain(global_row[2])


def summary_markdown(record: dict[str, object], global_row: list[str] | None) -> str:
    lines = [
        f"# {record['instance']}",
        "",
        "> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.",
        "",
        "## Results and progress",
        "",
        f"- **Benchmark outcome:** {record['statusLabel']}",
        f"- **Best verified result:** {record['bestResult']}",
        f"- **Best bound or certificate:** {record['bestBound']}",
        f"- **Study result:** {record['studyStatus']}",
    ]
    if global_row:
        grade_code, grade_label = evidence_grade(str(record["instance"]))
        lines += [
            "",
            "## Certified optimality or infeasibility result",
            "",
            f"- **Conclusion:** {record['globalConclusion']}",
            f"- **Main method:** {record['globalMethod']}",
            f"- **Verification category:** {grade_code} — {grade_label}",
            f"- **Earlier source-table status:** {academic_wording(plain(global_row[3]))}",
            "- **Reconciliation rule:** The verification category above governs this summary when older instance or table wording differs.",
        ]
    else:
        lines += [
            "",
            "## Interpretation",
            "",
            "The benchmark study does not report a certified global optimum or infeasibility result for this instance. The archived work may still contain a stricter incumbent, a stronger lower bound, an exact structural reduction, a closed local neighborhood, or a documented negative experiment.",
        ]
    lines += [
        "",
        "## Experiment workflow",
        "",
        "1. Freeze the original model, baseline, objective convention, and acceptance tolerance.",
        "2. Profile the untouched formulation and propose falsifiable structural hypotheses.",
        "3. Run bounded primal, dual, reduction, or certificate experiments with explicit stopping rules.",
        "4. Map useful results back to the original MPS and classify the resulting verification method.",
        "",
        "## Download bundle",
        "",
        "The sibling `.tar.gz` archive copies the related research material from this instance directory and adds this summary plus a package manifest. Only official raw `.mps`/`.mps.gz` inputs are omitted to avoid redistributing bulky benchmark source files; public solutions, hashes, derived proof models, runs, logs, and any proof traces present in the directory remain included. Files retained externally by hash cannot be embedded here.",
        "",
        "## Provenance",
        "",
        "Generated from the local `MIPLIB_openproblem` research archive for the LLM4MIP website. Read the source instance README and package manifest before reusing a numerical claim.",
        "",
        f"- **Source base commit:** `{record['sourceBaseCommit']}` plus the disclosed 18 September working-tree reconciliation",
        f"- **Source README SHA-256:** `{record['sourceReadmeSha256']}`",
        "",
    ]
    return "\n".join(lines)


def archive_instance(source_dir: Path, target: Path, summary: str) -> tuple[int, int, list[str]]:
    package_root = f"{source_dir.name}-findings"
    included: list[Path] = []
    excluded: list[str] = []
    for path in sorted(source_dir.rglob("*"), key=lambda item: item.as_posix()):
        if not path.is_file():
            continue
        rel = path.relative_to(source_dir)
        if any(part in {".DS_Store", "__pycache__"} for part in rel.parts):
            excluded.append(f"{rel.as_posix()} (cache or OS metadata)")
            continue
        if rel.parts[0] == "input" and (path.name.endswith(".mps") or path.name.endswith(".mps.gz")):
            excluded.append(
                f"{rel.as_posix()} ({path.stat().st_size} bytes; raw benchmark input; sha256 {sha256(path)})"
            )
            continue
        included.append(path)

    manifest_lines = [
        f"# Package manifest: {source_dir.name}",
        "",
        "Generated for the LLM4MIP site from the 2026-09-18 research snapshot.",
        "Source base commit: 89a8abd0847941bdf774353a1983d5e6a00457a0 plus the disclosed 18 September working-tree reconciliation.",
        "Archive timestamps and ownership are normalized for reproducible packaging.",
        "",
        f"Included source files: {len(included)}",
        f"Excluded source files: {len(excluded)}",
        "",
        "## Included files",
        "",
    ]
    manifest_lines.extend(f"- `{path.relative_to(source_dir).as_posix()}`" for path in included)
    manifest_lines += ["", "## Excluded files", ""]
    manifest_lines.extend(f"- `{item}`" for item in excluded)
    if not excluded:
        manifest_lines.append("- None")
    manifest = "\n".join(manifest_lines) + "\n"

    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=6) as zipped:
            with tarfile.open(fileobj=zipped, mode="w", format=tarfile.PAX_FORMAT) as tar:
                add_bytes(tar, f"{package_root}/summary.md", summary.encode("utf-8"))
                add_bytes(tar, f"{package_root}/PACKAGE-MANIFEST.md", manifest.encode("utf-8"))
                add_file(tar, SOURCE / "LICENSE", f"{package_root}/LICENSE")
                for path in included:
                    rel = path.relative_to(source_dir).as_posix()
                    add_file(tar, path, f"{package_root}/{source_dir.name}/{rel}")
    return len(included), len(excluded), excluded


def build_instances() -> list[dict[str, object]]:
    text = SOURCE_README.read_text(encoding="utf-8")
    global_rows = markdown_rows(section(text, "Verified global conclusions"))
    globals_by_name = {instance_name(row[0]): row for row in global_rows}
    report_conclusions = reconciled_conclusions()
    result_rows = markdown_rows(section(text, "Results at a glance"))
    if len(result_rows) != 113:
        raise RuntimeError(f"Expected 113 source result rows, found {len(result_rows)}")
    result_names = [instance_name(row[0]) for row in result_rows]
    source_names = {path.name for path in (SOURCE / "instances").iterdir() if path.is_dir()}
    if len(result_names) != len(set(result_names)) or set(result_names) != source_names:
        raise RuntimeError(
            "Results-at-a-glance roster does not exactly match the source instance directories: "
            f"{sorted(set(result_names) ^ source_names)}"
        )
    expected_details = set(result_names) - {"rmine14"}
    existing_details = {path.name for path in DETAILS.iterdir() if path.is_dir()} if DETAILS.exists() else set()
    stale_details = existing_details - expected_details
    if stale_details:
        raise RuntimeError(f"Stale generated instance directories require review: {sorted(stale_details)}")

    records: list[dict[str, object]] = []
    for row in result_rows:
        name = instance_name(row[0])
        if name == "rmine14":
            continue
        source_dir = SOURCE / "instances" / name
        if not source_dir.is_dir():
            raise FileNotFoundError(source_dir)
        status, label = status_for(name, globals_by_name)
        global_row = globals_by_name.get(name)
        grade_code, grade_label = evidence_grade(name) if global_row else (None, None)
        if global_row:
            conclusion, report_grade = report_conclusions[name]
            if report_grade != grade_code:
                raise RuntimeError(f"Evidence grade mismatch for {name}: report {report_grade}, mapping {grade_code}")
        else:
            conclusion = None
        best_result = plain(row[1])
        best_bound = plain(row[2])
        record: dict[str, object] = {
            "instance": name,
            "status": status,
            "statusLabel": label,
            "bestResult": best_result,
            "bestResultDisplay": bound_display(name, "primal", best_result),
            "bestBound": best_bound,
            "bestBoundDisplay": bound_display(name, "dual", best_bound),
            "studyStatus": academic_wording(plain(row[3])),
            "globalConclusion": conclusion,
            "globalMethod": current_global_method(name, global_row) if global_row else None,
            "evidenceGrade": grade_code,
            "evidenceLevel": grade_label,
            "sourceEvidenceNote": academic_wording(plain(global_row[3])) if global_row else None,
            "summary": f"details/{name}/summary.md",
            "archive": f"details/{name}/{name}-findings.tar.gz",
            "sourceBaseCommit": "89a8abd0847941bdf774353a1983d5e6a00457a0",
            "sourceReadmeSha256": sha256(source_dir / "README.md"),
        }
        target_dir = DETAILS / name
        target_dir.mkdir(parents=True, exist_ok=True)
        summary = summary_markdown(record, global_row)
        archive_path = target_dir / f"{name}-findings.tar.gz"
        included, excluded, _ = archive_instance(source_dir, archive_path, summary)
        archive_hash = sha256(archive_path)
        record.update(
            {
                "archiveBytes": archive_path.stat().st_size,
                "archiveSha256": archive_hash,
                "includedFiles": included,
                "excludedFiles": excluded,
            }
        )
        summary += (
            "\n## Package integrity\n\n"
            f"- **Archive:** `{name}-findings.tar.gz`\n"
            f"- **Compressed bytes:** `{archive_path.stat().st_size}`\n"
            f"- **SHA-256:** `{archive_hash}`\n"
            f"- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/{name}/README.md\n"
        )
        (target_dir / "summary.md").write_text(summary, encoding="utf-8")
        records.append(record)

    if len(records) != 112:
        raise RuntimeError(f"Expected 112 publication instances, found {len(records)}")
    graded = set().union(*(group["instances"] for group in EVIDENCE_GROUPS.values()))
    if graded != set(globals_by_name):
        raise RuntimeError(f"Evidence-grade roster differs from global table: {sorted(graded ^ set(globals_by_name))}")
    counts = {key: sum(record["status"] == key for record in records) for key in ("concluded", "verified-open", "numeric-optimal", "no-feasible")}
    expected = {"concluded": 30, "verified-open": 76, "numeric-optimal": 2, "no-feasible": 4}
    if counts != expected:
        raise RuntimeError(f"Unexpected status counts: {counts}; expected {expected}")

    records.sort(key=lambda record: str(record["instance"]).lower())
    (SITE / "instances").mkdir(exist_ok=True)
    (SITE / "instances" / "instances.json").write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    payload = json.dumps(records, ensure_ascii=False, separators=(",", ":"))
    (SITE / "instances" / "data.js").write_text(f"window.INSTANCE_DATA={payload};\n", encoding="utf-8")
    return records


def deterministic_tree_archive(source_dir: Path, target: Path, root_name: str, extras: list[tuple[Path, str]] | None = None) -> None:
    paths = [path for path in source_dir.rglob("*") if path.is_file() and path.name != ".DS_Store"]
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as zipped:
            with tarfile.open(fileobj=zipped, mode="w", format=tarfile.PAX_FORMAT) as tar:
                for path in sorted(paths, key=lambda item: item.as_posix()):
                    add_file(tar, path, f"{root_name}/{path.relative_to(source_dir).as_posix()}")
                for path, arcname in extras or []:
                    add_file(tar, path, arcname)


def deterministic_multi_archive(
    sources: list[tuple[Path, str]], target: Path, extras: list[tuple[Path, str]] | None = None
) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as zipped:
            with tarfile.open(fileobj=zipped, mode="w", format=tarfile.PAX_FORMAT) as tar:
                for source_dir, root_name in sources:
                    paths = [path for path in source_dir.rglob("*") if path.is_file() and path.name != ".DS_Store"]
                    for path in sorted(paths, key=lambda item: item.as_posix()):
                        add_file(tar, path, f"{root_name}/{path.relative_to(source_dir).as_posix()}")
                for path, arcname in extras or []:
                    add_file(tar, path, arcname)


def build_downloads() -> None:
    DOWNLOADS.mkdir(exist_ok=True)
    gurobi_skill_source = DOWNLOADS / "milp-structure-research"
    copt_skill_source = DOWNLOADS / "milp-structure-research-copt"
    if not gurobi_skill_source.is_dir() or not copt_skill_source.is_dir():
        raise FileNotFoundError("solver-specific skill source directories are missing")
    deterministic_tree_archive(
        gurobi_skill_source,
        DOWNLOADS / "milp-structure-research.tar.gz",
        "milp-structure-research",
    )
    deterministic_tree_archive(
        gurobi_skill_source,
        DOWNLOADS / "milp-structure-research-gurobi.tar.gz",
        "milp-structure-research",
    )
    deterministic_tree_archive(
        copt_skill_source,
        DOWNLOADS / "milp-structure-research-copt.tar.gz",
        "milp-structure-research-copt",
    )
    comparison = SOURCE / "docs" / "comparisons" / "milp-structure-skill-effect-20260913"
    comparison_downloads = {
        "comparison.csv": "skill-comparison.csv",
        "audit.json": "skill-comparison-audit.json",
        "README.md": "skill-comparison-report.md",
        "SOURCE.md": "skill-comparison-source.md",
    }
    for source_name, target_name in comparison_downloads.items():
        shutil.copy2(comparison / source_name, DOWNLOADS / target_name)
    deterministic_tree_archive(
        comparison,
        DOWNLOADS / "skill-experiment-evidence.tar.gz",
        "milp-structure-skill-effect-20260913",
        [(SOURCE / "LICENSE", "milp-structure-skill-effect-20260913/LICENSE")],
    )
    deterministic_multi_archive(
        [
            (
                SOURCE / "docs" / "first-five-dual-bound-review-2026-09-18",
                "first-five-dual-bound-review-2026-09-18",
            ),
            (
                SOURCE / "docs" / "rows-06-20-dual-bound-review-2026-09-18",
                "rows-06-20-dual-bound-review-2026-09-18",
            ),
        ],
        DOWNLOADS / "campaign-reconciliation-audits.tar.gz",
        [(SOURCE / "LICENSE", "LICENSE")],
    )

    rows: list[dict[str, str]] = []
    with (comparison / "comparison.csv").open(encoding="utf-8", newline="") as handle:
        rows.extend(csv.DictReader(handle))
    (SITE / "assets").mkdir(exist_ok=True)
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
    (SITE / "assets" / "comparison-data.js").write_text(f"window.COMPARISON_DATA={payload};\n", encoding="utf-8")


def main() -> None:
    from build_campaign_data import main as build_campaign
    build_campaign()
    from build_skill_data import main as build_skill
    build_skill()


if __name__ == "__main__":
    main()

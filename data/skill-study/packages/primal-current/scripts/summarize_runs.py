#!/usr/bin/env python3
"""Summarize recorded validation outcomes, NOT independently validate solutions.

Input is JSONL: one meta record followed by experiment records. See
references/validation-and-measurement.md. Decimal arithmetic preserves tiny
improvements and negative/maximization objectives.
"""
import argparse
from collections import Counter
from decimal import Decimal, InvalidOperation, getcontext, localcontext
import json
from pathlib import Path
import re


def number(value, name):
    if isinstance(value, bool) or value is None:
        raise ValueError(f'{name}: expected finite numeric string')
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f'{name}: invalid number') from exc
    if not result.is_finite():
        raise ValueError(f'{name}: non-finite value')
    # Allow the long terminating-decimal witnesses used in this repository.
    tup = result.as_tuple()
    required = len(tup.digits) + abs(result.adjusted()) + abs(tup.exponent) + 32
    if required > 10000:
        raise ValueError(f'{name}: numeric exponent/precision too large for a compact ledger')
    getcontext().prec = max(getcontext().prec, required)
    return result


def sha(value):
    return isinstance(value, str) and bool(re.fullmatch(r'[0-9a-fA-F]{64}', value))


def _summarize(records):
    if not records or records[0].get('type') != 'meta':
        raise ValueError('First record must be meta')
    meta = records[0]
    if meta.get('sense') not in ('min', 'max') or not sha(meta.get('model_sha256')):
        raise ValueError('meta requires sense=min/max and model_sha256')
    baseline = None if meta.get('baseline') is None else number(meta['baseline'], 'baseline')
    threshold = number(meta.get('min_improvement', '0'), 'min_improvement')
    if threshold < 0:
        raise ValueError('min_improvement must be nonnegative')
    direction = Decimal(1) if meta['sense'] == 'min' else Decimal(-1)
    events, outcomes = [], Counter()
    end = Decimal(0)
    allocated = Decimal(0)
    candidate_count = eligible_count = 0
    ids = set()
    for r in records[1:]:
        if r.get('type') != 'experiment' or not r.get('run_id') or r['run_id'] in ids:
            raise ValueError('Each experiment needs a unique run_id')
        ids.add(r['run_id'])
        start = number(r['start_s'], 'start_s')
        wall = number(r['wall_s'], 'wall_s')
        workers = number(r.get('workers', 1), 'workers')
        if start < 0 or wall < 0 or workers < 1 or workers != workers.to_integral_value():
            raise ValueError('Invalid experiment timing/workers')
        end = max(end, start + wall)
        allocated += wall * workers
        outcomes[str(r.get('status', 'UNRECORDED'))] += 1
        c = r.get('candidate')
        if c is None:
            continue
        candidate_count += 1
        a = c.get('audit', {})
        # Read only explicit, hash-bound original-model validation outcomes.
        if not (a.get('passed') is True and a.get('all_original_constraints_checked') is True
                and a.get('model_sha256', '').lower() == meta['model_sha256'].lower()
                and sha(c.get('solution_sha256'))
                and a.get('solution_sha256', '').lower() == c['solution_sha256'].lower()
                and a.get('grade') in ('exact_rational', 'decimal_zero', 'numerical')
                and a.get('report')):
            continue
        value = number(c['objective'], 'candidate objective')
        if value != number(a['recomputed_objective'], 'recomputed objective'):
            raise ValueError('Candidate objective differs from recorded audit recomputation')
        at = number(c['verified_at_s'], 'verified_at_s')
        if at < start or at > start + wall:
            raise ValueError('verified_at_s outside experiment interval (include verification time)')
        row_tol = number(a['row_tolerance'], 'row_tolerance')
        int_tol = number(a['integrality_tolerance'], 'integrality_tolerance')
        if row_tol < 0 or int_tol < 0:
            raise ValueError('Negative audit tolerance')
        if a['grade'] in ('exact_rational', 'decimal_zero') and (row_tol != 0 or int_tol != 0):
            raise ValueError('Zero/exact grade inconsistent with nonzero tolerances')
        eligible_count += 1
        events.append((at, r['run_id'], value, c))
    best = baseline
    first_feasible = None
    first_improvement = None
    trajectory = []
    for at, run_id, value, c in sorted(events, key=lambda e: (e[0], e[1])):
        if first_feasible is None:
            first_feasible = at
        gain = None if best is None else direction * (best - value)
        # Always track every strict numerical improvement, even below reporting threshold.
        if best is None or gain > 0:
            best = value
            trajectory.append({'verified_at_s': str(at), 'run_id': run_id, 'objective': str(value),
                               'gain_over_previous': None if gain is None else str(gain),
                               'declared_category': c.get('category', 'unspecified'),
                               'audit_grade': c['audit']['grade'], 'solution_sha256': c['solution_sha256']})
        baseline_gain = None if baseline is None else direction * (baseline - value)
        if baseline_gain is not None and baseline_gain > 0 and baseline_gain >= threshold and first_improvement is None:
            first_improvement = at
    improvement = None if best is None or baseline is None else direction * (baseline - best)
    return {'instance': meta.get('instance'), 'sense': meta['sense'],
            'baseline': None if baseline is None else str(baseline),
            'best_objective': None if best is None else str(best),
            'improvement_over_baseline': None if improvement is None else str(improvement),
            'relative_improvement': None if improvement is None else str(improvement / max(Decimal(1), abs(baseline))),
            'first_recorded_valid_candidate_s': None if first_feasible is None else str(first_feasible),
            'first_baseline_improvement_s': None if first_improvement is None else str(first_improvement),
            'no_baseline_requires_first_feasible_metric': baseline is None,
            'observed_elapsed_s': str(end), 'allocated_worker_seconds': str(allocated),
            'runs': len(ids), 'statuses': dict(outcomes), 'candidate_records': candidate_count,
            'eligible_audited_candidate_records': eligible_count, 'trajectory': trajectory,
            'warning': 'Summary of supplied audit records only; audit files/hashes and MPS feasibility were NOT replayed. Worker-seconds are allocation estimates, not measured CPU time. Compare grades/categories separately.'}


def summarize(records):
    with localcontext() as context:
        context.prec = 80
        return _summarize(records)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('ledger', type=Path)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    try:
        records = [json.loads(line) for line in args.ledger.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
        result = summarize(records)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        ap.error(str(exc))
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        if args.output.resolve() == args.ledger.resolve():
            ap.error('Output must not overwrite input ledger')
        args.output.write_text(rendered, encoding='utf-8')
    print(rendered, end='')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Retrieve compact frozen case evidence; does not read or solve an MPS."""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--name', help='Exact case name; substring fallback')
    group.add_argument('--family', help='Family key; use --list-families to inspect')
    group.add_argument('--list-families', action='store_true')
    ap.add_argument('--limit', type=int, default=8)
    args = ap.parse_args()
    if args.limit < 1:
        ap.error('--limit must be positive')
    index = json.loads((Path(__file__).resolve().parents[1] / 'references' / 'instances.json').read_text(encoding='utf-8'))
    if args.list_families:
        print(json.dumps(index['family_counts'], ensure_ascii=False, indent=2))
        return
    cases = index['instances']
    if args.name:
        exact = [r for r in cases if r['name'].casefold() == args.name.casefold()]
        cases = exact or [r for r in cases if args.name.casefold() in r['name'].casefold()]
    else:
        cases = [r for r in cases if r['family'] == args.family]
    if not cases:
        ap.error('No matching frozen case; do not infer a classification for this instance.')
    keys = ('name', 'family', 'structure', 'primal_category', 'project_comparison',
            'repository_summary', 'next_primal_route', 'transferable_route', 'limitation', 'source_url')
    print(json.dumps({'snapshot_commit': index['snapshot_commit'], 'matches': len(cases),
                      'cases': [{k: r[k] for k in keys} for r in cases[:args.limit]]}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

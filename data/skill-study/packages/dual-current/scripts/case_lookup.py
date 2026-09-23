#!/usr/bin/env python3
"""Print matching dual case records without loading the whole corpus into context."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', help='Exact instance name, name fragment, or family')
    args = parser.parse_args()
    data = json.loads((Path(__file__).resolve().parents[1]/'references/corpus-index.json').read_text(encoding='utf-8'))
    if args.query is None:
        print(json.dumps({k:v for k,v in data.items() if k != 'instances'}, ensure_ascii=False, indent=2))
        return 0
    query = args.query.casefold()
    exact = [r for r in data['instances'] if r['name'].casefold() == query]
    rows = exact or [r for r in data['instances'] if query in r['name'].casefold() or query == r['family'].casefold()]
    print(json.dumps(rows, ensure_ascii=False, indent=2))
    return 0 if rows else 1


if __name__ == '__main__':
    raise SystemExit(main())

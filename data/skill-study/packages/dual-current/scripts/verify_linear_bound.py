#!/usr/bin/env python3
"""Exact weak-duality bound for a supplied sparse linear JSON model.

Verifies neither an original MPS map nor branching/cuts. Standard library only.
See references/linear-certificate.md for the closed schema and trust boundary.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise ValueError('Exact numbers must be decimal/fraction strings or integers')
    return Fraction(value)


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f'Duplicate JSON key: {key}')
        out[key] = value
    return out


def read_json(raw):
    return json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique_object)


def fields(obj, required, optional=()):
    if not isinstance(obj, dict) or not set(required) <= set(obj) or set(obj)-set(required)-set(optional):
        raise ValueError(f'Invalid schema; expected {required}, optional {optional}')


def verify(model, cert, model_sha256):
    fields(model, ('format', 'sense', 'offset', 'variables', 'rows'))
    fields(cert, ('format', 'model_sha256', 'multipliers'), ('claimed_bound',))
    if model['format'] != 'linear-box-v1' or cert['format'] != 'linear-bound-v1':
        raise ValueError('Unsupported format')
    if cert['model_sha256'] != model_sha256:
        raise ValueError('Model hash mismatch')
    if model['sense'] not in ('min', 'max'):
        raise ValueError('Invalid objective sense')
    if not isinstance(model['variables'], list) or not isinstance(model['rows'], list):
        raise ValueError('Variables and rows must be lists')
    if not isinstance(cert['multipliers'], dict):
        raise ValueError('Multipliers must be an object')
    sign = 1 if model['sense'] == 'min' else -1
    bounds, residual = {}, {}
    for var in model['variables']:
        fields(var, ('name', 'cost', 'lb', 'ub'))
        name = var['name']
        if not isinstance(name, str) or not name or name in bounds:
            raise ValueError('Invalid or duplicate variable name')
        lo = None if var['lb'] is None else rational(var['lb'])
        hi = None if var['ub'] is None else rational(var['ub'])
        if lo is not None and hi is not None and lo > hi:
            raise ValueError('Reversed bounds')
        bounds[name] = (lo, hi)
        residual[name] = sign*rational(var['cost'])
    total = sign*rational(model['offset'])
    row_names = set()
    for row in model['rows']:
        fields(row, ('name', 'sense', 'rhs', 'coefficients'))
        name = row['name']
        if not isinstance(name, str) or not name or name in row_names:
            raise ValueError('Invalid or duplicate row name')
        row_names.add(name)
        if row['sense'] not in ('>=', '<=', '='):
            raise ValueError('Invalid row sense')
        y = rational(cert['multipliers'].get(name, 0))
        if (row['sense'] == '>=' and y < 0) or (row['sense'] == '<=' and y > 0):
            raise ValueError(f'Wrong multiplier sign: {name}')
        total += y*rational(row['rhs'])
        if not isinstance(row['coefficients'], dict):
            raise ValueError('Coefficients must be an object')
        for var, value in row['coefficients'].items():
            if var not in bounds:
                raise ValueError(f'Unknown column: {var}')
            residual[var] -= y*rational(value)
    if set(cert['multipliers']) - row_names:
        raise ValueError('Multiplier references an unknown row')
    nonzero = 0
    for name, coefficient in residual.items():
        if coefficient == 0:
            continue
        nonzero += 1
        endpoint = bounds[name][0 if coefficient > 0 else 1]
        if endpoint is None:
            raise ValueError(f'No finite bound: residual at unbounded endpoint for {name}')
        total += coefficient*endpoint
    value = sign*total
    if 'claimed_bound' in cert:
        claimed = rational(cert['claimed_bound'])
        if sign*claimed > total:
            raise ValueError('Claim exceeds the certified bound strength')
    return {'verified_for_supplied_linear_model': True,
            'original_mps_mapping_verified': False,
            'model_sha256': model_sha256,
            'sense': model['sense'],
            'bound_type': 'lower' if sign == 1 else 'upper',
            'bound_exact': str(value),
            'residual_corrections': nonzero}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', type=Path)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    try:
        raw = args.model.read_bytes()
        result = verify(read_json(raw), read_json(args.certificate.read_bytes()), hashlib.sha256(raw).hexdigest())
    except (ValueError, TypeError, KeyError, OSError, ZeroDivisionError) as error:
        print(json.dumps({'verified_for_supplied_linear_model': False, 'error': str(error)}))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())

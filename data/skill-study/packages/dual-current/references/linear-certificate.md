# Small rational linear-bound checker

Use `scripts/verify_linear_bound.py` to replay a bound for a **supplied linear relaxation**, for example one geometric subproblem or one branch leaf. It uses Python's standard-library Fraction, all columns and safe box-residual correction. It does not generate multipliers or solve an LP. Prefer established full-model proof tools for large proof pipelines.

For normalized minimization, choose row multipliers y≥0 for ≥ rows, y≤0 for ≤ rows, and free y for equality rows. Set `r=c−Aᵀy`. The exact bound is

`offset + yᵀb + Σ_j min_{lb_j≤x_j≤ub_j} r_j x_j`.

Residuals need not vanish on bounded variables. On an infinite endpoint, a residual pointing to that endpoint makes this formula unbounded, so the checker rejects a finite claim. Maximization is handled by negating the entire objective first, including its offset; multipliers apply to this normalized minimization problem.

## Schema and invocation

All numbers are JSON integer literals or strings containing exact decimals/fractions. Floats are rejected. `null` means −∞ only in `lb`, +∞ only in `ub`. Duplicate keys/names, unrecognized fields, nonexistent rows/columns and wrong multiplier signs are rejected. A missing row multiplier is zero; a missing row coefficient is zero. The JSON is a continuous linear relaxation: do not silently drop indicators, quadratic terms, semi-continuous domains or integer-only conditions and call it an equivalent MPS export. Dropping integrality may be a valid but weaker relaxation; establish the actual mapping separately.

Example model (`model.json`):

```json
{
  "format": "linear-box-v1",
  "sense": "min",
  "offset": "0",
  "variables": [{"name": "x", "cost": "1", "lb": "0", "ub": "10"}],
  "rows": [{"name": "demand", "sense": ">=", "rhs": "2", "coefficients": {"x": "1"}}]
}
```

Create a certificate using the SHA-256 of the **exact model.json bytes**:

```python
import hashlib, json
from pathlib import Path
raw = Path('model.json').read_bytes()
certificate = {
    'format': 'linear-bound-v1',
    'model_sha256': hashlib.sha256(raw).hexdigest(),
    'multipliers': {'demand': '1'},
    'claimed_bound': '2'
}
Path('certificate.json').write_text(json.dumps(certificate), encoding='utf-8')
```

```text
python <skill-directory>/scripts/verify_linear_bound.py model.json certificate.json
```

Exit 0 reports an exact fraction lower bound 2. Exit 1 reports a rejected input/claim. `claimed_bound` is optional and may be weaker than the computed bound. The output always states `original_mps_mapping_verified: false` because a matching JSON hash does not prove that its model is a relaxation of the original MPS.

Before using its output as an original-MIP bound, separately verify every necessary row/domain/objective mapping, added-cut validity and completeness of any case decomposition. A valid leaf certificate is not a complete tree certificate. This helper does not implement Farkas infeasibility proofs, lattice rounding, nonlinear constraints or branch coverage. Never substitute the helper's successful exit for those missing arguments.

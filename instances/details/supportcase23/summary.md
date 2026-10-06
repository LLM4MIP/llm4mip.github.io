# supportcase23

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: -12160.659354160929084790008020999953
- Dual bound: -12345.87023419769
- Normalized gap: 0.0150018489197895776050029376489973213220936662
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: -12160.6593571676
- Primal difference (baseline minus result): -0.000003006670915209991979000047
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: -12633.1586
- Dual difference (result minus baseline): 287.28836580231

## Verification and qualifications

Public starting material required exact repair/canonicalization. No substantive primal improvement. Numerical dual is separate from the weaker independently replayed rational branch certificate.



- Primal validation: Exact rational original-MPS feasibility, zero residual
- Dual validation: See separately reported numerical and independent exact bounds
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/supportcase23/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

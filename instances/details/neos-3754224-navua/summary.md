# neos-3754224-navua

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 166345.747187400683521027956891053406115318333
- Dual bound: 56490.87734419854
- Normalized gap: 0.660400832005897789531506055730262855882133564
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 157909.0677610051
- Primal difference (baseline minus result): -8436.67942639558352102795689105340611531833266
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 56251.4076
- Dual difference (result minus baseline): 239.46974419854

## Verification and qualifications

Original strict rational witness, separately graded numerical and independent exact dual evidence, verified core final-result packages; full trial archives retained locally.

Improves repaired campaign start, but does not beat v36 headline 157909.0677610051.

- Primal validation: Exact rational original-MPS feasibility, zero residual
- Dual validation: numerical_solver
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-3754224-navua/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

# t1717

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 158260
- Dual bound: 137323.70814993372
- Normalized gap: 0.132290483066259825603437381524074308100593959
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 158260
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: 137668.992
- Dual difference (result minus baseline): -345.28385006628

## Verification and qualifications

No primal gain after separately recorded public-solution integer canonicalization. Cheapest-support equivalence, valid subset/clique cuts and pair branching were audited. Numerical global bound is stronger than the independently exact135070 certificate.



- Primal validation: Exact rational original-MPS feasibility, zero residual
- Dual validation: See separately reported numerical and independent exact bounds
- Primal comparison: No difference above 1e-7
- Dual comparison: Below historical COPT bound

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/t1717/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

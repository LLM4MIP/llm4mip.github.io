# ns930473

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Optimal
- Primal bound: 821466
- Dual bound: 821466
- Normalized gap: 0
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 821466
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 1899.50067
- Dual difference (result minus baseline): 819566.49933

## Verification and qualifications

The source arc graph forces increasing pickups followed by increasing deliveries, with at most15 requests per vehicle. Complete exact pricing covers2760 subproblems. Two independent Python integer DPs reproduce the certificate821466, matching the original feasible witness.



- Primal validation: exact
- Dual validation: exact
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/ns930473/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

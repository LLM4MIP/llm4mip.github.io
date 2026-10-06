# momentum3

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 173202.18557350038
- Dual bound: 107995.45322036758
- Normalized gap: 0.376477537724035000215508783813008078332857164
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 173202.1762194289
- Primal difference (baseline minus result): -0.00935407148
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 96179.1231
- Dual difference (result minus baseline): 11816.33012036758

## Verification and qualifications

UMTS station/user and power-repair neighborhoods produce no material primal improvement. Original-row scaling and audited power/conflict/clique inequalities strengthen the numerical global bound. The final integer decisions equal the repaired baseline decisions.



- Primal validation: tolerance_1e-9
- Dual validation: numerical
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/momentum3/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

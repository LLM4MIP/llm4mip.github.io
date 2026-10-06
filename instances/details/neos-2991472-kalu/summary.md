# neos-2991472-kalu

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Optimal
- Primal bound: 12
- Dual bound: 12
- Normalized gap: 0
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 12
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 0
- Dual difference (result minus baseline): 12

## Verification and qualifications

All13392 dense mode rows are audited. An equivalent item-pattern model closes under both COPT and Gurobi. A solver-independent proof then excludes all four possible improving omission sets using141 finite infeasibility states and6564 independently checked branches.



- Primal validation: exact
- Dual validation: exact
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-2991472-kalu/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

# shipsched

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 111919.8337342348
- Dual bound: 85777.6824670317
- Normalized gap: 0.233579253962084478655357672231151297383503721
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 111919.8337342348
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 67029.7019
- Dual difference (result minus baseline): 18747.9805670317

## Verification and qualifications

historically accepted numerical witness; not uniformly revalidated; precedence-pattern recourse, paper-motivated scheduling neighborhoods, independently verified directed-cycle inequalities, and matched global branch-and-cut controls



- Primal validation: Historical evidence grade; see instance report
- Dual validation: dual skill Gurobi
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/skills-research/comparisons/per_instance_comparison.csv)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

# scpm1

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 537
- Dual bound: 416
- Normalized gap: 0.225325884543761638733705772811918063314711359
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 540.0
- Primal difference (baseline minus result): 3
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 415.555435
- Dual difference (result minus baseline): 0.444565

## Verification and qualifications

historically accepted numerical witness; not uniformly revalidated; exact rational LP-dual replay plus deterministic cost-1 RWLS

Numerical difference shown, but frozen project attribution is not upgraded by this arithmetic audit.

- Primal validation: Historical evidence grade; see instance report
- Dual validation: dual skill Gurobi; dual skill COPT terminal
- Primal comparison: Numerically better; not project-attributed
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/skills-research/comparisons/per_instance_comparison.csv)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

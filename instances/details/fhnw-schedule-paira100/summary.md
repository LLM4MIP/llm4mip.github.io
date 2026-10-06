# fhnw-schedule-paira100

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Optimal
- Primal bound: -15.113116512593402
- Dual bound: -15.113116512593401992
- Normalized gap: Not applicable
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: -15.1131226682367
- Primal difference (baseline minus result): -0.000006155643298
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: -23.8016842
- Dual difference (result minus baseline): 8.688567687406598008

## Verification and qualifications

Computational optimum; official lower headline is nonintegral, so no numerical primal improvement is claimed

Reported numerical lower bound marginally exceeds primal; retain numerical qualification and do not clamp source values.

- Primal validation: Historical evidence grade; see instance report
- Dual validation: -15.113116512593402 (Gurobi + audited valid cuts)
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/fhnw-schedule-paira100/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

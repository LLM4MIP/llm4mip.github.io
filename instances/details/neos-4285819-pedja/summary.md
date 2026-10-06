# neos-4285819-pedja

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 88.49933630640803
- Dual bound: 62.376611386884534
- Normalized gap: 0.295174246607677786307992939321114343826351607
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 88.49933630640803
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: 63.3949254
- Dual difference (result minus baseline): -1.018314013115466

## Verification and qualifications

Exact interval propagation on both binary-gated branches justifies tightening 617068 big-M rows. The independent export audit verifies the complete matrix, bounds, types and objective. Full tight-M COPT tree gives global numerical bound 62.376611386884534, compared with initial 62.35413501686672. Primal is unchanged; local transplant bounds are excluded.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: No difference above 1e-7
- Dual comparison: Below historical COPT bound

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-4285819-pedja/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

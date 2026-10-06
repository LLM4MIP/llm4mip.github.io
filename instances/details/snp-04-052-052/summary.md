# snp-04-052-052

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 881740229.202574
- Dual bound: 880540652.1100941
- Normalized gap: 0.00136046542139148000439825948963141499370945197
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 881796490.7470638
- Primal difference (baseline minus result): 56261.5444898
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 843534432
- Dual difference (result minus baseline): 37006220.1100941

## Verification and qualifications

Joint procurement/production/inventory neighborhoods improve the strict baseline by17997.815490. Inventory-prefix, resource-grid and piecewise-capacity cuts, with independently justified initial-chain integrality, strengthen the numerical global bound.



- Primal validation: tolerance_1e-9
- Dual validation: numerical
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/snp-04-052-052/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

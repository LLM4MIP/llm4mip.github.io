# neos-5151569-mologa

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 686721918.741876557859
- Dual bound: 686532411.3768101
- Normalized gap: 0.000275959394762946903792303305716513318128468621
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 686748326.4866663
- Primal difference (baseline minus result): 26407.744789742141
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 686479073
- Dual difference (result minus baseline): 53338.3768101

## Verification and qualifications

Concurrent primal/dual, up to 8 cores per role, 2-2.5 hours; latest public seed also improved; no optimality proof



- Primal validation: Historical evidence grade; see instance report
- Dual validation: Numerical global solver bound on source-audited formulations
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-5151569-mologa/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

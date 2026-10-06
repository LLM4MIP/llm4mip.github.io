# n370b

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 1212433
- Dual bound: 1166799
- Normalized gap: 0.0376383684706701318753283686603713359831017467
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 1220708.0
- Primal difference (baseline minus result): 8275
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 1074178.91
- Dual difference (result minus baseline): 92620.09

## Verification and qualifications

Balanced blocks and joint flow/activation moves improve the primal by4333. Quantity-dependent cost splitting and two independent star DPs certify1166798.995818, hence the integer bound1166799.



- Primal validation: exact
- Dual validation: exact
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/n370b/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

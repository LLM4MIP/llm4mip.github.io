# n3707

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 1185209
- Dual bound: 1102426
- Normalized gap: 0.0698467527668115918795756697763854307552507617
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 1186691.0
- Primal difference (baseline minus result): 1482
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 1035948.62
- Dual difference (result minus baseline): 66477.38

## Verification and qualifications

Joint component rewiring and flow repair improve the primal by1482. Complete exact transportation star pricing gives1102425.083897, strengthened to1102426 using the proved integer-optimum property.



- Primal validation: exact
- Dual validation: exact
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/n3707/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

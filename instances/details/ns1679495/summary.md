# ns1679495

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 2642035.19871373
- Dual bound: 2626815.66620823
- Normalized gap: 0.00576053358899593825983764542784341714465884185
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 2642035.198713481
- Primal difference (baseline minus result): -2.49E-7
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 2556399.7
- Dual difference (result minus baseline): 70415.96620823

## Verification and qualifications

The original uncapacitated commodity-flow structure permits a487-arc shortest-path reduction. Exact station pricing and4163 independently checked conditional exclusions preserve an optimum. The strongest numerical dual is2626815.66620823; a separate exact certificate gives2612880.60890689.



- Primal validation: exact
- Dual validation: numerical
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/ns1679495/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

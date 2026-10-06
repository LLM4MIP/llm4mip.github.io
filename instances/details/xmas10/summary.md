# xmas10

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: -497
- Dual bound: -507
- Normalized gap: 0.0197238658777120315581854043392504930966469428
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: -497.0
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: -516.336258
- Dual difference (result minus baseline): 9.336258

## Verification and qualifications

See instance evidence and portable replay

The independently replayed exact forest-strip bound -507 improves the publicly reported family bound -511 by 4. The best completed solver-only numerical result remains -511. Model validity and fingerprint checks pass. Keep evidence grades separate.

- Primal validation: See original-decimal Fraction check in instance package
- Dual validation: Exact integer/rational certificate or complete DP replay
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/xmas10/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

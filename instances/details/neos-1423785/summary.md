# neos-1423785

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 21893.333343320162
- Dual bound: 20707.76431845254
- Normalized gap: 0.0541520565313709511026286854245281471854448902
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 21893.26
- Primal difference (baseline minus result): -0.073343320162
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 20327.177
- Dual difference (result minus baseline): 380.58731845254

## Verification and qualifications

7462 exact copy eliminations; 960 complementary pairs; four-link joint neighborhoods, near-point recourse and periodic search; 99 audited local-cost valid inequalities added individually to complete model



- Primal validation: See original-decimal Fraction check in instance package
- Dual validation: Numerical global bound with structural audits; no independent exact lower-bound certificate is claimed
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-1423785/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

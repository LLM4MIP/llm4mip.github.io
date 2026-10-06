# supportcase38

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 32564.500162611843
- Dual bound: 32476.03269588074
- Normalized gap: 0.00271668431234436140952557971223165494174948017
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 32873.9683458331
- Primal difference (baseline minus result): 309.468183221257
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: 32476.0327
- Dual difference (result minus baseline): -0.00000411926

## Verification and qualifications

167 audited 15-node monotone binary chains; joint threshold/continuous neighborhoods; fixed-integer crossover and original-model warm global search; adaptive continuous-variable LP pricing

The bound difference is within half of the historical table last displayed digit; do not interpret it as a robust difference.

- Primal validation: See original-decimal Fraction check in instance package
- Dual validation: Numerical global bound with structural audits; no independent exact lower-bound certificate is claimed
- Primal comparison: Attributed improvement
- Dual comparison: Below historical COPT bound

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/supportcase38/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

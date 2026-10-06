# gasprod1-1

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Optimal
- Primal bound: 291.5265300348231
- Dual bound: 291.52653003486193
- Normalized gap: Not applicable
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 291.1753206178254
- Primal difference (baseline minus result): -0.3512094169977
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 253.271446
- Dual difference (result minus baseline): 38.25508403486193

## Verification and qualifications

Solver numerical global optimality; not an exact arithmetic or Lean proof

All4 original public vectors fail1e-9; fixed rounded integers/full original continuous repair converge to about291.5265336024; repair is not claimed as a new primal record Reported numerical lower bound marginally exceeds primal; retain numerical qualification and do not clamp source values.

- Primal validation: See original-decimal Fraction check in instance package
- Dual validation: Numerical global bound with structural audits; no independent exact lower-bound certificate is claimed
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/gasprod1-1/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

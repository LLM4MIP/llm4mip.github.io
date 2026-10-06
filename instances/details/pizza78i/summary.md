# pizza78i

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Optimal
- Primal bound: 564039
- Dual bound: 564039
- Normalized gap: 0
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 564039
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 508093
- Dual difference (result minus baseline): 55946

## Verification and qualifications

Exact original-model optimum: a source-derived voucher projection proves a lower bound of 564039 and an independently checked original integer witness attains it. This conclusion comes from the finite combinatorial proof, not the earlier COPT bound 495580.380952381. Read reports/PROOF.md for the implication chain and Lean obligations.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: exact_original_global_optimal
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/pizza78i/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

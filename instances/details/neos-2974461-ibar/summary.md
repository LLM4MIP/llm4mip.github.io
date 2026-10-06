# neos-2974461-ibar

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 468906174.771
- Dual bound: 443920829.19063455
- Normalized gap: 0.0532843176837403746060212275617374011157730325
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 468906174.771
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 429197921
- Dual difference (result minus baseline): 14722908.19063455

## Verification and qualifications

The lower bound is numerical COPT on a full source-audited global model, with structural signatures and exported row/domain/objective checks. The original feasible incumbent is unchanged. Reduced or fixed primal neighborhoods are excluded from global aggregation.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-2974461-ibar/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

# ivu06-big

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 140.412332083
- Dual bound: 135.44891253182323
- Normalized gap: 0.0353488862234893473847466913879474960561181893
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 140.74
- Primal difference (baseline minus result): 0.327667917
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 135.430283
- Dual difference (result minus baseline): 0.01862953182323

## Verification and qualifications

The selected 111-duty original 0/1 partition improves the frozen primal 140.74366634 to 140.412332083, with zero original row/domain residuals. Completed original-model COPT gives numerical dual 135.44891253182323. Separate exact raw-source branch-and-price replay proves 67723688451/500000000 by exhaustive region coverage and the minimum over the surviving frontier. Restricted column-pool bounds are excluded.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/ivu06-big/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

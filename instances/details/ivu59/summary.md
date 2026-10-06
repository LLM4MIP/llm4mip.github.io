# ivu59

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 911.94105059
- Dual bound: 885
- Normalized gap: 0.0295425352028729315675667526701814946531828106
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 927.8947518206729
- Primal difference (baseline minus result): 15.9537012306729
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 884.788371
- Dual difference (result minus baseline): 0.211629

## Verification and qualifications

Validated original partition exchanges improve frozen primal 912.70015745 to 911.94105059. Exact reduced-cost exclusion preserves every solution in the cap-885 region; completed COPT INFEASIBLE in that region, together with the outside-cap cover, proves numerical global lower bound 885. Display the floating excess 885.0000000000076 as 885. The independent exact parity-price certificate is 884462983177/1000000000. Advisory reduced costs used for primal proposals are not asserted dual-feasible.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/ivu59/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

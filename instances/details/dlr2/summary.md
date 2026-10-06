# dlr2

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 18265839.45029593
- Dual bound: 11601762.345761254
- Normalized gap: 0.364838261207136002356627099491044926623813891
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 18311711.89666227
- Primal difference (baseline minus result): 45872.44636634
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: No finite bound
- Dual difference (result minus baseline): Not applicable

## Verification and qualifications

The final original-validated primal improves the frozen 18311711.896662273 baseline by 45872.44636634365. The dual is the completed full-original LP optimum 11601762.345761254. Research ended within its original clock, but the initial evidence seal missed the deadline. A later artifact-only repair made zero optimization calls: late_delivery=true and within_original_hard_deadline=false. The published sparse SOL deletes only exactly zero entries from the dense archived SOL, preserving the represented point.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: Attributed improvement
- Dual comparison: No finite historical COPT bound

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/dlr2/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

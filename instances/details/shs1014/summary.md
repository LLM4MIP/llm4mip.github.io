# shs1014

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 22671.197441887947
- Dual bound: 22555.8775122676
- Normalized gap: 0.00508662720246433165168487335317373065970245084
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 22671.19742691877
- Primal difference (baseline minus result): -0.000014969177
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: 23116.6794
- Dual difference (result minus baseline): -560.8018877324

## Verification and qualifications

The accepted global numerical bound is 22555.8775122676 from an audited network projection. Conflicting larger continuation dual values are quarantined. The displayed primal is a numerical point; the separate exact feasible witness has objective 22671.197441887947. This is numerical polishing only.

Use the archived exact primal value rather than the rounded or numerical catalogue display; the original display is retained separately. Historical COPT lower bound exceeds the archived feasible primal. Kept as a baseline inconsistency, not a valid superiority comparison.

- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: Above v36 primal
- Dual comparison: Historical bound exceeds feasible primal

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/shs1014/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

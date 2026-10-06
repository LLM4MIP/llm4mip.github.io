# rfds-4-days

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: -1129915.8646
- Dual bound: -1146278.6542107703
- Normalized gap: 0.0142747049774178348692325467654232313293061775
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: -1129915.8646
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: -1157062.2
- Dual difference (result minus baseline): 10783.5457892297

## Verification and qualifications

QUALIFIED numerical global dual: the strongest full-original run also produced an incumbent with original-row violation 1142141.00397197; that candidate is rejected. Preserve the raw solver dual with this numerical qualification. Independent full-original runs gave -1147434.3976039088 and LP -1158940.9781666666. No optimality or primal improvement is claimed. The retained primal passes the complete original-model checker.

QUALIFIED numerical global dual: the strongest full-original run also produced an incumbent with original-row violation 1142141.00397197; that candidate is rejected. Preserve the raw solver dual with this numerical qualification. Independent full-original runs gave -1147434.3976039088 and LP -1158940.9781666666. No optimality or primal improvement is claimed. The retained primal passes the complete original-model checker.

- Primal validation: Historical evidence grade; see instance report
- Dual validation: qualified_numerical_original_global
- Primal comparison: No difference above 1e-7
- Dual comparison: Excluded: qualified numerical bound

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/rfds-4-days/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

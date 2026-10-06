# scpn2

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 485
- Dual bound: 352
- Normalized gap: 0.274226804123711340206185567010309278350515464
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 485.0
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 350.409358
- Dual difference (result minus baseline): 1.590642

## Verification and qualifications

Completed full-original COPT lower bound 351.0207653022212 gives 352 on the exact integer objective lattice. A separate complete-source rational price certificate proves 351 exactly. Restricted covering/repair masters do not give global bounds. Original validated primal remains 485.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/scpn2/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

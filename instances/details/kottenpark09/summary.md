# kottenpark09

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 1715
- Dual bound: 230
- Normalized gap: 0.865889212827988338192419825072886297376093294
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 1715.0
- Primal difference (baseline minus result): 0
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 183.5
- Dual difference (result minus baseline): 46.5

## Verification and qualifications

Two raw-source auditors prove integrality-preserving relaxation of 2734670 assignment columns: 1780414 unique binary-margin intersections and 954256 forced zeros. All original rows/domains/objective are retained. An equivalent global model adds 7920 source-proved gated-day cuts. Completed clean COPT API bound 229.199999999994 rounds to 230 using the exact 5Z objective lattice. F=0,z<=1710 pilots are conditional and cannot supply a standalone global bound. The primal 1715 is unchanged.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: No difference above 1e-7
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/kottenpark09/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

# ds-big

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 194.49841415
- Dual bound: 178.14457882305123
- Normalized gap: 0.0840821011236444058173828560236618258308817167
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 194.58674798
- Primal difference (baseline minus result): 0.08833383
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 87.2719112
- Dual difference (result minus baseline): 90.87266762305123

## Verification and qualifications

The global numerical lower bound is the minimum over a source-audited exhaustive dummy-count/parity partition, including syndrome-class trees. The conditional class bound alone is insufficient. Separate exact source/price certificates prove 118.008983109. The exact feasible primal remains 194.49841415; solver tolerance polishing is recorded separately.

Numerical difference shown, but frozen project attribution is not upgraded by this arithmetic audit.

- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: Numerically better; not project-attributed
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/ds-big/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

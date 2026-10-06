# tpl-tub-ws1617

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 121065
- Dual bound: 120885
- Normalized gap: 0.00148680460909428819229339610952793953661256350
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 121066.0
- Primal difference (baseline minus result): 1
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: 120987.401
- Dual difference (result minus baseline): -102.401

## Verification and qualifications

The completed full-original COPT API lower bound 120884.16551379114 rounds to 120885 through an independently audited optimum-equivalent integer-objective projection. The source proof covers the necessary continuous-variable rounding without deleting costs or constraints. Frozen public baseline is 121065, not the historical headline 121066.

Numerical difference shown, but frozen project attribution is not upgraded by this arithmetic audit.

- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: Numerically better; not project-attributed
- Dual comparison: Below historical COPT bound

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/tpl-tub-ws1617/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

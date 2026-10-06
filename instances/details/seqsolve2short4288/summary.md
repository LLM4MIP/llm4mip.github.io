# seqsolve2short4288

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 83.99999983543596
- Dual bound: 17
- Normalized gap: 0.797619047222563961808284579923535904070475708
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 83.9999999999994
- Primal difference (baseline minus result): 1.6456344E-7
- Dual improvement vs historical COPT 10h: False
- Historical COPT 10h dual: 33.1143818
- Dual difference (result minus baseline): -16.1143818

## Verification and qualifications

The full source-audited global numerical bound 16.876334243370593 rounds upward to 17 on the proved integer objective lattice. The primal difference from 84 is numerical polishing, not a discrete improvement. Valid structural/site-gap cuts and complete exported-model audits are recorded; restricted primal neighborhoods never supply global bounds.

Numerical difference shown, but frozen project attribution is not upgraded by this arithmetic audit.

- Primal validation: Historical evidence grade; see instance report
- Dual validation: numerical_global_with_exact_source_audit
- Primal comparison: Numerically better; not project-attributed
- Dual comparison: Below historical COPT bound

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/seqsolve2short4288/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

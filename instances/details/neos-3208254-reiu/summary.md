# neos-3208254-reiu

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Optimal
- Primal bound: -34902
- Dual bound: -34902
- Normalized gap: 0
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: -34897.00052514407
- Primal difference (baseline minus result): 4.99947485593
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: -38606.2553
- Dual difference (result minus baseline): 3704.2553

## Verification and qualifications

The original model implies a rooted binary tree with exact ancestry. A Huffman lower bound plus a tail/cherry correction gives -34902, attained by an independently checked original witness.



- Primal validation: exact
- Dual validation: exact
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-3208254-reiu/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

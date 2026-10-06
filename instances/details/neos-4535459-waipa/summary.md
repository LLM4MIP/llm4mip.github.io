# neos-4535459-waipa

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 23331046
- Dual bound: 15474160.819061
- Normalized gap: 0.336756662386204201903335152654535934651193950
- Primal improvement vs MIPLIB v36: True
- MIPLIB v36 primal: 26040609.0
- Primal difference (baseline minus result): 2709563
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 0
- Dual difference (result minus baseline): 15474160.819061

## Verification and qualifications

Source-audited 800-job/200-machine flowshop single-job insertion descent improves primal from 26040609 to 23331046. Reconstruct the full original variable vector and verify all original rows/domains. Job head/tail inequalities plus nested-prefix assignment potentials prove the exact dual 15474160819061/1000000; the independent certificate checker verifies all 640000 potential inequalities. Relaxation optima are not original-model optimality results.



- Primal validation: Historical evidence grade; see instance report
- Dual validation: exact_original_global_lower_bound
- Primal comparison: Attributed improvement
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-4535459-waipa/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

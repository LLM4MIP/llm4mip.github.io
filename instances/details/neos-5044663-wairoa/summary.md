# neos-5044663-wairoa

Result snapshot: 2026-10-06.

## Current result

- Conclusion: Open
- Primal bound: 4654500
- Dual bound: 4654300
- Normalized gap: 0.0000429691696207970780964657857986894403265656891
- Primal improvement vs MIPLIB v36: False
- MIPLIB v36 primal: 4654484.555290672
- Primal difference (baseline minus result): -15.444709328
- Dual improvement vs historical COPT 10h: True
- Historical COPT 10h dual: 4654134.39
- Dual difference (result minus baseline): 165.61

## Verification and qualifications

Public headline4654484.555290672 fails strict original feasibility. Its canonical strict repair is4654500, which was not improved. Numerical4654300 uses an audited objective100 lattice and cutoff transfer; independent exact certificate proves4654200.



- Primal validation: Exact rational original-MPS feasibility, zero residual
- Dual validation: See separately reported numerical and independent exact bounds
- Primal comparison: Above v36 primal
- Dual comparison: Improved

## Files and provenance

[Result data](result.json) · [Source research record](https://github.com/Huangyc98/MIPLIB_openproblem/blob/organize/complete-results-20260921/instances/neos-5044663-wairoa/README.md)

The result bundle contains this summary, the current result data, and the project license.
Source research records may require repository access. Solver logs and full proof archives
are not embedded in this compact result bundle. Numerical and tolerance-based conclusions
retain their stated qualifications; the source-model qualification for tagus is recorded
in its own result. These are project results against fixed baselines, not a live leaderboard.

# neos-3682128-sandon

Snapshot: 21 September 2026. Repository research results; not a live MIPLIB leaderboard.

## Current result

- Cohort: subsequent20
- Status: Certified optimality / infeasibility
- Primal: 34666770.0
- Dual / certificate: 34666770
- Global conclusion: OPT = 34666770.0
- Evidence: Portable exact certificate
- Project primal update vs MIPLIB v36: False (not_in_project_primal_table)
- Dual improvement vs historical COPT 10h: True

exact closure witness; complete machine-configuration enumeration with exact rational duals and an exact original-MPS lift

Best-of separate runs; selected numerical D may exceed independent certified D

## Evidence and provenance

[Instance evidence](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/skills-research/comparisons/per_instance_comparison.csv) · [Complete campaign ledger](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/results/catalogue.json)

The full campaign contains 132 instances: 112 original cases and 20 subsequent evaluation cases.
The subsequent cohort uses post-hoc best valid bounds from separate skill runs; numerical bounds
and independently certified bounds are distinct. Genus g31 closures accept residuals below 1e-10.

## Download scope

The result bundle contains this summary, the per-instance ledger and license. Detailed experiment records and certificates are linked in the research repository; they are not embedded in this compact bundle.

Archive SHA-256: `9cdd65984a0bbb537e14d151a54e6e7fb5adc50d196d6ea83bd36711bcce76d7`

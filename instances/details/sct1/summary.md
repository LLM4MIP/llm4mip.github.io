# sct1

Snapshot: 21 September 2026. Repository research results; not a live MIPLIB leaderboard.

## Current result

- Cohort: subsequent20
- Status: Verified feasible; open
- Primal: -187.52765083903063
- Dual / certificate: -199.81870652161473
- Global conclusion: Not established
- Evidence: See the stated numerical tolerances and source audits.
- Project primal update vs MIPLIB v36: False (not_in_project_primal_table)
- Dual improvement vs historical COPT 10h: True

historically accepted numerical witness; not uniformly revalidated; structure-guided exact fixed-outside neighborhoods, local branching, exact LP dual certification, and an original-model global control

Best-of separate runs; selected numerical D may exceed independent certified D

## Evidence and provenance

[Instance evidence](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/skills-research/comparisons/per_instance_comparison.csv) · [Complete campaign ledger](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/results/catalogue.json)

The full campaign contains 132 instances: 112 original cases and 20 subsequent evaluation cases.
The subsequent cohort uses post-hoc best valid bounds from separate skill runs; numerical bounds
and independently certified bounds are distinct. Genus g31 closures accept residuals below 1e-10.

## Download scope

The result bundle contains this summary, the per-instance ledger and license. Detailed experiment records and certificates are linked in the research repository; they are not embedded in this compact bundle.

Archive SHA-256: `0a5576152f56b13c11de7eb1c562acaf9bbe4aaa379dbff42b59413fac91ca91`

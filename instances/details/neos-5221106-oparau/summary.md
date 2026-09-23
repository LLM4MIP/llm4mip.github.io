# neos-5221106-oparau

Snapshot: 21 September 2026. Repository research results; not a live MIPLIB leaderboard.

## Current result

- Cohort: subsequent20
- Status: Verified feasible; open
- Primal: 52.07
- Dual / certificate: 42.54
- Global conclusion: Not established
- Evidence: See the stated numerical tolerances and source audits.
- Project primal update vs MIPLIB v36: True (numeric_improvement)
- Dual improvement vs historical COPT 10h: True

historically accepted numerical witness; not uniformly revalidated; incumbent-capped exact mode-4 projection plus exact route exchange and assignment-radius search

Best-of separate runs; selected numerical D may exceed independent certified D

## Evidence and provenance

[Instance evidence](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/skills-research/comparisons/per_instance_comparison.csv) · [Complete campaign ledger](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/results/catalogue.json)

The full campaign contains 132 instances: 112 original cases and 20 subsequent evaluation cases.
The subsequent cohort uses post-hoc best valid bounds from separate skill runs; numerical bounds
and independently certified bounds are distinct. Genus g31 closures accept residuals below 1e-10.

## Download scope

The result bundle contains this summary, the per-instance ledger and license. Detailed experiment records and certificates are linked in the research repository; they are not embedded in this compact bundle.

Archive SHA-256: `b5c9846349a66c5106901e31f21d74d7fa14619cc41765d983be4348f71411d9`

# graphdraw-grafo2

Snapshot: 21 September 2026. Repository research results; not a live MIPLIB leaderboard.

## Current result

- Cohort: subsequent20
- Status: Verified feasible; open
- Primal: 68590.5
- Dual / certificate: 53513.5
- Global conclusion: Not established
- Evidence: See the stated numerical tolerances and source audits.
- Project primal update vs MIPLIB v36: True (numeric_improvement)
- Dual improvement vs historical COPT 10h: True

historically accepted numerical witness; not uniformly revalidated; objective-graph degree and disconnected-component restricted LNS with original-MPS replay

Best-of separate runs; selected numerical D may exceed independent certified D

## Evidence and provenance

[Instance evidence](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/skills-research/comparisons/per_instance_comparison.csv) · [Complete campaign ledger](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b63b89634917ccde2f9e7dc7aefe1583a3eb55e8/results/catalogue.json)

The full campaign contains 132 instances: 112 original cases and 20 subsequent evaluation cases.
The subsequent cohort uses post-hoc best valid bounds from separate skill runs; numerical bounds
and independently certified bounds are distinct. Genus g31 closures accept residuals below 1e-10.

## Download scope

The result bundle contains this summary, the per-instance ledger and license. Detailed experiment records and certificates are linked in the research repository; they are not embedded in this compact bundle.

Archive SHA-256: `1e471503dcf7d455eddf2fc1ee060dbe6382adeb3073d1407bf26f2f637a7ba0`

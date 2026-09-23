# `mip-primal-improve`: handoff for the 20-instance MIPLIB experiment

This directory preserves the controlled primal-search experiment using `mip-primal-improve` on 20 MIPLIB instances. It enables subsequent agents to reconstruct the workflow, verify conclusions and compare results with the general-skill and dual-skill experiments.

## Identify the experimental skill version first

This experiment used the skill frozen on 2026-09-14. The currently distributed repository version was updated to COPT-first after the experiment; the two versions must not be conflated.

|  Object |  `SKILL.md` SHA-256  |  Meaning |
|---|---|---|
| Experimental freeze version |  `1bab6d94a097dcb4f0506a4b03120aee57fa9c829ca7250ed066fd7782feb341`  | The skill to actually generate the result of this 20 instance |
| Current release |  `ae0b7e8b8c3578ce06d7158f05e3535c1321e097c916295632281f707a470753`  | Experimentally converted to a COPT-first version |

The freeze version is in [`sources/skill-used/` ](sources/skill-used/), the current version is in [`skills/mip-primal-improve/` ](../../../skills/mip-primal-improve/)]. The default sequence of the current skill is: Pre-detect COPT; COPT missing; License unavailable or unable to maintain the model semantics, then search for Gurobi; CuOPT under applicable conditions, and other compatible backend.

The experiment was actually primarily conducted at Euler4 using Gurobi 13.0.2. Altman's COPT 8.0.4 passed the four parallel small model capability test and served as a public model source and an optional back-end; it did not become the main back-end of the final 20 instance experiment.

##  Fixed protocol

-  The experiment ID is `mip_primal_skill20_20260914T2328CST`
- original prompt SHA- 256 :  `849e3886025a907c05b6b29fd9cc58e7b2cb0947ab16365997163024098311ff`
-  Example number: 20
-  Budget for each instance: 150 minutes
-  Checkpoint: 30, 60, 90, 120, 150 minutes
-  Schedule: 5 fixed batch, each batch 4 instance; evidence integrity barrier between batches
-  Maximum concurrency: 4 for a different instance
-  Base Seeds: 20260911; the actual seeds and parameters of each phase are maintained in a complete running list
-  Euler4 Per instance Resources: 12 CPU slot, Gurobi `SoftMemLimit=80` decimal GB; declared global upper limit is 48 slots, 320 GiB
-  Significantly improved threshold: directional improvement strict greater than `max(1e-6, 1e-9 × max(1, |verified baseline|))`
-  Data isolation: prohibited from reading the prompt, script, log, solution, report and objective instance of other skill experiments, internal research; objective case queries of skill are closed

`SoftMemLimit=80` represents 80 × 10 ^ 9 bytes, about 74.51 GiB. Some workers have another 80 GiB `RLIMIT_AS`; these restrictions are not a hard guarantee of RSS aggregation.

##  Complete process of experimentation

Each instance follows the same outward process:

1.  Freeze the original MPS, SHA-256, objective sense, public headline, independently verifiable baseline, budget and random seed.
2.  Create structural cards, identify real discrete decisions, complete variables, combine constraints and already existing solutions.
3.  Independent verification public or already a solution; public headline records separated from actual verifiable vectors.
4.  Execute a restricted primal baseline, then use an incumbent transfer based on a combination of structure and stagnation signals, Gurubi primal/NoRel/RINS, continuous recourse after a fixed integer, structured LNS, local branching, joint destroy-and-repair, compact reformulation, determination lifting, solution, pool rearrangement and boundary kick.
5.  Each candidate must be sequenced back into the original variable space and independently checked on the untouched original model. The solver incumbent, rounded hint, or the limited model optimal solution cannot be updated before verification is complete.
6.  Each improvement continues to be searched; the first improvement is just a milestone, current, best, failure range and recovery status respectively.
7.  Insert the incumbent who has verified at the time in the minutes 30 / 60 / 90 / 120 / 150; stop the candidate search and complete the budget verification at the minute 150.
8.  A set of four instances will be added to the next set of instances only after they have formed the final proof.
9.  Finally, aggregate trajectories, verification results, methods, resource records, and protocol biases. Failures, no improvements, and infrastructure anomalies are all retained in the denominator of an instance of 20.

Most `run_manifest.json` files retain the old `not_reached` placeholders in `checkpoint_schedule[].status`, even when the corresponding trajectory checkpoints exist. Use `primal_trajectory.csv` and `summary.csv` to determine checkpoint completion, not that placeholder field. `ger50-17-trans-dfn-3t` has two distinct 30-minute observations; the machine-readable table retains both original rows without deduplication.

##  Verification throughput

20 is the main classification for the final result `numerical`.

The main verifier checks the original variable solution of the actual landing disk using `1e-6` to check the variable domain, bounds, integrality, ordinary and ranged rows, applicable extension constraint, objective sense and constant, and all-variable-fix model verification. GMP only provides additional arbitrary precision numerical evidence: linear line and objective tolerance `1e-5`, integer tolerance `1e-4`.

These checks are not equivalent to zero tolerance exact feasibility, nor do they constitute globally optimal proof. The original report label for `scpm1` is `numerical+GMP explicit tolerances`, and still cannot be written as exact. The `OPTIMAL`, `CUTOFF` or `INFEASIBLE` of the restricted neighborhood only close the local range of their explicit declarations.

## result

The 20 / 20 instance forms a terminal record, and the 5 batch barrier is all complete, with no remaining owned process.

-  By instance wall clock and: `3000.00151331822077` minute
-  meaningful-active Time and: `2627.11802992026012` Minutes
-  Solver process time and: `2559.12273121935710` minutes
- Reserved worker-seconds: `2160000.0`
-  Example of an accepted improvement: 6
-  13 is the most commonly used method of improvement.
-  Substantial improvement in the pre-declared significance and attribution qualities of the original report instance: 4 / 20

The numerical is an instance-by-instance approximation, not a parallel experiment. `allocated_worker_seconds` is a resource reservation, not a test of CPU consumption.

`accepted_improvement_count` is an explanation field based on a pre-declared comparator, the rules of significance and attribution, which cannot be redirected through the trajectory of the accepted row count or the number of times the objective value changes. For example, `r4l4-02-tree-bounds-50` has more accepted rows, but only 5 is counted in that field.

| Instance | Comparison | Finally verified primal | Improvements in direction |  accepted updates  | First and last improvement |
|---|---:|---:|---:|---:|---:|
| `graphdraw-grafo2` | 68613.49999999869 | 68590.5 | 22.999999998690328 | 3 | 25.535 / 61.180 min |
| `cmflsp60-36-2-6` | 73891245.38458703 | 73891245.26398355 | 0.12060348 | 1 | 130.553 / 130.553 min |
| `r4l4-02-tree-bounds-50` | official 499132179.0015595 | 499061405.0 | 70774.0015595 vs official | 5 | 26.209 / 147.751 min |
| `ns1856153` | 34.163461799659395 | 34.01697312588409 | 0.146488673775305 | 2 | 24.314 / 30.151 min |

`r4l4-02-tree-bounds-50` has no independently verified initial baseline available; it can only report improvements to the relative freeze official value and cannot be filled in the verified-baseline improvement column.

The remainder of the results require separate explanation:

-  `eva1aprime6x6opt`: 1 accepted the numerical-polish update, changing the `0.000001485198708`.
-  `shipsched`: 1 accepted the numerical-polish update, changing the `0.00045377348`.
-  `zeil`: A numerical change of about `3.436e-10`, `accepted_improvement_count=0`.
-  `cdma`: Get first feasible, not an improvement on a verified baseline.
-  `rocII-8-11`:external transfer, not an improvement generated by this experiment.
-  `ns1456591`: The final numerical value decreases to `0.0002388874898`, but does not exceed the pre-declared relative significant threshold, classified as `no_improvement`.

The final residuals or integrality deviations for `polygonpack4-10`, `cmflsp60-36-2-6`, `ns1456591`, and `sct1` are close to `1e-6`. Comparisons must retain the actual residuals and tolerances, not merely pass/fail labels.

##  Protocol deviations and boundary conclusions

The most important deviation from concurrent fairness occurs in `scpm1`: sample evidence shows that duplicate controller/native search overlaps about 35.2 per second. The largest parallel of different instances is still 4, but the total number of candidate/search processes in a sample string reaches 5. This deviation must be maintained with the result.

The remaining biases mainly involve authentication interruptions, parser/setup failures, controller recovery, license, environment, log renaming, read-only transmissions and cap back data. Failure of no valid native child, passive waiting and read-only sorting are not counted as meaningful-active time. Machine-readable summaries see [`protocol-deviations.jsonl` ](protocol-deviations.jsonl), complete details are left in each instance's report, manifesto and original ledger].

This experiment examined only primal feasible solution and incumbent improvement. It did not organize an independent dual-bound campaign, nor did it prove any instance globally optimal.

##  Read sequence of subsequent AI

1.  Please read this document and [`COMPARISON_CONTRACT.md` ](COMPARISON_CONTRACT.md)].
2.  Read [`experiment_manifest.json` ](experiment_manifest.json) Confirmation of the identity of experiments, skills and resources.
3.  `instance_results.csv` ](instance_results.csv), `trajectories.csv` ](trajectories.csv), `validation_summary.csv` ](validation_summary.csv) and `methods.csv` ](methods.csv) are used to compare machines.
4.  Read [`results.jsonl` ](results.jsonl)] when you need to preserve the original abstract value; read [`sources/summary.csv` ](sources/summary.csv) and [`sources/report.md` ](sources/report.md)] when you need to verify the original conclusion.
5.  For individual instances, read `instances/<name>/final_report.md`, `validation.json`, `primal_trajectory.csv`, `run_manifest.json`, `model_provenance.json` and `skill_audit.json` in the following order.
6.  `instances/<name>/best.sol.gz` is the final primespace solution for deterministic compression. SHA-256 after solution compression must be equal to `validation.json` and `source_sha256` in [`artifact_manifest.jsonl` ](artifact_manifest.jsonl)].
7.  When the original log, model, phase ledger, or restart state is required, move to the complete archive according to the artifact manifest.

The complete work is archived at Euler4:

```text
/data1/wyc/mip_primal_skill20_20260914T2328CST
```

The current Windows transport mirror:

```text
D:\sufe\AI4MIP\reports\mip_primal_skill20_20260914T2328CST
```

Local snapshot statistics for 29,868 files, 4,210,303,507 bytes. Git packs only retain core evidence of about 4.8 MiB, machine tables and compressed final solution; original logs, MPS, solution pools and intermediate files are positioned by path, size and SHA-256 index.

The `report_zh.md` in the experimental directory is not included in this package because it actually belongs to the general/structure experiment `controlled_miplib20_20260911_1451`. The general authority report for this primal experiment is [`sources/report.md` ](sources/report.md)].

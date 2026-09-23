# The role of `milp-structure-research` in studying 20 open MIPLIB instances

**Report date:** 2026-09-13
**Comparison:** the user-selected `milp-structure-research` run (skill run) and the user-selected report from a run without that skill (no-skill run)
**Instances:** 20
**Problem type:** all interpreted as minimization problems

## Summary

This report compares two historical studies of the same 20 open MIPLIB instances to examine the practical role of `milp-structure-research`.

The skill does not win on every numerical metric. The results support the following conclusions:

1. **The skill run finds better feasible solutions.** At absolute tolerance `1e-7`, its final selected primal bounds have 11 wins, 9 ties and 0 losses.
2. **The skill run produces stronger mathematical closure.** It provides exact global optimality certificates for `ns1456591` and `neos-3682128-sandon`; the no-skill run closes no instances.
3. **The skill run makes more strict improvements over public baselines.** Using frozen public baselines and instance-specific strict acceptance rules, it improves 4 instances, versus 2 for the no-skill run.
4. **The no-skill run advances general-purpose solver dual bounds more strongly.** It has higher dual bounds on 12 of 20 instances and smaller consistently defined symmetric gaps on 11; the skill-run counts are 8 and 9, respectively.
5. **The skill provides research discipline rather than a generic parameter recipe.** It requires inspecting the original matrix, freezing claims and baselines, formulating falsifiable structural hypotheses, separating construction from proof, mapping reduced-model results back to the original model, independent replay, and recording unsuccessful experiments and evidence levels. This clarifies why a result is credible and what to try next.

The practical recommendation is a hybrid workflow: **use the skill for structural discovery, method selection, certificate construction and auditing, then strengthen dual bounds with dedicated solver runs on the original model.**

## 1. Comparison design and limitations

### 1.1 The two groups

- **Skill run:** structured research on 20 instances under `controlled_miplib20_20260911_1451`. Each retains one of `skill_use.md`, `skill_gate.json` or `skill_read.audit.json`. Audits show that 20/20 instances passed the skill/reference reading gate before reading models or web pages or calling a solver.
- **No-skill run:** `comparisons/copt_pdf_20260912/report.md` and its PDF. The appendix records PDF and spreadsheet tools, but no `milp-structure-research`. This does not imply an absence of structural reasoning: several instances use pattern repair, local neighborhoods and problem-specific constraints. The label only indicates whether the complete skill workflow governed the run.

### 1.2 This is not a causal-effect estimate

This is a paired retrospective review, not a randomized, blinded, equal-resource A/B experiment. The groups may differ in solving time, threads, machines, solver states, starts, external baselines, tolerance handling, stopping decisions and research order. Therefore:

- We can report which group obtained better saved primal bounds, dual bounds or certificates.
- We can audit whether the skill was read before execution and whether outputs follow its required artifact structure.
- We **cannot** attribute every difference to the skill's net causal contribution or infer an average speedup on future instances.

Direct observations are distinguished from explanations of mechanisms. Observations come from saved CSVs, reports and certificates; explanations are conservative interpretations of recorded decisions.

## 2. Consistent metrics and acceptance rules

For each minimization instance:

- `P` is the objective of a verified feasible solution, a primal upper bound; lower is better.
- `D` is a valid global dual lower bound; higher is better.
- The consistent symmetric gap is `|P-D| / max(1, |P|, |D|)`; smaller is better.

Primal and dual numerical outcomes use absolute tolerance `1e-7`. The consistent gap serves cross-report comparison, not instance-level strict feasibility or optimality acceptance. In particular, 6 selected skill-run `P` values are **tolerance-indexed results**: accepted at a stated tolerance but not automatically new incumbents under stricter tolerances. These 6 instances are:

`polygonpack4-10`、`eva1aprime6x6opt`、`cmflsp60-36-2-6`、`sct1`、`shipsched`、`rocII-8-11`。

Thus "11 primal-bound wins and 9 ties for skill" describes the consistent numerical comparison; "4 versus 2 strict new public-baseline improvements" is the stricter statistic for public contributions.

## 3. Summary results

|  Metric | Skill run | No-skill run |  Explanation |
|---|---:|---:|---|
|  Better primal bound (`1e-7`) |  11  |  0  | The remaining 9 instances tie |
|  Better dual bound (`1e-7`) |  8  |  12  |  No ties |
| Smaller consistent gap |  9  |  11  | Reflects both bounds |
| Strict improvement over frozen public baseline |  4  |  2  | Instance-specific strict acceptance rules |
| Exact global optima |  2  |  0  |  `ns1456591`, `neos-3682128-sandon`  |
| Selected tolerance-indexed primal bounds |  6  | Not applicable | Not equivalent to strict incumbents |
| Instance-level prerequisite skill gates |  20/20  |  0/20  | Per-instance audit artifacts retained |

The skill run has lower selected feasible objectives on 55% of instances and ties on 45%. The no-skill run has higher dual bounds on 60% and smaller consistent gaps on 55%. The skill favors structural feasible-solution discovery and provable closure; the no-skill run favors general-purpose solver progress on global lower bounds.

## 4. Numerical comparison of all 20 instances

Lower `P` and higher `D` are better; gaps are percentages. `†` marks a tolerance-indexed skill-selected `P`. S means the skill run is better, N means the no-skill run is better, and = means a tie at `1e-7`.

| Batch | Instance | No-skill `P` |  skill `P`  | P winner | No-skill `D` |  skill `D`  | D winner | No-skill gap |  skill gap  | Gap winner |
|---:|---|---:|---:|:---:|---:|---:|:---:|---:|---:|:---:|
| 1 | graphdraw-grafo2 | 68609.5 | 68595.5 | S | 36415.846575 | 36159.784211 | N | 46.9230% | 47.2855% | N |
| 1 | polygonpack4-10 | -53594508.70758318 | -53594508.70758325† | = | -93676649.5393 | -93676450.235594 | S | 42.7878% | 42.7876% | S |
| 1 | scpm1 | 537 | 537 | = | 415 | 414 | N | 22.7188% | 22.9050% | N |
| 1 | ger50-17-trans-dfn-3t | 3969.4334 | 3969.4334 | = | 3917.155362 | 3929.073502 | S | 1.3170% | 1.0168% | S |
| 2 | eva1aprime6x6opt | -18.1009952803 | -18.1010029814† | S | -239.422770 | -495.370254 | N | 92.4397% | 96.3460% | N |
| 2 | cmflsp60-36-2-6 | 73891245.6476 | 73891244.2216† | S | 73188341.5984 | 71322258.2647 | N | 0.9513% | 3.4767% | N |
| 2 | r4l4-02-tree-bounds-50 | 499110528 | 499097063 | S | 480648435.4129 | 479452299.6157 | N | 3.6990% | 3.9361% | N |
| 2 | sct1 | -187.527649450 | -187.527650839† | S | -200.245049 | -201.483830 | N | 6.3509% | 6.9267% | N |
| 3 | shipsched | 111919.986911 | 111919.833734† | S | 81014.604552 | 79152.377477 | N | 27.6138% | 29.2776% | N |
| 3 | rocII-8-11 | -8.739844935 | -8.739845027† | = | -11.837792 | -11.854389 | N | 26.1700% | 26.2733% | N |
| 3 | ns1856153 | 34.163474399 | 34.016973126 | S | 0.0033625 | 28.9 | S | 99.9902% | 15.0424% | S |
| 3 | dc1l | 1758647.6801 | 1758647.6801 | = | 1749186.5342 | 1748341.9143 | N | 0.5380% | 0.5860% | N |
| 4 | neos-5221106-oparau | 52.67 | 52.07 | S | 0 | 42.54 | S | 100.0000% | 18.3023% | S |
| 4 | zeil | 1081.3585 | 1081.3585 | = | 815.379743 | 833.831254 | S | 24.5967% | 22.8904% | S |
| 4 | cdma | -2.296609568e16 | -2.47784784e16 | S | -3.1763448e16 | -6.382890198e16 | N | 27.6965% | 61.1798% | N |
| 4 | ns1456591 | 988.14128344 | 988.14128344 | = | 473.415027 | 988.14128344 | S | 52.0904% | 0.0000% | S |
| 5 | seqsolve1 | 4279 | 4277 | S | 4272 | 4269 | N | 0.1636% | 0.1870% | N |
| 5 | stockholm | 129 | 122 | S | 106 | 104 | N | 17.8295% | 14.7541% | S |
| 5 | supportcase22 | 110 | 110 | = | 1.4 | 6 | S | 98.7273% | 94.5455% | S |
| 5 | neos-3682128-sandon | 34666770 | 34666770 | = | 21672926.2429 | 34666770 | S | 37.4821% | 0.0000% | S |

Full unrounded data, status labels and outcomes are available in the [machine-readable comparison](comparison.csv).

## 5. What the skill changes

### 5.1 Build a structural profile before running the solver

The skill begins with the untouched MPS matrix, recording variable domains, row types, objective structure, sparsity, symmetry, graph/network/decomposition candidates and numerical scale before selecting experiments. This reduces the risk of being misled by variable names, existing formulations or a single solver log.

The 20 instances led to varied methods rather than a parameter sweep: objective-graph component LNS, canonical-slice projection, exact rational LP-dual replay, fundamental-cycle inequalities, fixed-pattern exact recourse, connectivity projection, route quotients, configuration enumeration, combinatorial Benders and DEC master row generation.

### 5.2 Require at least two falsifiable structural hypotheses

Each instance starts with structural explanations followed by small experiments with stopping rules. Failures enter the ledger rather than disappearing. Negative results retain a specific scope, such as a family of fundamental-cycle inequalities failing under the current separator and budget, rather than becoming claims that cuts never help or the instance has no structure.

### 5.3 Separate construction from proof

Primal discovery and global lower-bound proof use different pipelines:

- Construction seeks feasible patterns, repairs, neighborhoods and exact recourse.
- Proof seeks valid relaxations, exact enumeration, DP, master duals or original-model solver bounds.

This allowed `ns1456591` and `neos-3682128-sandon` to progress beyond matching the incumbent to transferable global certificates.

### 5.4 Map results to the original model and verify independently

Structural reduction alone is not a conclusion. The skill requires recording:

1. Why the reduction or projection is equivalent or valid.
2. How reduced solutions lift to original variables.
3. How original-MPS feasibility, objective values and bounds are rechecked.
4. Tolerances, rounding, objective constants and sign conventions.
5. Independent certificate-checking results.

These requirements expose the 6 tolerance-indexed results and prevent slight improvements at one tolerance from being reported as strict new incumbents.

### 5.5 Preserve an auditable decision trail

The skill run retains reading gates, structural profiles, method tables, experiment ledgers, mapping and certificate audits, and next-step recommendations alongside final values. The existence of consistent artifacts strongly supports its workflow role; attributing a particular technique entirely to the skill is a weaker mechanistic inference.

## 6. Representative skill successes

### 6.1 `ns1456591`: from an open gap to exact optimality

Both groups have primal bounds near `988.14128344`. The no-skill dual is `473.415027263`, with gap 52.09%. The skill constructs an exact route quotient, applies Held-Karp/set-partitioning DP and a rational dual of the complete master, and verifies lifting to the original model. Primal and dual then both equal `988.14128344`, with gap 0.

The gain is a proof of global optimality for the apparent best solution, rather than a lower feasible objective.

### 6.2 `neos-3682128-sandon`: complete configuration enumeration

Both groups retain primal bound `34666770`. The no-skill dual is `21672926.2429`. The skill identifies machine configurations, enumerates all relevant configurations, constructs an exact rational master dual and verifies lifting. The resulting dual `34666770` proves global optimality.

Structural research can therefore deliver its entire benefit on the proof side without improving the incumbent.

### 6.3 `ns1856153`: improvement at both ends

The skill run used an exact connectivity projection, transpose/tree equivalence, and cutoff-based big-M tightening to reduce the primal bound from `34.163474399` to `34.016973126`, while increasing the dual bound from the near-zero `0.0033625` to `28.9`. The consistently defined gap fell from 99.99% to 15.04%, one of the clearest improvements at both ends among the 20 instances.

### 6.4 `neos-5221106-oparau`: a strict new solution through projection

Exact mode-4 projection, route exchange and assignment-radius neighborhoods improve the primal from `52.67` to the strictly accepted `52.07`, raise the dual from `0` to `42.54`, and reduce the consistent gap from 100% to 18.30%.

### 6.5 Other strict improvements over public baselines

Using the skill run's frozen public baselines and strict acceptance rules, the 4 improvements are:

- `graphdraw-grafo2`：`68595.5`；
- `r4l4-02-tree-bounds-50`：`499097063`；
- `ns1856153`：`34.01697312588408`；
- `neos-5221106-oparau`：`52.07`。

The no-skill run records 2 contributions under the same definition: `graphdraw-grafo2` and `r4l4-02-tree-bounds-50`. Its separate discussion of the `shipsched` reference improvement does not enter its frozen-public-baseline contribution count. These definitions are kept distinct.

## 7. Where the no-skill run is stronger

The skill run does not maximize general-purpose solver dual progress within limited time. The no-skill run has higher final duals on 12/20 instances and smaller consistent gaps on 11/20, notably:

- `eva1aprime6x6opt`, `cmflsp60-36-2-6`, `sct1` and `shipsched`: the skill finds slightly lower or tolerance-indexed feasible objectives but leaves weaker dual bounds.
- `cdma`: the skill has a lower feasible objective but a much lower saved dual; the gap expands from 27.70% to 61.18%.
- `seqsolve1`: the skill lowers the primal from 4279 to 4277, but the no-skill dual 4272 exceeds the skill dual 4269, leaving the no-skill run with a slightly smaller gap.

This is consistent with the workflow: structural research spends time recovering semantics, proving projections, checking mappings and constructing exact certificates. If these methods do not close the instance, fewer resources may remain for original-model branch-and-bound. The no-skill run often uses MIPFocus, RINS, bound focus, external-pattern repair and general solver strengthening directly, producing stronger computational duals.

The skill should therefore not be viewed as a replacement for solver parameter tuning.

## 8. Structural methods by instance

| Instance | The main structure of the skill route | Focus on results |
|---|---|---|
|  graphdraw-grafo2  | Objective graph number and non-connected fraction limit LNS, original MPS relay | New strict primal bound |
|  polygonpack4-10  | Specifications of projection equivalent snippet links to core local branching | Double is slightly strong; primal bound is the index of tolerance |
|  scpm1  | exact rational LP dual reversal with certainty cost- 1 RWLS | Exactly effective dual evidence |
|  ger50-17-trans-dfn-3t  | Rounding logic cutset reinforced by audit | It's more of a dual gap. |
|  eva1aprime6x6opt  | Material selection topology recovery, fixed mode recourse, clique and symmetry | tolerance index primal bound; not closure |
|  cmflsp60-36-2-6  | Fixed mode exact LP recourse with Y/Z neighborhood | tolerance index primal bound; strict value not improved |
|  r4l4-02-tree-bounds-50  | The five fundamental inequalities of the audit BFS | New strict primal bound |
|  sct1  | Structure fixed external neighborhood, local branching, exact LP dual and original model control | Index of tolerance primal bound |
|  shipsched  | Precedence pattern recourse, scheduling neighborhood, orientation inequality | Index of tolerance primal bound |
|  rocII-8-11  | Public mode repair, time structure restrictions and original model control | numerical stability; not closure |
|  ns1856153  | Exact connected density projection, shift/tree equivalent and cutoff big-M tightening | New strict primal bound, dual significantly improved |
|  dc1l  | exact structure quotient model with a valid certificate chain | Certificate route unfinished closure |
|  neos-5221106-oparau  | exact mode- 4 projection, route, exchange and assignment-radius | New strict primal bound, dual significantly improved |
|  zeil  | Exact `w` projection with support cuts | And the dual gap is stronger. |
|  cdma  | Public mode repair with OR-hull boundary box Lagrangian certificate | Primal bound better, dual weaker |
|  ns1456591  |  Exact route quotient, Held–Karp/set-partitioning DP, rational master dual, and lifting |  exact globally optimal |
|  seqsolve1  | Activation, rounding and Hall reinforcement | Primal bound better, dual slightly weaker |
|  stockholm  | Benders for the exact recourse | Primal bound is better than gap |
|  supportcase22  | DEC main problem generates the exact `1/5` lattice with the quotient model | And the dual gap is stronger. |
|  neos-3682128-sandon  | Complete machine configuration enumeration, exact rational dual and exact enhancement |  exact globally optimal |

The table shows the skill's main value in **method selection and evidence organization**. It maps observed matrix structure to verifiable algorithm families rather than forcing every instance through one algorithm.

## 9. Evidence levels for skill benefits

### Level A: directly auditable facts

- All 20/20 instances have prerequisite skill-reading gates and hash audits.
- CSVs reproduce the 11-win/9-tie primal comparison, 8-versus-12 dual comparison and 9-versus-11 gap comparison.
- Two exact optimality closures and their certificate chains exist.
- Six tolerance-indexed results are explicitly separated from strict incumbents.
- Every instance retains its structural method, experimental results and final status.

### Level B: strong mechanistic explanations

- Closure of `ns1456591` and `neos-3682128-sandon` directly corresponds to route quotients/configuration enumeration, exact duals and lift verification.
- Large improvements for `ns1856153` and `oparau` match the recorded projection and tightening methods.

### Level C: effects that cannot be attributed to the skill alone

- The skill alone is not proven to cause all 11 primal improvements; budgets, machines, randomness, starts and solve order also matter.
- The no-skill group includes problem-specific ideas, so it cannot simply be labeled unstructured.
- These 20 deliberately selected open instances do not represent all MIPLIB or industrial MIPs.

## 10. Proposed next hybrid experiment

A stricter measurement of the skill's incremental value should use a paired, equal-resource protocol:

1. Fix MPS hashes, public-baseline snapshots, solver versions, machines, threads, seeds, absolute/relative tolerances and wall-clock budgets.
2. Give both groups identical original MPS files, incumbents and external information; vary only the skill's structural gate and method generation.
3. Divide each group's equal budget into structure/preprocessing, primal construction and dual/proof stages.
4. After structural work, run the same original-model dual-strengthening task in the skill group as in the control.
5. Preregister strict new-incumbent counts, valid dual improvements, exact closures, original-model replay pass rates and certificate-checking time.
6. Repeat across multiple seeds and retain all unsuccessful approaches.
7. Independently review exact closures and replay new incumbents on the original MPS at strict tolerances.

An immediately actionable workflow for the current results is:

- Retain structural discovery, evidence gates, and tolerance/mapping audits.
- Reserve a separate fixed solver dual budget after each structural experiment.
- Transfer structural cuts, variable fixings, warm starts and projection information to the original-model solver.
- For open instances, report structural certificate bounds and best computational solver bounds separately.

## 11. Reproducibility and source hashes

[`compare_skill_effect.py`](compare_skill_effect.py) parses the saved results and calculates values with `Decimal`. Machine-readable outputs are:

- [`comparison.csv`](comparison.csv): 20 per-instance comparison rows.
- [`audit.json`](audit.json): input/output hashes, design, aggregate counts and pass status.
- [`skill-gate-inventory.csv`](skill-gate-inventory.csv): prerequisite skill-gate artifact paths and hashes for 20 instances.
- [`SOURCE.md`](SOURCE.md): input snapshots, PDF visual checks and recomputation notes.

Main input snapshots:

| Input | Bytes |  SHA-256  |
|---|---:|---|
| No-skill `report.md` |  58,162  |  `528d544ac95193213eeb3cfd6bdf98804f123c34e7fbe417ad7c8e374c185134`  |
| No-skill PDF |  189,424  |  `c8dfe7590ce5723a81bbca1a5aa2ebf9912c033b86a1ad83f8cef5331522d0b9`  |
| skill `summary.csv` | 14,799 | `7b1df6d2b6a9441cf16f2a82d2b7b77e782cb7ab73ea73b72c556718dd7934e7` |
| skill `report_zh.md` | 28,284 | `a1d728d332dd963bcea1cbd24cfe1253f995a6c4d540fb58962d074197ee07dd` |
| `milp-structure-research/SKILL.md` | 4,966 | `f8a09b104f0af3786b2e702f60dde3de7fd54a1aac581dff9bdd8a3325c84b4f` |
| Comparison CSV |  11,838  |  `18f14dc58129789881d26c44b01c5514cb6007d8c52a74c01a07d7fc58a746f2`  |

The 21-page no-skill PDF was rendered and checked page by page. Its title, 20-instance tables, conclusions and appendices agree with the Markdown report, with no observed table truncation or obvious layout omissions.

## 12. Conclusion

The benefits of `milp-structure-research` on these 20 instances are:

1. **More high-quality feasible solutions:** 11 wins and 9 ties under the consistent comparison, with no worse selected primal bounds.
2. **Mathematical certificates beyond computational results:** 2 additional exact global optimality closures, with independent audits of projections, reductions, duals and lifting.
3. **More reliable research records:** explicit separation of strict incumbents, tolerance-indexed points, computational duals, exact duals and negative results.

The limitation is equally clear: general dual progress in these historical runs trails the no-skill run, which has higher duals on 12/20 instances and smaller gaps on 11/20. The skill's role is to **select better-supported structural methods for solvers and turn results into auditable, reproducible and, where possible, provable research conclusions**, rather than replace MIP solvers.

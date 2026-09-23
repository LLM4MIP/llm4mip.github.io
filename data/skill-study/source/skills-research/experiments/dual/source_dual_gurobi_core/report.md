# Controlled dual-bound research on 20 MIPLIB instances

## Shared experiment manifest

- Experiment: `miplib20_dual_skill_20260917T0231CST`
- Experiment root: `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST`
- Start: `2026-09-17T02:31:29+08:00`
- Frozen skill SHA-256: `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535`
- Planned budget: 150 wall minutes per instance, five ordered batches of four with strict barriers
- Baseline: Gurobi 13.0.2, 300 seconds, MIPFocus=3, Seed=20260911
- Per-instance solver limit: 8 threads, 56 GiB SoftMemLimit, NodefileStart=16 GiB, one owned solver
- Shared resource evidence: `resource_manifest.json`; primary execution host: `euler4`

Numerical solver bounds and independently checked exact/certified bounds remain separate throughout. Checkpoints include only evidence accepted by their scheduled boundary; later validation is not backfilled.

## Aggregate outcomes

- Instances with at least one strict numerical improvement: **20 / 20**; total accepted numerical improvements: **109**.
- Instances with at least one strict certified-value improvement: **9 / 20**; total certified-value improvements: **51**.
- First-finite global duals obtained: **0**; external transfers: **0**; evidence-strength upgrades at unchanged value: **5**.

| instance | batch | baseline numeric dual | best numeric dual | best certified dual | gain vs baseline | evidence | status |
|---|---:|---:|---:|---:|---:|---|---|
| graphdraw-grafo2 | 1 | 36194.61842105262 | 53510.5 | 35762.0 | 17315.88157894738 | completed floating-point Gurobi global bound on a replay-validated global strengthening, followed by separately proved exact 0.5 objective-lattice rounding | complete |
| polygonpack4-10 | 1 | -93676718.85471497 | -76521127.37712 | unavailable | 17155591.47759497 | replay-validated numerical global lower bound from a valid conflict relaxation | complete |
| scpm1 | 1 | 414 | 416 | 414 | 2 | numerical complete Gurobi cutoff infeasibility transferred through an independently verified exact reduced-cost cutoff map; exact 414 certificate tracked separately | complete |
| ger50-17-trans-dfn-3t | 1 | 3878.7428649808458 | 3934.3152 | unavailable | 55.57233501915425 | global numerical Gurobi bound on replay-validated strengthening with exact objective-lattice rounding | complete |
| eva1aprime6x6opt | 2 | -205.55395880970968 | -96.70380539695806 | unavailable | 108.85015341275162 | global numerical Gurobi bound on a replay-validated clique-cut strengthening with objective-priority branching | complete |
| cmflsp60-36-2-6 | 2 | 72979501.78444459 | 73054818.85442139 | unavailable | 75317.06997680664 | replay-validated numerical global lower bound on an exact active-period extension | complete |
| r4l4-02-tree-bounds-50 | 2 | 480184507.38540703 | 483755247.8932753 | 476622475 | 3570740.50786829 | numerical Gurobi bound on an independently verified exact-equivalent fixed-tree PESP projection; exact cycle-congruence certificate tracked separately | complete |
| sct1 | 2 | -202.9387684697806 | -199.81870652161473 | unavailable | 3.120061948165869 | global numerical Gurobi bound on an independently replayed optimal-value-preserving strengthening | complete |
| shipsched | 3 | 78053.47380846048 | 85777.6824670317 | 0 | 7724.208658571224 | global numerical Gurobi bound on the untouched original model, kept separate from an exact objective-domain floor | complete |
| rocII-8-11 | 3 | -11.859235629816055 | -11.82 | -12 | 0.039235629816054995 | replay-validated numerical global lower bound over an exhaustive binary split | complete |
| ns1856153 | 3 | 0.0 | 32.6971654879775 | 11.224893917963225 | 32.6971654879775 | numerical Gurobi bound on an independently verified exact-equivalent all-cutset connectivity projection; exact 7936/707 combinatorial certificate tracked separately | complete |
| dc1l | 3 | 1747587.045303841 | 1748926.03079 | unavailable | 1338.9854861591011 | numerical Gurobi bound on replayed Lagrangian relaxation with exact original-objective lattice rounding | complete |
| neos-5221106-oparau | 4 | 0.0 | 24.71937119987213 | 15.11 | 24.71937119987213 | global numerical Gurobi bound on an original-equivalent replayed full formulation, kept separate from an exact assignment-dual/lattice certificate | complete |
| zeil | 4 | 813.8244907898472 | 817.284526478749 | 813.5094878037870948029898319960691 | 3.4600356889018 | replay-validated numerical global lower bound on an equivalent chain-SOS formulation | complete |
| cdma | 4 | -3.648143918896635e+16 | -2.700669263025124e+16 | -6.382890200999861e+16 | 9474746558715112.0 | numerical Gurobi global bound transferred through an independently verified pointwise objective lower estimator on the identical full feasible set; exact LP-Lagrangian certificate tracked separately | complete |
| ns1456591 | 4 | 441.98874800250115 | 988.14128344 | 988.14128344 | 546.152535437499 | exact scaled-integer route-projection dual certificate with matching route partition lifted to the untouched original MPS | complete_exact_optimality_proved |
| seqsolve1 | 5 | 4271.0 | 4275.0 | 3737.0 | 4.0 | numerical_solver_dual_plus_independently_replayed_exact_equivalence_mapping_and_exact_objective_lattice_rounding | complete |
| stockholm | 5 | 103.0 | 106.0 | 87 | 3.0 | replay-validated numerical global lower bound on an untouched/equivalent full model | complete |
| supportcase22 | 5 | 0.4 | 6.4 | 6.0 | 6.0 | global_numerical_solver_cutoff_exclusion_plus_exact_objective_support | complete |
| neos-3682128-sandon | 5 | 20881515.656582348 | 34666770 | 34666770 | 13785254.343417652 | exact rational structural certificate and exhaustive finite-state DP with an independently exact-checked feasible original-MPS solution | complete_exact_optimality_proved |

## Common-budget dual trajectories

| instance | num 30m | num 60m | num 90m | num 120m | num 150m | cert 30m | cert 60m | cert 90m | cert 120m | cert 150m |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| graphdraw-grafo2 | 44871.333333333336 | 52655.0 | 53452.0 | 53510.5 | 53510.5 | 35762.0 | 35762.0 | 35762.0 | 35762.0 | 35762.0 |
| polygonpack4-10 | -93676428.4107312 | -93676026.52340318 | -88223247.44006532 | -76521391.09508 | -76521127.37712 | unavailable | unavailable | unavailable | unavailable | unavailable |
| scpm1 | 414 | 415 | 416 | 416 | 416 | 414 | 414 | 414 | 414 | 414 |
| ger50-17-trans-dfn-3t | 3911.846032419113 | 3924.958 | 3933.477 | 3934.3152 | 3934.3152 | unavailable | unavailable | unavailable | unavailable | unavailable |
| eva1aprime6x6opt | -195.18081665612982 | -142.47495614263013 | -114.26876454206847 | -96.70380539695806 | -96.70380539695806 | unavailable | unavailable | unavailable | unavailable | unavailable |
| cmflsp60-36-2-6 | 72979501.78444459 | 73043985.79665373 | 73043985.79665373 | 73043985.79665373 | 73054818.85442139 | unavailable | unavailable | unavailable | unavailable | unavailable |
| r4l4-02-tree-bounds-50 | 480184507.38540703 | 481698898.35102266 | 483643438.9367033 | 483643438.9367033 | 483755247.8932753 | 475109573 | 476398744 | 476462311 | 476622475 | 476622475 |
| sct1 | -200.5276624960709 | -200.43111239812075 | -200.41816024463472 | -200.33787555306816 | -199.81870652161473 | unavailable | unavailable | unavailable | unavailable | unavailable |
| shipsched | 78053.47380846048 | 78053.47380846048 | 84757.70504936673 | 84757.70504936673 | 85777.6824670317 | unavailable | unavailable | 0 | 0 | 0 |
| rocII-8-11 | -11.84499080864419 | -11.84499080864419 | -11.84499080864419 | -11.83 | -11.82 | -12 | -12 | -12 | -12 | -12 |
| ns1856153 | 26.99999999999997 | 31.16501326209632 | 31.16501326209632 | 32.563224893918 | 32.6971654879775 | unavailable | unavailable | 11.224893917963225 | 11.224893917963225 | 11.224893917963225 |
| dc1l | 1747704.5602424452 | 1748360.97471 | 1748467.3413 | 1748652.63363 | 1748926.03079 | unavailable | unavailable | unavailable | unavailable | unavailable |
| neos-5221106-oparau | 15.119999999998981 | 20.53 | 21.080000000000002 | 24.70749999999953 | 24.71937119987213 | 0.0 | 8.15 | 11.36 | 11.36 | 15.11 |
| zeil | 813.8244907898472 | 815.6280135115437 | 816.8556476879875 | 816.8556476879875 | 817.284526478749 | 0 | 360.1587430181678135272622386970211 | 813.5094878037870948029898319960691 | 813.5094878037870948029898319960691 | 813.5094878037870948029898319960691 |
| cdma | -3.648143918896635e+16 | -2.700669263025124e+16 | -2.700669263025124e+16 | -2.700669263025124e+16 | -2.700669263025124e+16 | unavailable | -63828902009998610 | -63828902009998610 | -63828902009998610 | -63828902009998610 |
| ns1456591 | 605.6295715556794 | 988.14128344 | 988.14128344 | 988.14128344 | 988.14128344 | unavailable | 988.14128344 | 988.14128344 | 988.14128344 | 988.14128344 |
| seqsolve1 | 4271.0 | 4273.0 | 4275.0 | 4275.0 | 4275.0 | 3737.0 | 3737.0 | 3737.0 | 3737.0 | 3737.0 |
| stockholm | 104.0000723700098 | 105.0 | 105.0 | 105.0 | 106.0 | 0 | 82 | 82 | 87 | 87 |
| supportcase22 | 1.0 | 2.0 | 6.4 | 6.4 | 6.4 | unavailable | 1.0 | 5.4 | 6.0 | 6.0 |
| neos-3682128-sandon | 20881520 | 33158530 | 34332695 | 34666770 | 34666770 | unavailable | 33158530 | 34332695 | 34332695 | 34666770 |

## Failed routes and next experiments

| instance | failed or dominated routes | next distinct dual experiment |
|---|---|---|
| graphdraw-grafo2 | translation normalization and coupled-block probes were uninformative; the terminal objective-cut run did not strictly improve after the numerical guard | price a larger disjoint component partition jointly, then add its independently replayed component cuts to the full model before a fresh bound-focused tree |
| polygonpack4-10 | aggressive-presolve canonical arm produced no candidate; rotation-aggregated nine-polygon oracle ended TIME_LIMIT_UNKNOWN | resume rotation-aggregated polygon-set separation from the validated six-polygon master with a longer or stronger geometry/area oracle |
| scpm1 | nested bucket refinements and dominance did not strengthen the bound; cutoff-416 and objective-shell searches stayed incomplete; COPT refused the model under its size-limited license | complete the exact objective-416 shell with PB-SAT/DP or a stronger multirow aggregation and exact exclusion certificate |
| ger50-17-trans-dfn-3t | rejected truncated-row cut model; valid but weak design projection; replay-valid dynamic separator ended below retained bound | design-capacity Benders master with complete max-flow/min-cut feasibility separation |
| eva1aprime6x6opt | compact conflict replacement and all-row indicator exposure were weaker; conflict-degree priority and the final selective implied-cut fallback did not displace the retained tree | solve a complete precedence/assignment projection with symmetry-aware branching and stabilized Lagrangian closure, then lift validated cuts to the full model |
| cmflsp60-36-2-6 | capacity Lagrangian was dominated; aggressive original run was stopped after remaining below baseline; activation-prefix, family-activation, no-heuristic, and short active-period routes did not clear significance | continue the validated active-period extension with period/family cover separation or a longer bound-focused tree |
| r4l4-02-tree-bounds-50 | the cuts3 projected run lagged the base projection; randomized DFS cycle expansion exhausted several GiB without a certificate; early setup attempts failed before optimization | exact Benders or cycle separation over the projected PESP model with stabilized retained-row multipliers |
| sct1 | valid group-OR extension was weaker; no-heuristics and alternate-seed trees lagged at two diagnostic observations | complete precedence/assignment projection with stabilized Lagrangian closure or symmetry-aware branching |
| shipsched | tight-M, triangle, indicator, symmetry-core, no-heuristic, and public-start equal-budget probes were weaker than the retained original-model trees | derive a complete precedence-conflict separation oracle on the 71-ship core and feed its cuts into a persistent full-model bound tree |
| rocII-8-11 | initial Pall run had a configuration failure before optimization; LR-monotonicity, SOS, continuous encodings, and stronger chained order formulation did not improve the accepted cutoff sequence | continue cutoff exclusion below -11.82 using the replay-validated ordered endpoint hull, or add stronger valid order/rectangle cuts |
| ns1856153 | Martin and pair-cost formulations were weaker; the valid global exact row slowed search; one alternate seed was safely stopped after trajectory domination | separate stronger geometry-aware cutsets or use an exact quotient-tree decomposition with multi-cluster matching prices |
| dc1l | integral-slack variant was weaker; stronger retained-side-row aggregation was computationally weaker; public-start aggregation and alternate seed lagged | globally priced decomposition of covering rows with stabilized residual-side multipliers and inherited bound |
| neos-5221106-oparau | the exact tight-M-only probe remained at zero, cheapest-mode aggregation and size-4 SEC routes stayed below the retained demand-flow bound, and exact incoming minima duplicated outgoing minima | add dynamically separated capacity/subtour cuts to a persistent tight-M full-model tree and derive a capacity-aware exact multi-depot assignment dual |
| zeil | continuous-cumulative encoding-3 and explicit-binary-shift probes were globally valid but nonimproving; initial baseline invocation failed configuration before optimization | jointly optimize valid window multipliers and the closure relaxation with separation, then replay the resulting rational certificate |
| cdma | binary and normalized-q projections were weaker; original stabilization hit numerical trouble; strong branching and an alternate long seed lagged; euler4 COPT was blocked by its noncommercial size limit | derive perspective or disjunctive cuts for the paired on/off continuous columns and dense balance equations, then replay them in the numerically stable scaled-objective model |
| ns1456591 | the denser 171-leader orbitope was valid but weaker than the simpler symmetry reduction | not-applicable: exact original-problem global closure was proved |
| seqsolve1 | Heuristics=0 cutoff probe was safely stopped after two matched-time diagnostics showed weaker root separation; Hall 1500s plateaued at the already accepted 4275 after lattice rounding | build an explicit objective-cutoff infeasibility formulation for the next integer target and add mixed h/pairday cover separation before a longer proof run |
| stockholm | BendersStrategy parameter was unavailable; recursive deviation enumeration added no support; strong branching stalled and was safely interrupted | exact resource-constrained separation for fractional cover-master solutions, then combinatorial Benders cuts that couple OD blocks |
| supportcase22 | aggressive original B&C remained weak; cutoff<=10 and cutoff<=6.4 root-cut probes timed out; threshold-6 and 27/5-plus-unit simple propagation stalled; pattern-shell cut and no-cut probes that did not close are retained pending | Use the exact objective-support shell at the next attainable value, fixing one support-count pattern per run or using a second MILP backend; retain the independently replayed exact LB as the lower shell. |
| neos-3682128-sandon | the inherited size-limited license failed before optimization; a misspelled RLT parameter and one malformed parameter JSON failed before model optimization; the 600-second aggressive original-model run was weaker than baseline | not-applicable: exact original-problem global closure was proved |

## Cross-instance lessons

- Exact structural projection was most valuable when the large MPS hid a small complete combinatorial core. For `ns1456591`, a 19-customer route partition admitted exhaustive dynamic programming and an integer master dual, closing the original problem exactly; for other instances, exact aggregations supplied useful certified bounds even when they remained below the best numerical tree bound.
- Reformulation quality had to be measured on the bound trajectory, not inferred from apparent algebraic strength. Dense orbitope constraints, indicator conversions, explicit binary encodings, and retained-side-row variants were sometimes valid yet slower or weaker than a simpler representation.
- Independently proving an objective lattice safely converted terminal floating bounds into stronger discrete bounds on several models. A numerical guard was still necessary near an imposed objective cut so solver epsilon was not promoted to a false lattice step.
- Numerical and exact evidence often advanced at different rates. Keeping two monotone series made it possible to retain a strong numerical global bound while separately improving a weaker rational, combinatorial, or min-cut certificate.
- A productive long tree was usually worth preserving after a useful trajectory appeared. Short diagnostic probes were most useful for rejecting a representation or branching choice; repeated parameter-only restarts did not replace a distinct structural route.
- Every generated cut or projection needed literal source-MPS replay. This caught the invalid first `ger50-17-trans-dfn-3t` cut model, where fixed-format name truncation silently omitted variables, before its contradictory bound could be accepted.
- Public feasible solutions helped as validated starts and conservative cutoffs, but contributed no dual evidence. Their objective values and feasibility tolerances remained separate from official/reference dual fields.
- Exact symmetry was useful when it removed interchangeable blocks cheaply, while denser ordering constraints could overwhelm the gain. The simpler `ns1456591` canonicalization improved the numerical bound; its larger orbitope variant was valid but weaker.
- Dualizing a small set of coupling rows after an exact projection produced strong bounds on covering-style models. Multiplier signs, residual slack penalties, and retained objective terms had to be replayed coefficient by coefficient.
- Scheduled no-backfill checkpoints exposed real timing effects: several candidates were produced before a boundary but accepted only afterward, and stale or delayed writers were corrected without changing the frozen boundary state.
- Backend availability is part of the evidence record. Gurobi 13.0.2 on euler4 was licensed for the declared workloads. COPT 8.0.4 on euler4 fell back to a size-limited noncommercial mode for one probe, while altman passed a 2,501-binary COPT solve test but had only about 1.3 GiB free filesystem space; these host-specific constraints were treated as infrastructure outcomes rather than model results.
- A small forced scheduling prefix can close the last gap left by a much larger dynamic program. For `neos-3682128-sandon`, sequence decomposition, an exact machine/deadline DP, and the forced eight-period machine-4 prefix raised the certified lower bound to the exact feasible objective of 34,666,770.
- Cover certificates are sensitive to their indexing domain. On `stockholm`, two early cross-OD mappings were retracted; restricting replay to valid same-OD paths produced a sound exact bound of 87, while 9,376 replayed cover rows raised the full-model numerical bound to 106.
- Exact propagation and solver cutoff exclusion complemented one another on `supportcase22`: exact enumeration certified 6, while an original-model numerical cutoff proof reached 6.4. Neither evidence class was promoted into the other.
- On `seqsolve1`, max-flow/min-cut supplied a portable exact certificate at 3,737, while capacity-column generation and exhaustive Hall/cutoff checks supported the stronger numerical bound 4,275. This again justified reporting separate numerical and certified series.

## Timing, resources, deviations, and limitations

| instance | wall min | active min | solver-process min | worker seconds | protocol deviation | limitation |
|---|---:|---:|---:|---:|---|---|
| graphdraw-grafo2 | 150.28562228333334 | 150.0 | 115.65391789674759 | 9000 | Transient SSH/DNS reconnect failures occurred between runs; no solver overlap, lost process, or acceptance-policy change resulted. | 53510.5 depends on floating-point tree evidence before exact lattice rounding and is not an independent exact tree certificate; the independent rational original-row bound is 35762; interrupted-process time includes a 145-second logged lower bound |
| polygonpack4-10 | 150.3402737736702 | unknown | 102.83647667816064 | unknown | baseline began at wall second 338.095431 after mandatory audit/transfer; one unproductive aggressive-presolve arm was cleanly stopped; no evidence from unknown-status work was accepted | final bound is numerical; infeasibility cuts and zero-gap master solution have no rational proof log |
| scpm1 | 150.0 | 150.0 | 95.376609090964 | 9000 | baseline launch followed the mandatory skill/policy audit and began 328.2 seconds after timer start; the 150-minute file write was 14.942 seconds late but filtered evidence at the scheduled boundary with no backfill | best 416 depends on numerical Gurobi global infeasibility after exact map validation; independently replayable exact evidence reaches 414 |
| ger50-17-trans-dfn-3t | 150.0 | 150.0 | 108.19973940054575 | 9000 | not-applicable | best result remains a numerical solver-tree bound; no independent rational or exhaustive tree certificate |
| eva1aprime6x6opt | 152.02549036741257 | 150.0 | 114.50176267623901 | 9000 | Two initial baseline launches and one parameter command exited before model load; 30m and 120m process snapshots required explicit metadata corrections; the 30m writer was 0.000563 seconds early with unchanged accepted state; automatic review rejected a redundant recursive local-to-remote audit-tree upload. | the best result remains a floating-point global solver bound; no exact lattice or independent rational branch-tree certificate was obtained |
| cmflsp60-36-2-6 | 150.87822070916494 | unknown | 109.43054269949594 | unknown | remote instance initially lacked the MPS and it was staged from the untouched generic collection after timer/audit; one nonaccepted capacity-Lagrangian counter discrepancy was disclosed; one dominated aggressive run was cleanly interrupted | final bound is numerical; no exact or rational certified lower bound was produced |
| r4l4-02-tree-bounds-50 | 150.0 | 150.0 | 115.17657592693965 | 9000 | several setup/SSH attempts failed before solver creation; the 150-minute checkpoint write was 16.905 seconds late, and scheduled-epoch validation confirmed no post-boundary acceptance or backfill | best numerical value is not an exact branch certificate; strongest independently certified cycle bound remains below the reproducible numerical baseline |
| sct1 | 150.0 | 150.0 | 128.05534990231197 | 9000 | not-applicable | best result remains a floating-point global solver bound; no rational or exhaustive tree certificate |
| shipsched | 150.75474148333333 | 150.0 | 107.5088515718778 | 9000 | The 90-minute writer emitted a stale in-memory snapshot; raw output was preserved and the checkpoint was reconstructed solely from immutable pre-boundary evidence with no backfill. | the best numerical result is a floating-point Gurobi tree bound; the independent exact certificate proves only objective nonnegativity (0); the public feasible vector was numerical primal information only |
| rocII-8-11 | 150.21162883838016 | unknown | 106.33931172291437 | unknown | an initial broad shared-root filename search exposed paths/snippets from other instances; no unintended information was used; one configuration failure occurred before optimization | best numerical lower bound is not exact; the separate exact -12 certificate is weaker than the numerical best |
| ns1856153 | 150.0 | 150.0 | 120.19835461775462 | 9000 | failed local-build/SSH/optional-parameter attempts occurred before solver creation; two dominated runs were safely interrupted and preserved; final sync retried after a transient hostname-resolution failure | best 32.6971654879775 is numerical; independently replayable exact combinatorial evidence reaches 7936/707 |
| dc1l | 150.0 | 150.0 | 110.37608304818471 | 9000 | 90-minute checkpoint file was written about 88 seconds late and conservatively excluded a post-boundary acceptance; no backfill | best result remains numerical; exact lattice arithmetic does not certify the branch-and-bound lower bound itself |
| neos-5221106-oparau | 151.07514469999998 | 150.0 | 105.11386916240056 | 9000 | Transient SSH hostname-resolution failures occurred between successful checks; no solver overlap, lost process, checkpoint backfill, or acceptance-policy change resulted. | the strongest numerical result is a floating-point Gurobi global tree bound without an exact tree certificate; the independent exact assignment/lattice certificate is weaker |
| zeil | 151.56951119105022 | unknown | 111.27695556879044 | unknown | one baseline configuration attempt failed before optimization; one broad search exposed only a prior path name without content use; automatic approval review rejected an optional local-to-remote v2 mirror | strongest bound remains numerical; the separately exact closure certificate is weaker; an optional local-to-remote mirror was rejected while the complete canonical local bundle was preserved |
| cdma | 150.0 | 150.0 | 114.63007170756659 | 9000 | one parameter-interface launch failed before optimization; original stabilization was safely interrupted for numerical trouble; COPT lacked a full-size license; all checkpoint evidence remained boundary-filtered with no backfill | the strongest bound is numerical; the independently replayable exact LP-Lagrangian certificate is materially weaker |
| ns1456591 | 150.0 | 56.296136505 | 15.004490438954035 | unknown | not-applicable | none for the final value; the earlier Gurobi bounds remain numerical, while the closing certificate is exact |
| seqsolve1 | 151.08033259312313 | 150.0 | 115.44477837085724 | unknown | Initial start_instance.py invocation omitted required --root and exited before timer creation; corrected immediately with no intervening target-specific access. | The best numerical bound relies on floating-point Gurobi branch-and-cut. Exact replay validates transformations and unit-lattice rounding but is not an exact tree certificate. The separate exact max-flow/min-cut certificate is weaker. |
| stockholm | 151.68754551410674 | unknown | 87.61315001646678 | unknown | The first start_instance.py call omitted required --root and exited during argument parsing; it was corrected before target inspection. The fixed baseline began 250.406 seconds after the timer while the mandatory skill audit and transfer completed. Two early cross-OD certificate mappings were retracted and checkpoints corrected; no retracted evidence contributes to any final value. The uninformative strong-branch run was safely interrupted after 451.335 solver seconds. | strongest numerical bound 106 exceeds the exact certified bound 87; the rational certificate covers the replayed path-cover relaxation rather than the full original matrix; no official transferable dual was available |
| supportcase22 | 151.9410255630811 | 150.0 | 86.51552956501642 | 9000 | Initial start_instance invocation omitted --root and failed before target inspection; the successful timer record was then created before target access. The 90-minute artifact write was 25.37 seconds late after the legacy comparator rejected exact fraction 27/5; eligibility still used accepted_epoch <= the predeclared barrier, so no backfill occurred. | The exact certificate reaches the separately reported certified bound; any stronger accepted numerical cutoff remains solver-numerical and has no exact proof artifact. |
| neos-3682128-sandon | 150.0 | 141.77440018653868 | 17.130982379118603 | unknown | not-applicable | none for the final value; intermediate Gurobi bounds are numerical, while the closing lower bound and matching feasible objective were checked exactly |

## Per-instance records

### graphdraw-grafo2

The frozen reproducible numerical dual was **36194.61842105262** and the final best numerical dual was **53510.5**. The best certified dual was **35762.0**. The strongest accepted value, **53510.5**, has evidence type `completed floating-point Gurobi global bound on a replay-validated global strengthening, followed by separately proved exact 0.5 objective-lattice rounding`.

Methods: edge-disjoint star projections; exact per-component 61Z lattices; complete component-support accounting; globally valid component cuts in the full model; bound-focused branch-and-cut

Result provenance: new skill-arm structural derivation and solver evidence; public values were used only as primal context. Validation grade: `A-numerical-scope-checked-plus-certified-floor`. Stopping reason: predeclared 150-minute hard deadline reached with final evidence checkpointed and zero owned solver processes

Evidence index: `instances/graphdraw-grafo2/accepted_bounds/0008_full_strengthened_v1.json`. Detailed report: `instances/graphdraw-grafo2/final_report.md`.

### polygonpack4-10

The frozen reproducible numerical dual was **-93676718.85471497** and the final best numerical dual was **-76521127.37712**. The best certified dual was **unavailable**. The strongest accepted value, **-76521127.37712**, has evidence type `replay-validated numerical global lower bound from a valid conflict relaxation`.

Methods: canonical one-hot slices; exhaustive triple conflicts; validated four-, five-, and six-polygon conflict-master separation

Result provenance: derived from the hashed untouched MPS; immutable numerical acceptance records and independent source/map/master replay; no public dual transfer. Validation grade: `replay-validated numerical`. Stopping reason: wall_budget_exhausted

Evidence index: `instances/polygonpack4-10/accepted_bounds/bound_009_six_separation_stage1.json`. Detailed report: `instances/polygonpack4-10/final_report.md`.

### scpm1

The frozen reproducible numerical dual was **414** and the final best numerical dual was **416**. The best certified dual was **414**. The strongest accepted value, **416**, has evidence type `numerical complete Gurobi cutoff infeasibility transferred through an independently verified exact reduced-cost cutoff map; exact 414 certificate tracked separately`.

Methods: exact nonnegative row aggregation and integer DP; exact rational LP-dual reduced-cost filtering; verified cutoff equivalence; complete bound-focused cutoff infeasibility

Result provenance: new structural derivation and solver proof; no external dual transfer. Validation grade: `A-numerical-scope-checked with separate exact certificate`. Stopping reason: predeclared 150-minute hard deadline reached with zero owned solver processes

Evidence index: `instances/scpm1/accepted_bounds/0004_cutoff_refutation_lb416.json`. Detailed report: `instances/scpm1/final_report.md`.

### ger50-17-trans-dfn-3t

The frozen reproducible numerical dual was **3878.7428649808458** and the final best numerical dual was **3934.3152**. The best certified dual was **unavailable**. The strongest accepted value, **3934.3152**, has evidence type `global numerical Gurobi bound on replay-validated strengthening with exact objective-lattice rounding`.

Methods: rounded multicommodity balance/capacity cuts; full-model branch-and-cut; exact 1/5000 objective lattice; public feasible cutoff after validation

Result provenance: new skill-arm derivation and numerical reproduction; public feasible solution used only as validated primal cutoff input. Validation grade: `A-numerical-scope-checked`. Stopping reason: predeclared 150-minute hard cap reached with zero owned solver processes

Evidence index: `instances/ger50-17-trans-dfn-3t/accepted_bounds/accepted_015_public_cutoff_terminal_lattice_3934_3152.json`. Detailed report: `instances/ger50-17-trans-dfn-3t/final_report.md`.

### eva1aprime6x6opt

The frozen reproducible numerical dual was **-205.55395880970968** and the final best numerical dual was **-96.70380539695806**. The best certified dual was **unavailable**. The strongest accepted value, **-96.70380539695806**, has evidence type `global numerical Gurobi bound on a replay-validated clique-cut strengthening with objective-priority branching`.

Methods: exact binary-alias extraction; integral set-packing conflict graph; 6676 maximal-clique cuts; generic-cut suppression; objective-support priority branching; targeted indicator diagnostics

Result provenance: new skill-arm conflict/clique derivation and numerical solver result; official values remained primal context only. Validation grade: `A-numerical-scope-checked`. Stopping reason: fixed 150-minute wall budget completed with zero owned solver processes

Evidence index: `instances/eva1aprime6x6opt/accepted_bounds/0006_priority_objective_cuts0_2400s_numeric.json`. Detailed report: `instances/eva1aprime6x6opt/final_report.md`.

### cmflsp60-36-2-6

The frozen reproducible numerical dual was **72979501.78444459** and the final best numerical dual was **73054818.85442139**. The best certified dual was **unavailable**. The strongest accepted value, **73054818.85442139**, has evidence type `replay-validated numerical global lower bound on an exact active-period extension`.

Methods: original-model branch-and-cut; capacity Lagrangian probe; exact activation-prefix, family-activation, and active-period OR extensions

Result provenance: derived from the hashed untouched MPS; immutable solver records and independently replayed exact-extension mapping; no public dual transfer. Validation grade: `replay-validated numerical`. Stopping reason: wall_budget_exhausted

Evidence index: `instances/cmflsp60-36-2-6/accepted_bounds/0003_active_period_extended_1080s_02.json`. Detailed report: `instances/cmflsp60-36-2-6/final_report.md`.

### r4l4-02-tree-bounds-50

The frozen reproducible numerical dual was **480184507.38540703** and the final best numerical dual was **483755247.8932753**. The best certified dual was **476622475**. The strongest accepted value, **483755247.8932753**, has evidence type `numerical Gurobi bound on an independently verified exact-equivalent fixed-tree PESP projection; exact cycle-congruence certificate tracked separately`.

Methods: exact spanning-tree elimination of PESP potentials; bound-focused branch-and-cut on the exact projection; exact edge-disjoint cycle-congruence packing with independent integer replay

Result provenance: new exact-equivalent projection, numerical solver bounds, and newly derived exact cycle certificates; no external dual transfer. Validation grade: `A-numerical-scope-checked with separate exact certificate`. Stopping reason: predeclared 150-minute hard deadline reached with zero owned solver processes

Evidence index: `instances/r4l4-02-tree-bounds-50/accepted_bounds/0025_tree_projected_v1_3000_483755247_8932753.json`. Detailed report: `instances/r4l4-02-tree-bounds-50/final_report.md`.

### sct1

The frozen reproducible numerical dual was **-202.9387684697806** and the final best numerical dual was **-199.81870652161473**. The best certified dual was **unavailable**. The strongest accepted value, **-199.81870652161473**, has evidence type `global numerical Gurobi bound on an independently replayed optimal-value-preserving strengthening`.

Methods: exact activation-integrality strengthening for 818 variables; full-model branch-and-cut; validated public start/cutoff; group-OR diagnostic

Result provenance: new skill-arm strengthening and numerical solver result; public feasible solution used only as validated primal cutoff input. Validation grade: `A-numerical-scope-checked`. Stopping reason: predeclared 150-minute wall cap reached after final validation with zero owned solver processes

Evidence index: `instances/sct1/accepted_bounds/accepted_018_activation_integrality_v1_seed13_terminal_-199_81870652161473.json`. Detailed report: `instances/sct1/final_report.md`.

### shipsched

The frozen reproducible numerical dual was **78053.47380846048** and the final best numerical dual was **85777.6824670317**. The best certified dual was **0**. The strongest accepted value, **85777.6824670317**, has evidence type `global numerical Gurobi bound on the untouched original model, kept separate from an exact objective-domain floor`.

Methods: exact event-chain tight-M reformulation; triangle and fixing cuts; indicator representation; exact zero-offset core projection; measured full-model branch-and-cut fallback; validated public cutoff/start diagnostic

Result provenance: new skill-arm structural diagnostics and original-model numerical search; public solution used only as a validated primal start/cutoff. Validation grade: `A-numerical-scope-checked-plus-certified-floor`. Stopping reason: predeclared 150-minute wall budget exhausted after final validation with zero owned solver processes

Evidence index: `instances/shipsched/accepted_bounds/0004_original_final_2550s_numeric.json`. Detailed report: `instances/shipsched/final_report.md`.

### rocII-8-11

The frozen reproducible numerical dual was **-11.859235629816055** and the final best numerical dual was **-11.82**. The best certified dual was **-12**. The strongest accepted value, **-11.82**, has evidence type `replay-validated numerical global lower bound over an exhaustive binary split`.

Methods: exact objective-cardinality certificate; exhaustive P#0#10 split; ordered confidence-endpoint hull; successive cutoff exclusion

Result provenance: derived from the hashed untouched MPS; exact combinatorial certificate plus immutable exhaustive-split solver/cutoff records and mapping replay; no public dual transfer. Validation grade: `replay-validated numerical plus exact combinatorial certificate`. Stopping reason: wall_budget_exhausted

Evidence index: `instances/rocII-8-11/accepted_bounds/0006_pall_orderhull_cutoff_m1182_numeric.json`. Detailed report: `instances/rocII-8-11/final_report.md`.

### ns1856153

The frozen reproducible numerical dual was **0.0** and the final best numerical dual was **32.6971654879775**. The best certified dual was **11.224893917963225**. The strongest accepted value, **32.6971654879775**, has evidence type `numerical Gurobi bound on an independently verified exact-equivalent all-cutset connectivity projection; exact 7936/707 combinatorial certificate tracked separately`.

Methods: exact projection from staged Boolean connectivity to undirected cutsets; branch-and-cut on the all-cutset model; exact cluster contraction, spanning-tree enumeration, and matching certificate

Result provenance: new exact-equivalent connectivity formulations, numerical solver bounds, and new exact combinatorial certificates; no external dual transfer. Validation grade: `A-numerical-scope-checked with separate exact certificate`. Stopping reason: predeclared 150-minute hard deadline reached with zero owned solver processes

Evidence index: `instances/ns1856153/accepted_bounds/0008_connectivity_cutset_v2_seed13_2200_32_6971654879775.json`. Detailed report: `instances/ns1856153/final_report.md`.

### dc1l

The frozen reproducible numerical dual was **1747587.045303841** and the final best numerical dual was **1748926.03079**. The best certified dual was **unavailable**. The strongest accepted value, **1748926.03079**, has evidence type `numerical Gurobi bound on replayed Lagrangian relaxation with exact original-objective lattice rounding`.

Methods: exact slack-substitution cover projection; duplicate-column aggregation; sign-valid Lagrangian relaxation; exact 1/100000 objective lattice; validated public cutoff/start

Result provenance: new skill-arm derivation and numerical solver result; public feasible vector used only as independently validated cutoff/start. Validation grade: `A-numerical-scope-checked`. Stopping reason: predeclared 150-minute hard deadline reached with zero owned solver processes

Evidence index: `instances/dc1l/accepted_bounds/0005_lagrangian_cover_v4_seed11_800s_lattice_numeric.json`. Detailed report: `instances/dc1l/final_report.md`.

### neos-5221106-oparau

The frozen reproducible numerical dual was **0.0** and the final best numerical dual was **24.71937119987213**. The best certified dual was **15.11**. The strongest accepted value, **24.71937119987213**, has evidence type `global numerical Gurobi bound on an original-equivalent replayed full formulation, kept separate from an exact assignment-dual/lattice certificate`.

Methods: exact tight-M/service equivalence; route-cost projection; size-2/3/4 subtour cuts; customer-count and demand flows; cheapest-mode aggregation; exact assignment dual; strengthened full-model branch-and-cut

Result provenance: new structural derivations and solver evidence from the untouched MPS; official values were used only as background. Validation grade: `A-numerical-scope-checked-plus-certified-floor`. Stopping reason: predeclared 150-minute wall budget exhausted after final result validation and zero-process audit

Evidence index: `instances/neos-5221106-oparau/accepted_bounds/0012_full_tight_route_v8_1500s_numeric.json`. Detailed report: `instances/neos-5221106-oparau/final_report.md`.

### zeil

The frozen reproducible numerical dual was **813.8244907898472** and the final best numerical dual was **817.284526478749**. The best certified dual was **813.5094878037870948029898319960691**. The strongest accepted value, **817.284526478749**, has evidence type `replay-validated numerical global lower bound on an equivalent chain-SOS formulation`.

Methods: cumulative-chain SOS equivalence; continuous and explicit-binary representation probes; exact LP-dual certificates; exact weighted-window closure/min-cut relaxation; bound-focused branch-and-cut

Result provenance: derived from the hashed untouched MPS; immutable solver records, full original-to-derived replay, exact rational aggregation, and integer min-cut replay; no public dual transfer. Validation grade: `replay-validated numerical plus exact rational/combinatorial certificate`. Stopping reason: wall_budget_exhausted

Evidence index: `instances/zeil/accepted_bounds/0009_chain_sos_aggr_2400s_numeric.json`. Detailed report: `instances/zeil/final_report.md`.

### cdma

The frozen reproducible numerical dual was **-3.648143918896635e+16** and the final best numerical dual was **-2.700669263025124e+16**. The best certified dual was **-6.382890200999861e+16**. The strongest accepted value, **-2.700669263025124e+16**, has evidence type `numerical Gurobi global bound transferred through an independently verified pointwise objective lower estimator on the identical full feasible set; exact LP-Lagrangian certificate tracked separately`.

Methods: full original-model baseline; binary and normalized continuous projections; full-feasible-set conservative objective scaling; bound-focused Gurobi trees; exact rational LP-Lagrangian certificate

Result provenance: new verified relaxation and solver bound with a separately derived exact rational certificate; no external dual transfer. Validation grade: `A-numerical-scope-checked with separate exact certificate`. Stopping reason: predeclared 150-minute hard deadline reached with zero owned solver processes

Evidence index: `instances/cdma/accepted_bounds/0002_objective_scaled_v3_900.json`. Detailed report: `instances/cdma/final_report.md`.

### ns1456591

The frozen reproducible numerical dual was **441.98874800250115** and the final best numerical dual was **988.14128344**. The best certified dual was **988.14128344**. The strongest accepted value, **988.14128344**, has evidence type `exact scaled-integer route-projection dual certificate with matching route partition lifted to the untouched original MPS`.

Methods: exact 20-layer symmetry canonicalization; metric route projection; exact reverse/forward Held-Karp route enumeration; exact set-partition DP; integer route-master dual; exact lift to untouched MPS

Result provenance: new skill-arm structural derivation independently replayed on Windows and euler4; public MIPLIB primal values were not used in the proof. Validation grade: `A-exact-original-closure`. Stopping reason: accepted exact global lower bound matched an exactly checked feasible objective on the untouched original MPS

Evidence index: `instances/ns1456591/accepted_bounds/0003_route_master_exact.json`. Detailed report: `instances/ns1456591/final_report.md`.

### seqsolve1

The frozen reproducible numerical dual was **4271.0** and the final best numerical dual was **4275.0**. The best certified dual was **3737.0**. The strongest accepted value, **4275.0**, has evidence type `numerical_solver_dual_plus_independently_replayed_exact_equivalence_mapping_and_exact_objective_lattice_rounding`.

Methods: fixed original baseline; exact capacity max-flow/min-cut relaxation; person-z packing; odd-capacity pairday CG and tight-M; person/site day-subset Hall packing; integer-target cutoff exclusion

Result provenance: new target-specific computation from the immutable original MPS; no external dual-bound transfer. Validation grade: `mixed: replay-validated numerical best plus independent exact max-flow/min-cut certificate`. Stopping reason: 150-minute hard wall-clock deadline

Evidence index: `accepted_bounds/accepted_0004_local_capacity_cg_numeric.json; accepted_bounds/accepted_0002_maxflow_exact.json; bound_validation.json; final_report.md`. Detailed report: `instances/seqsolve1/final_report.md`.

### stockholm

The frozen reproducible numerical dual was **103.0** and the final best numerical dual was **106.0**. The best certified dual was **87**. The strongest accepted value, **106.0**, has evidence type `replay-validated numerical global lower bound on an untouched/equivalent full model`.

Methods: original-model cut-focused branch-and-cut; exact same-OD path-cover replay; disjoint packing; iterative integer/fractional cover separation; exact rational cover-LP dual weighting; equivalent full-model strengthening

Result provenance: derived from the hashed untouched MPS; immutable numerical records, exact original-row cover replay, exact rational LP-dual certificate, and equivalent-model replay; no public dual transfer. Validation grade: `replay-validated numerical plus exact rational certificate`. Stopping reason: wall_budget_exhausted

Evidence index: `instances/stockholm/accepted_bounds/numeric_004_cover9376_final.json`. Detailed report: `instances/stockholm/final_report.md`.

### supportcase22

The frozen reproducible numerical dual was **0.4** and the final best numerical dual was **6.4**. The best certified dual was **6.0**. The strongest accepted value, **6.4**, has evidence type `global_numerical_solver_cutoff_exclusion_plus_exact_objective_support`.

Methods: fixed original baseline; objective-support lattice lifting; complete objective cutoffs; exact interval propagation with equality substitution; exhaustive 140-way 27/5-cost branch certificate; exact objective-support pattern shells

Result provenance: new computation on untouched hashed MPS; no external dual transferred. Validation grade: `independently replayed exact certificate plus separately labeled Gurobi numerical cutoff evidence`. Stopping reason: predeclared 150-minute hard cap

Evidence index: `instances/supportcase22/final_report.md`. Detailed report: `instances/supportcase22/final_report.md`.

### neos-3682128-sandon

The frozen reproducible numerical dual was **20881515.656582348** and the final best numerical dual was **34666770**. The best certified dual was **34666770**. The strongest accepted value, **34666770**, has evidence type `exact rational structural certificate and exhaustive finite-state DP with an independently exact-checked feasible original-MPS solution`.

Methods: objective-lattice rounding; exact setup and assignment relaxations; deadline/machine finite-state DP; sequence decomposition; forced machine-4 prefix; fixed-sequence aggregate start cuts

Result provenance: new skill-arm structural derivation replayed independently on Windows and euler4; no public dual transfer. Validation grade: `A-exact-original-closure`. Stopping reason: accepted exact global lower bound matched an exactly checked feasible objective on the untouched original MPS

Evidence index: `instances/neos-3682128-sandon/accepted_bounds/0012_exact_optimality_dominant_forced_machine4_prefix.json`. Detailed report: `instances/neos-3682128-sandon/final_report.md`.

## Skill-use audit

Coordinator `/root` read `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` and `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` at SHA-256 `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535`. Evidence: `skill_freeze_manifest.json`.

| instance | worker | original entrypoint | frozen entrypoint | SHA-256 | supporting resources | audit |
|---|---|---|---|---|---|---|
| graphdraw-grafo2 | `/root/b1_graphdraw` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| polygonpack4-10 | `/root/b1_polygon` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| scpm1 | `/root/b1_scpm1` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| ger50-17-trans-dfn-3t | `/root` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| eva1aprime6x6opt | `/root/b1_graphdraw` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| cmflsp60-36-2-6 | `/root/b1_polygon` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| r4l4-02-tree-bounds-50 | `/root/b1_scpm1` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); C:\Users\user\.codex\skills\mip-dual-improve\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`) | pass |
| sct1 | `/root` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| shipsched | `/root/b1_graphdraw` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| rocII-8-11 | `/root/b1_polygon` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| ns1856153 | `/root/b1_scpm1` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); C:\Users\user\.codex\skills\mip-dual-improve\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`) | pass |
| dc1l | `/root` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`) | pass |
| neos-5221106-oparau | `/root/b1_graphdraw` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| zeil | `/root/b1_polygon` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| cdma | `/root/b1_scpm1` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | C:\Users\user\.codex\skills\mip-dual-improve\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); C:\Users\user\.codex\skills\mip-dual-improve\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); C:\Users\user\.codex\skills\mip-dual-improve\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`) | pass |
| ns1456591 | `/root` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| seqsolve1 | `/root/b1_graphdraw` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |
| stockholm | `/root/b1_polygon` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | none recorded | pass |
| supportcase22 | `/root/b1_scpm1` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\linear-certificate.md (`7a4c15d76fd536497094ea8bf98cf24ebcf83fd65dc92c56c98db383e0ad8632`) | pass |
| neos-3682128-sandon | `/root` | `C:\Users\user\.codex\skills\mip-dual-improve\SKILL.md` | `D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\SKILL.md` | `61cc3bbe39f9b690ff6b0115cc7bb02475b786e6732af7de727b5b5280d16535` | D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\bound-validity.md (`3f930445ea8044143ed6d7aebe613c85aa92abe412e9e186e864f4bc62048a7c`); D:\sufe\AI4MIP\miplib20_dual_skill_20260917T0231CST\frozen_skill\references\dual-playbook.md (`455c925a432ed9ae6cd5ee9f9cc199e293ba845db768f00511cd94cd3afe9d3b`) | pass |

Target-specific `casebook.md`, `corpus-index.json`, and `case_lookup.py` content was excluded from instance work; the frozen package manifest retains their hashes without treating them as read resources.

## Scope and limitations

This is one controlled skill arm. It does not establish a causal speedup and does not imply that the skill guarantees improvement. Numerical bounds remain dependent on the saved solver logs, parameter records, model hashes, and mapping checks; only explicitly labeled exact/combinatorial certificates are independent of floating-point branch-and-bound tolerances. Public primal values were kept separate from dual evidence unless a recorded, validated cutoff use is stated in the instance artifacts.

# Primal Search Playbook

The following rules turn lessons from the casebook into executable decisions. Tune all parameters through pilots on the current instance. MIP, CP, and custom algorithms are backends for different structures, not a quality ranking.

By default, allocate the research budget only to obtaining better verified primal solutions; dual-bound improvement may be omitted entirely. Use LP solutions, pricing, or cuts only when they directly support construction, neighborhood selection, or repair. Do not pursue a stronger lower bound as a separate objective or substitute gap reduction for feasible-solution improvement. Bounds or local closure that arise from subproblems may be recorded, but do not extend a run merely to obtain them. Expand the task to dual bounds or optimality proofs only when the user requests that work separately.

Use a continuous outer search loop: `candidate generation → original-model validation → update best and solution pool → update center/cutoff/operators → next iteration`. A first feasible solution or first improvement triggers saving and an interim report; continue while the total budget remains. When one iteration stagnates, change the neighborhood, construction, representation, or recombination seed rather than treating the end of that iteration as completion of the task. If no total budget is specified, proceed in bounded batches and ask for a budget; do not silently adopt the illustrative 30-minute budget as the overall stopping condition.

## 1. Cheapest Effective Seed: Transfer Plus Target-Model Completion

Search in this order: existing repository solutions, all official revisions, sibling formulations, and benchmarks from the original application. Compare data, costs, constraints, variable domains, and label symmetries; do not compare only names or objective values. When the correspondence is only suggestive, it may still define a candidate design, but label it as a heuristic transfer and validate it on the target model rather than claiming equivalence.

- **Complete mapping:** When every original variable can be determined, lift the vector directly and check it. The additional upper bounds in `bley` must also be checked.
- **Core mapping:** Transfer only the physical design or categories, then re-solve the target model's remaining discrete operations and continuous recourse. The design and operation variables in `dws` must not be mistaken for one variable group.
- **External data:** For CVRP, first reconcile customers, distance rounding, demands, capacity, and fleet-size semantics. Given routes can provide an upper bound whenever they lift to a feasible original-model solution; obtaining that upper bound does not require first proving that every original solution projects into the external model.
- **Symmetric labels:** For `nj`, relabel the same partition to satisfy the target formulation, then regenerate roots and flows. Do not arbitrarily add every possible root-ordering constraint.

A strong external solution may help the user obtain a better primal quickly, but its provenance must not be labeled as an original GPT construction.

## 2. No Incumbent: Decompose Feasibility into Constructible Invariants

First preserve the hard conditions that are easiest to enforce exactly: one-of-k choice, capacity, connectivity, precedence, or boundaries. Use the remaining violation as an auxiliary search score; the original objective must never offset a hard-constraint violation.

1. Obtain a core state from an LP solution, greedy construction, historical near-feasible solution, or domain construction.
2. Identify the difficult block instead of always fixing the LP argmax. The 24-task block in `ns1905797` repeatedly timed out; rebalancing the assignment unlocked the construction.
3. Fix the master assignment and solve local routing, scheduling, or flow problems. Store the same master-assignment hash with every block to prevent splicing results from different assignments.
4. Merge all blocks and validate the coupling rows. As soon as the first complete feasible vector is available, run a bounded warm-start improvement phase.

When no domain structure is available, try feasibility pump, diving, or RENS. RENS does not require an incumbent: fix variables that are integral in the LP solution and tighten the remaining integer variables to adjacent integers. Failure of this subproblem does not prove that the original problem is infeasible. If too many incorrect fixings were made, reduce the fixing rate or change the rounding rule instead of blindly extending the time limit. [Official SCIP RENS documentation](https://scipopt.org/doc-9.2.4/html/heur__rens_8h.php)

## 3. Eliminate Auxiliary Variables While Preserving a Feasibility Bridge

Identify the real state `y`, such as selections, routes, configurations, orders, or mining periods, and build `lift(y)` or a completion oracle. Even zero-objective auxiliary variables may couple multiple decisions and must not be deleted without validation.

For a primal result, the sufficient statement is: **the particular core candidate found can be completed into a feasible solution of the original model**. A stronger coverage proof is necessary only when claiming equivalence or deriving a global conclusion from infeasibility of the reduced model. This distinction preserves the validity of the upper bound without paying for an unnecessary global proof merely to construct one candidate.

- **Scheduling:** Select jobs, start times, and orders; use CP or matching to generate a schedule, then fill the pair variables. A release-suffix master may be only a relaxation, so master feasibility does not imply schedule feasibility.
- **Layout:** Use a sequence pair, discrete coordinates with `NoOverlap`, or orientations in place of independent pair bits. Check rotations, boundaries, obstacles, and every original non-overlap condition.
- **Network:** Search over component balance/parity, paths, or trees; use a spanning forest or flow completion to recover the original variables.
- **Configuration:** Allow new configurations and capacities instead of searching only an existing finite column pool. Infeasibility of the pool means only that the current pool is insufficient.
- **Type counts:** Check complete column coefficients, costs, and every side row; use deterministic integer allocation to lift multiplicities. Similar names are insufficient evidence.

When continuous variables form only a system of difference constraints, look for a provably valid integer scaling. This worked for `liu` and `ns1905797`; a finite number of decimal places does not justify arbitrarily discretizing a general continuous model.

## 4. Feasible-Solution-Centered Structured LNS

Let `I` be the set of core integer variables and let `xbar` be the center. Choose a semantically related release set `F` with `F⊆I`, fix `I\F`, and retain the original domains and constraints for all other variables. Usually release every continuous variable, or release only the affected recourse variables when local separability has been proved.

Computable signals for choosing `F` include:

- resource contention near tight constraints: variables in the support of tight rows and their precedence or connectivity neighbors;
- positions where the LP and incumbent disagree, or where two strong solutions differ;
- high-cost real operational decisions, together with the zero-cost feasibility auxiliaries they require;
- geometric boundaries, critical paths, adjacent periods, or vehicles and machines that share demand;
- structures involved in successful past moves, while retaining exploration of other structures.

Do not treat "fix 90% of the variables" as a universal rule. Releasing one complete related block is usually more meaningful than releasing the same number of random variables; whether it is faster still requires measurement.

**RINS:** Fix integer variables for which the incumbent and LP solution agree within the recorded tolerance, and release the differing variables. This requires both an LP solution and an incumbent. **Crossover:** Fix the parts on which several strong solutions agree and recombine their differences. Both methods should avoid freezing highly coupled auxiliary encodings into an accidental obstruction. [SCIP primal heuristics](https://www.scipopt.org/download/slides/SCIP-primalHeuristics.pdf)

For a binary core, local branching may use

`sum_{i:xbar_i=0} x_i + sum_{i:xbar_i=1}(1-x_i) <= k`.

Do not apply this binary expression directly to general integer variables. Use an exact encoding of `d_i = [x_i != xbar_i]` to count category changes, or use an explicitly defined L1 distance. Moving from one option to another in a one-hot encoding changes two bits; reports must record both semantic moves and bit changes.

Save original domains on every iteration and restore them correctly before the next iteration. Do not accumulate a previous iteration's fixings, cutoff, or no-good constraints and still call the result the same neighborhood. Re-evaluate a candidate's continuous recourse and all coupling rows. For large models, use incremental updates for valid neighborhoods and cache affected rows and coefficients; independent acceptance still covers the entire untouched original model.

## 5. Change Routes After Stagnation

Maintain two objects: a monotonically improving `best_verified` and an exploratory `current` that may worsen.

| Pilot Observation | Next Action |
|---|---|
| A small neighborhood quickly completes with no improvement | Increase the semantic radius and combine related blocks; remember the scope excluded around this center |
| A large neighborhood repeatedly times out without a feasible candidate | Provide a stronger construction hint, preserve quotas or connectivity, reduce the release set, or switch to a compact representation |
| Many candidates are feasible but their objectives do not change | Deduplicate supports, increase discrete diversity, and try a kick, tabu search, or recombination |
| Recourse is infeasible for many different integer patterns | Use conflicts and tight rows to identify the shared obstruction and release the related variables jointly |
| Only tiny floating-point improvements appear | First normalize integer variables, repair recourse, and audit the original rows; if the improvement disappears, archive the numerical cause |
| The same structure already has an exact local-closure record | Skip only the search covered under the same center, fixed conditions, and objective threshold |

For `nj`, allow a feasible but worse compound kick followed by local descent; keep `best` unchanged until a better solution is found. If the implementation permits an infeasible `current`, store it in a separate near-feasible pool. Only a complete point with zero hard-constraint violations may become the incumbent.

For adaptive operator allocation, first give each operator a small number of comparable pilots, then update weights by verified gain per unit time while retaining an exploration share. A small gain is not necessarily ineffective, as `rmine15` shows, and a large apparent change is not necessarily valid because it may be a tolerance artifact. Do not use 22/112 as an operator hit probability. [SCIP ALNS operator-combination implementation](https://www.scipopt.org/doc/html/heur__alns_8c_source.php)

## 6. Work with General-Purpose Solvers

Retain one bounded strong baseline. If the user explicitly names a backend, first determine whether it is a hard requirement or a preference. If a hard requirement is unavailable, stop the affected solve and report the issue; do not fall back on your own. If a preferred backend is unavailable, record the reason and continue. Only when the user has not specified a backend should the following default order apply:

1. **Probe COPT first.** Check the API or CLI, version, license, model ingestion, current constraint types, MIP-start interface, and resource limits. Confirm with the current model or a semantically equivalent small test that solving can actually begin. By default, assign the first general-purpose MILP baseline, MILP neighborhoods, and LP/MILP recourse to COPT. COPT provides capabilities including `MipStartMode`, `HeurLevel`, `PreRootHeurLevel`, `DivingHeurLevel`, `SubMipHeurLevel`, and `MipRepair`; preserve an automatic-parameter baseline before tuning with short pilots. Because `MipRepair` may extend the solver's internal time limit, enforce an external hard deadline. [COPT parameter documentation](https://guide.coap.online/copt/en-doc/parameter.html)
2. **Fall back actively when COPT is unavailable or incompatible.** For a general linear MILP, probe Gurobi next and record the specific reason COPT failed. Gurobi's `MIPFocus=1` targets rapid discovery of feasible solutions. MIP starts may be supplied as candidates for backend completion or repair. These parameter names are specific to Gurobi. [Gurobi parameter guidelines](https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/guidelines.html) and [MIP starts](https://support.gurobi.com/hc/en-us/articles/360043834831-How-do-I-use-MIP-starts)
3. **Use cuOPT as a conditional primal backend.** Use it only when an NVIDIA GPU and driver and cuOPT are available, the model lies within the currently supported linear-MIP scope, and data conversion and variable ordering have been verified. Its MIP solver remains beta, but GPU primal heuristics fit this skill's candidate-discovery objective; heuristics-only mode and MIP starts may be evaluated. Current documentation describes limitations for some combinations of the MIP-start interface and presolve, so follow the behavior of the installed version. [cuOPT MIP scope](https://docs.nvidia.com/cuopt/user-guide/latest/milp-features.html), [MIP settings](https://docs.nvidia.com/cuopt/user-guide/latest/mip-settings.html), and [MIP start](https://docs.nvidia.com/cuopt/user-guide/latest/cuopt-python/mip/mip-api.html)
4. **Continue to other compatible backends.** SCIP, HiGHS, CBC, CP-SAT, or structure-specific code may handle the remaining routes. The fallback order serves preservation of original-model semantics, timely primal progress, and budget compliance; a solver name does not replace a capability check.

Write one `backend_probe` object for every probed or skipped backend. It must contain at least `backend, probe_command_or_api, executable_or_module, version, license_status, model_features, probe_result, fallback_reason, probe_wall_s`. At the manifest's top level, also record `requested_backend, preferred_backend, backend_selection_order, selected_backend/version`. A backend that is slower in one pilot is not thereby unavailable. Later cross-backend comparisons may use the same start, budget, and validation standard, but cap probing costs so installation attempts, license retries, or solver hopping do not consume the entire research budget.

Set objective, constraint, and integrality tolerances before choosing more primal-focused settings. Finding a better solution does not require forcing every sub-MIP to prove `MIPGap=0`. Apply bounded node or time limits and stop an individual subproblem after it produces a useful improvement, but the outer loop must validate and update the incumbent and then continue searching. A claim that a neighborhood has been completely excluded requires a complete termination record and the corresponding tolerances and evidence.

An adjustable first-pass budget example for 30 minutes is: 3 minutes for ingestion, seeds, and structure; 5 minutes for baseline validation and a short solver baseline; 17 minutes for two or three structural pilots and extension of productive routes; and 5 minutes reserved for lifting and independent acceptance. When reading a large model or running an exact checker is slow, measure that cost before adjusting the allocation. This ratio has not been validated against the 112-instance reference set.

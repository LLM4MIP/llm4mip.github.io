---
name: mip-primal-improve
description: "Continuously improve and validate feasible solutions for hard MILP/MIPLIB instances throughout the available search budget using incumbent transfer, compact construction, recourse repair, and adaptive structural neighborhoods. Use for primal-bound improvement or stalled incumbent search; do not stop at the first improvement. Not for dual-bound-only research or proving optimality."
---

# Find Better, Verifiable MIP Primal Solutions

Optimize the **verified primal trajectory and final best feasible value over the entire available budget**, while also seeking early improvements. The first improvement is an intermediate milestone, not a completion condition. GPT identifies the decision structure, designs moves, and implements mappings; solvers, CP, DP, and graph algorithms perform concrete searches; an independent checker decides whether a candidate may replace the incumbent. Do not change the objective into proving optimality or improving a lower bound.

## Primal-First Task Contract

- **By default, continuously improve the primal; no dual improvement is required.** Every better solution that is feasible for the original model is an intermediate result. If no incumbent exists, first find a complete feasible solution, then continue improving it. Producing a new lower bound, closing the primal-dual gap, or proving optimality is not required.
- By default, do not allocate a separate campaign to dual-bound research, global optimality proofs, or proof certificates. When primal progress stalls, change the construction, representation, neighborhood, or seed; do not automatically switch to dual work. Expand the objective only when the user separately requests it.
- LP relaxations, reduced costs, local solvers, and structural cuts may be used as auxiliary tools when they directly help construct, select, or repair candidates. Continue them according to their benefit to the verified primal, and do not substitute numerical dual progress for a primal result. Natural solver-side bound updates need not be disabled.
- Final acceptance requires feasibility on the original model and, when a finite baseline exists, a genuine objective improvement. Dual bounds and gaps are optional supplementary information. Feasibility validation is not an optimality proof, but it remains mandatory.

## Default Solver Policy: COPT First

1. Fix the original model, SHA-256, objective sense and constant, baseline source/date, known solutions, and available budget. Retain both the public headline and the independently verified baseline; they may differ. If no solution exists, seek feasibility first, without ordinary subtraction against `inf`, `=unkn=`, or solver sentinels.
2. Check existing results and negative records. For this repository, run `python scripts/case_lookup.py --name INSTANCE` and load only matching entries. The index is pinned to the 2026-09-14 commit; check for updates before further experiments. If the same original model has been proved infeasible or its incumbent globally optimal, verify the evidence and stop pointless primal search.
3. Use a trusted native parser to read variable types, rows, objective support, and extended structures such as indicators/SOS. Produce a one-page structure card covering **actual discrete decisions, completable auxiliary variables, coupling constraints, available solutions, and closed neighborhoods**. Do not load the entire MPS or huge row signatures into context. Variable names and DEC files are clues only: vehicle columns in tugela are interleaved, and small DEC blocks in dws012 may have no private variables.
4. If needed, use one short baseline to distinguish missing complete feasibility, a poor integer pattern, repairable continuous recourse, a local basin, or a difficult original representation. Include reading, modeling, lifting, and verification in time limits, not just solver `TimeLimit`. Repeating the same parameter trajectory does not constitute a different method.

## Begin with a Minimal, Reusable Diagnosis

| Signal | Priority action | Repository evidence |
|---|---|---|
| A sibling model, historical witness, or shared underlying data exists | Audit the mapping; transfer the discrete design; complete or repair it on the target original model | `bley_xs1noM`, `dws012-02`, CVRP, `nj` |
| No complete feasible solution exists | Construct while preserving quota, connectivity, or precedence; handle hard blocks; combine components, validate globally, then warm-start | `ns1905797`, `nj` |
| Fixing integer variables leaves only an LP, flow model, or difference constraints | Repair continuous recourse and establish a reliable incumbent; record whether the change is only numerical polishing | `sing17`; several tolerance counterexamples |
| Many auxiliary variables surround a small selection or ordering core | Construct on the core, lift deterministically, and return every candidate to the original model | `liu`, FHNW, `allcolor58`, `henty` |
| Point moves or small neighborhoods have failed and resources or space create correlations | Apply joint destroy-and-repair across vehicles, contiguous time windows, geometric boundaries, or related units | `tugela`, `rmine15`, `supportcase39` |
| Feasible solutions differ in large blocks and monotone descent has stalled | Use difference neighborhoods or recombination; preserve the best solution while allowing a bounded worsening kick before descending again | `nj`; negative records from `sing` and `gmut` |
| No credible structural route is available yet | Run a bounded primal-focused baseline from a verified start and compare it with structural routes under equal budgets | Generic-solver success on `nag` |

For detailed mechanisms, formulas, and minimum checks for each route, read [search-playbook.md](references/search-playbook.md). For historical positive and negative evidence, read [casebook.md](references/casebook.md). Do not impose a successful case's window size, modular indexing, or parameters on another model without evidence.

## Execute the Search Loop

Before each pilot, write: `observation -> action -> invariants to preserve -> variables to release -> completion method -> validation method -> route-switch condition`.

- **Feed a feasible solution to the backend as soon as practical.** Audit a complete solution before using it as a warm start. Partial hints guide search but cannot serve as validation. Structural construction and a general solver may alternate; they are not mutually exclusive.
- **Release semantic decisions rather than arbitrary bits.** Examples include one route, the extraction time of a mine block, or one component category. Preserve the relevant coupling rows and usually leave continuous recourse free. Zero-objective variables may control feasibility and must not be fixed automatically.
- **Change the representation or neighborhood, not only the random seed.** If a small neighborhood closes quickly without improvement, enlarge it or connect destroy regions. If a large neighborhood repeatedly finds no feasible candidate, reduce it while preserving construction invariants. Across effective operators, allocate later budget by verified gain, full elapsed time, feasible-candidate rate, and structural diversity while retaining a small exploration budget. This is a policy to calibrate, not a proved optimal allocation.
- **Remember the exact scope of every local exclusion.** Record the center-solution hash, free set, fixed variables, anchors, cutoff, and whether the search completed. Skip only a region already covered under the same center and constraints; a new incumbent usually invalidates old neighborhood conclusions. `TIME_LIMIT` and `UNKNOWN` do not mean the neighborhood is infeasible.
- **Keep `current` and `best` separate.** A kick or tabu step may temporarily worsen `current`; replace `best` only with a better original-model solution that passes validation. Deduplicate equal integer signatures unless the experiment explicitly recomputes continuous recourse.
- **Continue after every improvement.** Validate and save the new best, update the warm start, search center, and objective cutoff, reassess center-dependent neighborhood records, and then run the next search. A progress report does not end the task. Retain useful historical solutions for recombination and multistart search; do not deliver and stop merely because one improvement has been found.

## Continuous Search and Stopping Conditions

- Continue the outer loop until the user's total time or compute budget is exhausted, the user explicitly stops the work, or reliable global evidence proves that further primal improvement is impossible. Exhausting one pilot, seed, or neighborhood budget means switching routes or running the next round, not ending the task.
- A period without improvement, a local optimum, a timed-out cutoff search, or completion of a preset number of operators only triggers a route change. None proves that global improvement is impossible, and none justifies switching to dual research or stopping early.
- If the user provides no total budget, proceed in bounded rounds and ask for the total budget during progress reporting. A self-imposed limit on one round is not the user's total limit and cannot justify stopping after the first improvement. Continuous search does not authorize unlimited cost or new background automation.
- If an environment or resource blocker prevents progress, save `best` and complete restart state and report the blocker explicitly; do not claim that optimization is complete. A system interruption must also leave resumable state, and the first result must not be presented as completion.
- Reserve enough budget for final serialization and validation. At termination, report the final best solution, improvement trajectory, total elapsed time, and exact stopping reason. Do not use first-improvement stopping unless the user explicitly changes the task to "find only one better solution."

## Validation Gates Every Incumbent Update

Following [validation-and-measurement.md](references/validation-and-measurement.md), re-read the **actual serialized solution file** and check it against the untouched original model: every variable domain, ordinary row, applicable indicator and SOS constraint, objective sense, and objective constant. Reject NaN, infinity, duplicate variables, and unknown variables. Let the documented solution-file format determine whether omitted sparse entries mean zero.

`integer-fix + recourse optimize` generates a new solution; `all-variable-fix` checks the original candidate. Keep these operations distinct. Acceptance of a MIP start does not establish that the original vector passed validation. Report numerical feasibility, exact rational feasibility, and finite-precision Decimal-zero checks separately. Never present `OPTIMAL` on a fixed subproblem as optimality of the original problem.

Classify outcomes as `first_feasible`, `strict_improvement`, `recourse_improvement`, `numerical_polish`, `repair_only`, `reproduction/transfer`, or `no_improvement`. Provenance and numerical improvement are separate dimensions. Transferring the same underlying solution to three formulations yields three valid vectors, not three independent discoveries.

## Persistent Records and Delivery

Save `best.sol`, `validation.json`, `run_manifest.json`, `experiments.jsonl`, and replayable commands. The minimum restart state records the incumbent and model hashes, objective value, integer signature, current route, recent failures, and next action so that context compression does not cause old work to be repeated.

Use `python scripts/summarize_runs.py experiments.jsonl` to summarize the primal trajectory from **recorded validation results**; it does not replace an MPS checker. The measurement format is documented in the validation reference. In the final report, state the old and new values directly, attribute the improvement, give complete elapsed time, validation grade, and limitations, and link the solution and validation artifacts.

## Evidence Boundary

This skill derives from an instance-by-instance review of README files and result records for 112 problems, together with reviews of key case reports and source code. The latest table records 19 numerical improvements, including `sing17` polishing, plus 4 first finite solutions; an older 22-entry validation batch is retained separately. See [instances.md](references/instances.md) for the complete instance index and [instances.json](references/instances.json) for the machine-readable index. This is not a randomized controlled experiment and does not prove that the skill generally accelerates search. Evaluate it in later A/B tests using the same inputs, starts, hardware, and budgets.

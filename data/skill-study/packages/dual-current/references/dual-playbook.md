# Structural dual search

Use the row matching and evidence from the closest case, not its instance-specific numerical constants. The route ranking below is a synthesis of repository results, not a controlled demonstration that this order is universally faster.

## Route selection

| Observable structure | First bound-producing experiment | Required global justification | Continue or pivot |
|---|---|---|---|
| Objective on few selections; quadratic ordering/big-M auxiliaries | Project to selections; add safe resource-suffix, interval-capacity and conflict inequalities | Derive duration, release and latest-start meanings from exact rows; every original schedule satisfies the master | Add missing bottleneck intervals, then branch on the compact master; reject a cut after any valid counterexample |
| Endpoint intervals with transitive compatibility | DAG path cover / bipartite matching; clique and parity bounds | Show all original solutions induce the necessary interval ordering; use a dual matching/cover witness | Improve endpoint weights or colored structure before a generic tree |
| Repeated categorical types, free incidence flows, redundant labels | Exact aggregation, type multiplicities, component balance/parity elimination | Equality of names is insufficient; check all costs/side rows; preserve necessary integrality/congruences | Measure root bound and solve cost, not size reduction alone |
| Binary implications with few resource rows | Dualize resources; solve closure by min-cut | Correct Lagrangian signs; inner optimum or certified inner lower bound | Stabilized bundle/proximal updates, cover/clique cuts, warm-start max-flow; avoid endless oscillating subgradients |
| Chains/paths coupled by capacities | Lagrangian path/state DP | Exhaustive state transitions, exact cost accounting, every original assignment represented | Add state information or couple the most violated capacity families |
| Genuine private blocks plus few linking rows | Block convex-hull relaxation via Lagrangian or Dantzig–Wolfe | Removing linking rows really separates private variables; pricing bound must be global | Cache columns/oracles; stabilize duals; couple interacting blocks if separable relaxation plateaus |
| Binary design with continuous recourse | Benders dual cuts / feasibility rays; perspective or local disjunctive hulls | Dual feasible recourse multipliers; rays and cuts valid for all design values in scope | Multi-cuts/stronger master if recourse exact but master weak; integer recourse needs a justified integer/logic-based method |
| Unit-cost cover/packing and many dominated columns | Safe dominance, forced-cost extraction, rational LP dual; integer lattice rounding | Dominance respects every side constraint; dual covers every surviving and eliminated column through a proved map | Complete branch-dual cutoffs; conflict/clique strengthening; stop treating an incomplete tree as a bound |
| Rectangle layout or local geometry contributions | Free-coordinate small-star relaxations; complete separation branching; rational leaf bounds | No incumbent fixing; conservative coordinate box; disjoint cost edges or proved fractional cost allocation | Add profitable groups without double-counting; replace weakest group certificates |
| Small graph/routing/assignment core | Hall deficiency, cut bounds, subset/Steiner/route DP, exact enumeration | Identity of vertices/edges/domains and objective mapping; all route counts represented | Separate exceptional graph classes/case counts and retain a bound for every case |
| Arithmetic/algebraic structure | Parity/gcd, rank, capacity/area, counting inequalities; theorem matching | Exact hypotheses, signs, coverage, objective lattice; external result must match the actual model | Strengthen local counting by equality cases or finite lemma enumeration |
| Small attainable objective gap | Global cutoff feasibility model in SAT/PB/DP or MIP | Every improving original solution has an encoded witness; complete search or checked refutation | Iterate the next cutoff after success; `UNKNOWN` and timeouts prove nothing |
| No exploitable core, but original model well conditioned | Full-model root cuts / bound-focused branch-and-cut | Original or proved equivalent model; valid global cuts; correct statuses and tolerances | Diagnose root-vs-tree stalls; retain productive runs and budget alternatives fairly |

## Cheap bounds before expensive trees

Look for objective sparsity and zero-cost auxiliary variables, necessary connectedness, minimum number of selected objects, covering multiplicities, forced resource occupancy, parity and achievable cost residues. A 42-term parity argument (`allcolor58`) can outperform extensive optimization. A Hall deficiency can eliminate an entire bottleneck threshold (`lami`). On networks, separate a tree case solved by DP from all larger edge counts bounded cheaply (`dfn-bwin-DBE`).

Do not over-compress: aggregating non-identical costs or losing parity can erase exactly the structure producing a strong bound. A larger but stronger convex-hull formulation can be worthwhile. First compare build time, root bound, LP cost and memory on short comparable budgets.

## Lagrangian search that actually improves a bound

No original-model incumbent is required. If a step-size rule needs a primal target and none is available, use a target-free diminishing-step or justified stabilized bundle/master scheme. Do not suspend multiplier research to construct a primal solution. An incumbent arriving from an optional auxiliary solver can inform later updates without changing the dual objective.

For min f(x), constraints Ax≤b, x in retained set X, use λ≥0 and

`q(λ) = min_{x∈X} [f(x)+λᵀ(Ax−b)] ≤ OPT`.

1. Audit X and the dualized row list. Include objective offsets and fixed-variable costs exactly once.
2. Start with interpretable multipliers or LP prices. Use a verified closure/DP oracle where possible. If an inner minimization MIP times out, its **global lower bound**, not its best feasible value, bounds q(λ).
3. Exact minimizers supply valid supergradients for maximizing concave q. Heuristic or inexact oracles require an explicitly justified inexact method; do not treat their residuals as exact supergradients.
4. Keep the best safe q across iterations. If step updates cycle or generate repeated null steps, switch to a stabilized bundle/trust region, alter scaling, or strengthen X. A fixed count of null steps never proves dual optimality.
5. Add globally valid resource-cover cuts and dualize them, or retain a few critical couplings in the oracle. Track whether stronger oracles pay for their extra cost.
6. Replay only selected best multipliers with rational arithmetic or rigorous directed rounding; a fixed decimal precision alone does not establish exactness.

## Global cutoff progression

Derive the attainable objective lattice first. For an integer-valued minimization objective, excluding `f≤K` establishes `f≥K+1`. For lattice `a+δZ`, use the next lattice point, not an arbitrary epsilon. Without a proved lattice, report the weaker inequality actually excluded.

Retain a small exact core and encode the rest as a safe relaxation. A forward map from every original improving solution to a CNF satisfying assignment is enough to transfer UNSAT; two-way equivalence is needed only if SAT assignments must lift to original solutions. A full proof checks the map, branching completeness and all leaf refutations. After excluding one level, target the next while time remains.

## Solver use and measurement

The primary solver process serves dual progress. A separate optional primal solver may run concurrently under the shared resource budget, publish a feasible incumbent, and stop when that auxiliary purpose is met. Do not copy its primal-focused settings into the main dual process, require continued primal improvements, or delay a dual checkpoint while waiting for its result. If resources are constrained, prioritize the dual process and use an existing solution or no primal input.

Unless the user or a strict replay protocol fixes the backend, probe **COPT first**, then **Gurobi**, then **NVIDIA cuOPT**, then another compatible solver. A probe must initialize the API/executable and license, load the actual model without losing required constructs, accept the intended resource controls, and demonstrate access to a documented global bound and unambiguous status. Record every attempted backend and failure. Missing software, license failure, unsupported model features, unavailable global-bound evidence, or a reproducible fatal load/startup error justifies fallback. Slow progress, a weak bound, or an ordinary time limit does not; those support a separately logged portfolio experiment rather than silently relabeling COPT unavailable.

For COPT, use the installed-version API and documentation, preserve `Status` and the raw `ObjBound`, and start with a bound-producing baseline before changing search controls. For Gurobi fallback runs, `MIPFocus=3` is a documented option for stalled bounds and `MIPFocus=2` targets proving optimality; these settings have no assumed COPT or cuOPT equivalent. Compare them only when solver work is appropriate. Avoid primal-switch settings such as `ImproveStartTime` in a dedicated dual run unless specifically motivated. For cuOPT, verify the GPU/driver, installed MIP implementation, supported model features, and dual-bound/status API; do not enable a heuristics-only mode in the primary dual process. There is no universal best cut aggressiveness, LP method, presolve or thread count.

Describe controls first by intent: time limit, CPU threads or GPU allocation, memory, relative/absolute gap, randomness, presolve, cuts, heuristics, dual/proof focus, cutoff, branching priorities, MIP start, logging, and callbacks. For each backend record the mapping as `direct`, `approximate`, `unavailable`, or `model transformation`. A transformation needs its own model hash and validity argument. Approximate or unavailable mappings prevent a solver-only comparison and must be disclosed.

Changes that often deserve a structural test: prove tighter big-M values from variable bounds, eliminate duplicate/weak rows, strengthen on/off hulls, aggregate identical columns, and expose violated global cover/clique/energy cuts. Preserve numeric scaling and prevent unsafe coefficient rounding. Weak root bounds suggest formulation work; a strong root with a stalled tree suggests symmetry, branching, decomposition or cutoff proofs.

Use equal wall time, thread/RAM limits, initial information and model identity for performance comparisons. A historical ten-hour table and a new run on different hardware establish a bound difference, not an acceleration factor. Record preprocessing/compilation time too. Store the best numeric bound even when a stronger exact certificate is unavailable.

Official references checked 2026-09-20: [COPT modeling and MIP attributes](https://guide.coap.online/copt/en-doc/modeling.html), [COPT attributes](https://guide.coap.online/copt/en-doc/attribute.html), [Gurobi parameter guidelines](https://docs.gurobi.com/projects/optimizer/en/current/concepts/parameters/guidelines.html), [Gurobi parameter reference](https://docs.gurobi.com/projects/optimizer/en/current/reference/parameters.html), and [NVIDIA cuOPT MIP settings](https://docs.nvidia.com/cuopt/user-guide/latest/mip-settings.html). Check the installed-version documentation before using any parameter or attribute.

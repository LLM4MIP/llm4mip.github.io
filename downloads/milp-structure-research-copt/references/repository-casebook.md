# Repository casebook

These cases come from the accompanying MIPLIB open-problem repository. They are routing examples, not claims that the same method will work whenever a superficial feature appears.

## Successful closure patterns

### `fhnw-schedule-pair*`: project weak pairwise ordering onto selection

- **Signal:** the objective used only job-selection variables, while the MPS contained quadratic-many big-M ordering binaries; the LP permitted fractional overlap.
- **Reasoned route:** recover release/duration/latest-start semantics, then impose conflicts and interval energy directly on selections. Clustered deadlines supported a 200/400-binary release-suffix relaxation.
- **Why it closed:** the relaxation lower bound met an independently reconstructed feasible schedule. The master did not need to schedule every selected set; it only needed to be a valid lower-bound relaxation.
- **Critical counterexample:** an earlier version treated latest start as deadline and omitted processing time. A small original-MPS counterexample invalidated those cuts and all associated dual claims.
- **Evidence:** `docs/fhnw-schedule-pair-results-and-log-analysis-2026-09-08.zh.md`.

### `fhnw-binschedule0/1/2`: endpoint interval order plus lattice

- **Signal:** all OR supports lay within slots, so endpoint assignments determined compatibility intervals; loads were even.
- **Route:** build the interval-order DAG, derive minimum path cover via maximum matching, and round with the even-load lattice. Use a separate colored matching oracle to construct the witness.
- **Why not generic B&B:** a 539-second projected MIP stayed at a weak bound and did not expose the interval obstruction.
- **Evidence:** `instances/fhnw-binschedule0/reports/structural-investigation.md` and sibling reports.

### `neos-2978205-isar`: repeated columns become an exact quotient

- **Signal:** 320 selectors formed eight groups, but only 40 cost/structure types repeated across every group.
- **Route:** replace labeled selections by type multiplicities, aggregate continuous assignments, and prove liftability through margin realization.
- **Why the direction emerged:** an initially weak Lagrangian investigation exposed repeated types; the diagnostic failed as a bound but succeeded as structure discovery.
- **Result boundary:** the quotient-to-original mapping and lifted witness were checked; the final lower bound is a computational zero-gap result, not a portable formal MIP trace.
- **Evidence:** `instances/neos-2978205-isar/reports/final_report.md`.

### `allcolor58`: a one-line invariant beats a large autonomous workflow

- **Signal eventually used:** even capacity contributions versus 42 odd-demand obligations.
- **Route that closed:** parity lower bound plus a zero-tolerance original-MPS witness.
- **Anti-example:** two autonomous runs consumed most of their budget on parsers, schema mismatches, huge row-signature dumps, and guessed semantics; neither ran a combinatorial search. A later operator audit also proved the agent's objective-zero direction impossible.
- **Lesson:** correct structure recovery and compact invariants dominate speculative semantic reconstruction. Do not attribute the later parity idea to a run whose logs never reached it.
- **Evidence:** `instances/allcolor58/README.md` and `instances/allcolor58/framework-runs/*/operator-audit.md`.

### Graph/SAT cases: exact cutoff encoding plus proof replay

- **Signal:** the original model reduced exactly to a finite Boolean cutoff decision.
- **Route:** reconstruct CNF, solve the strict cutoff with CaDiCaL, convert/check DRAT or LRAT independently, and replay the primal against the original MPS.
- **Why it is stronger:** solver `UNSAT` alone is not the certificate; the checked trace is.
- **Evidence:** `instances/graph40-40-1rand/README.md`, `instances/graph40-80-1rand/README.md`, and `instances/bppc6-06/README.md`.

### `dfn-bwin-DBE`, CVRP, and graph-state cases: exact DP after state compression

- **Signal:** a small support/state frontier—spanning trees on ten nodes, capacity-feasible customer subsets, cyclic cutwidth, or forbidden-turn Steiner states.
- **Route:** exact subset/state DP, often with a separate cheap bound excluding larger supports.
- **Lesson:** the decisive question is state width, not original row count.
- **Evidence:** `instances/dfn-bwin-DBE/README.md`, `instances/cvrpp-n16k8vrpi/README.md`, `instances/ns1631475/README.md`, and `instances/neos-4355351-swalm/README.md`.

## Useful improvements without global closure

### `core4284-1064` and `core4872-1529`: set-cover reductions and certificates

- **Signal:** binary unit-cover rows, dominance, forced choices, rare/disjoint supports.
- **Routes:** exact row/column reduction, rational downward-rounded LP dual, disjoint-row packing, and an exact OPB cutoff for a future proof-producing backend.
- **Safety lesson:** one proposed integer row-packing bound exceeded the LP dual and was therefore impossible without extra valid inequalities; it was retracted. Two PB scripts were also discarded for row-orientation/parser errors.
- **Pivot:** when a native-cardinality solver returned `UNKNOWN`, the work switched to a weaker but portable independent lower-bound certificate.
- **Evidence:** `instances/core4284-1064/reports/final_report.md` and `instances/core4872-1529/reports/final_report.md`.

### `rmine*` and `mining`: closure core plus few resource rows

- **Signal:** nearly all local rows were two-variable precedence implications; only a small family of capacity rows coupled time/blocks. In `mining`, the block graph further reduced to directed paths with 21-state choices.
- **Routes:** maximum-closure/min-cut or path DP subproblems, Lagrangian relaxation of capacities, conflict/clique/lifted-cover cuts, and rational certificate checks.
- **Stopping evidence:** subgradient oscillation or bounds dominated by existing solver bounds motivated stabilized bundle or restricted-master work rather than more identical iterations.
- **Evidence:** `docs/rmine-family-2026-09-08.zh.md`, `instances/rmine15/reports/deep-study-2026-09-08.zh.md`, and `instances/mining/README.md`.

### `dws012-02`: reject a false decomposition, then transfer a sibling

- **Signal checked:** the official DEC file showed hundreds of small row blocks, but those blocks had no private variables.
- **Rejected route:** per-block Dantzig-Wolfe enumeration; removing master rows did not create the assumed independent recourse.
- **Successful primal route:** map the corresponding objective-supported design variables from `dws012-01`, alter the small differing selection, and reoptimize target recourse.
- **Lesson:** metadata is a hypothesis; variable-row incidence decides whether a decomposition is real.
- **Evidence:** `instances/dws012-02/reports/final_report.md`.

### `sing5/11/17`: local blocks are easy, global coupling is hard

- **Signal:** official unit-commitment blocks coupled by 336/672 demand and reserve master rows; LP fractionality and historical solution differences concentrated in particular block pairs.
- **Routes tested:** exact single/multi-block LNS, fixed-integer continuous repair, root MIR/flow-cover cuts, and Lagrangian bundle searches.
- **Negative conclusion:** many neighborhoods closed but the global gap remained; long sequences of null steps did not improve the Lagrangian bound.
- **Next route:** stronger block convex hulls, column generation, and coupling-row cuts—not broader ordinary one-block LNS.
- **Evidence:** `docs/sing-family-2026-09-08.zh.md`.

### `gmut-76-50`: solution-difference topology sets neighborhood scale

- **Signal:** a better-looking public solution failed strict integrality; after rounding, its difference from the valid solution formed one 216-column conflict-connected component.
- **Route implication:** independent small exchanges cannot reproduce the transition; use multi-remove/multi-add or component-wide search.
- **Claim boundary:** this diagnoses a neighborhood scale but neither proves improvement nor global optimality.
- **Evidence:** `instances/gmut-76-50/reports/final_report.md`.

### `fastxgemm*`: algebraic invariants, orbit exclusions, and local-boundary evidence

- **Signal:** cyclic tensor equations, slice-rank limits, tight-row disjointness, and small algebraic orbits.
- **Dual route:** lift rank/orbit exclusions into valid original-MIP lower bounds; use solver-free bitmask DP for finite cases.
- **Primal boundary:** fixed-support, Hamming-1/2, and one-vector/exchange searches were exhausted in recorded scopes. A support-relaxation witness without tensor equations is not a new decomposition.
- **Next route:** new support, multi-vector/multi-orbit transformations, larger coefficient/gauge actions, or proof-producing algebraic SAT/PB—not more fixed-support polishing.
- **Evidence:** `studies/fastxgemm-family-2026-09-09/REPORT.md`.

## Cross-case heuristic rules

- Stable integer pattern plus small continuous violations: fix integers and reconstruct continuous recourse exactly; if the objective returns to the old value, classify the apparent improvement as numerical polishing.
- A strict incumbent plus weak lower bound: invest in projection, cuts, invariants, or decomposition before more primal heuristics.
- Closed radius/window/block neighborhoods: the next admissible move must exceed the proven scope; this is a lower bound on heuristic scale, not a global bound.
- A solved sibling: transfer only through a coefficient-level crosswalk and target-MPS replay.
- `UNKNOWN`, timeout, partial proof, or controller `completed`: archive the negative result but make no mathematical closure claim.

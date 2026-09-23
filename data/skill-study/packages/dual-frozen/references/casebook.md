# Solved cases and transferable dual mechanisms

## Evidence and reading scope

Source: [Huangyc98/MIPLIB_openproblem, pinned snapshot](https://github.com/Huangyc98/MIPLIB_openproblem/tree/b329d3812c5acf51733e0e9f7baabdda7b1008d2), commit `b329d3812c5acf51733e0e9f7baabdda7b1008d2` (2026-09-14). Synthesis prepared 2026-09-16. The fixed 2026-09-04 MIPLIB-open cohort contains 112 studied instances, of which the repository lists 30 optimal and 2 infeasible; historical `rmine14` is outside that cohort. These are repository conclusions, not a claim that MIPLIB has accepted 32 new closures.

The repository's [dual comparison table](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/README.md#dual-bound-improvements-over-copt-10h) lists 41 improvements against a frozen COPT table. It is not a same-hardware/same-budget trial. Portable bounds can be weaker than historical numerical bounds, as in `rmine25`; certification progress and numerical improvement differ.

This skill uses the existing full-cohort README inventory, solved-case summaries, selected reports, and the newer [20-case dual audit](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/dual-bound-audit-2026-09-14/SUMMARY_20.zh.md). It does not rerun the 112 optimizations or independently replay their archived proofs. The September 14 audit supersedes older evidence labels/rounded values in some README rows. Its 20 cases must not be confused with any separate user's 20-instance primal campaign.

`corpus-index.json` contains all 112 names, source links/hashes, repository summaries, the 32 closure records and 41 comparison rows; audit fields are preserved separately instead of silently rewriting historical tables. Search only the desired instance. Mechanism transfer below is retrospective synthesis unless the original logs explicitly establish the original decision rationale.

## 1. Project a large scheduling formulation onto its objective decisions

**Cases:** `fhnw-schedule-paira100`, `paira200`, `pairb200`, `paira400`, `pairb400` (all with prefix `fhnw-schedule-`).

The objective is on job selection while most variables encode pairwise order. Recover exact releases r_i, latest starts ℓ_i and conservative processing durations p_i from the original inequalities. Set `D=max_i(ℓ_i+p_i)` over jobs not explicitly fixed out. Every selected interval lies before D and selected jobs do not overlap, so for each release t:

`Σ_{i:r_i≥t} p_i z_i ≤ D−t`.

A small binary release-suffix master is a global relaxation. Complete binary branching plus rational leaf duals gives an exact bound. The later proof has 7,699 total nodes for five cases and matching original-MPS feasible witnesses. Exact minima are −15.113116512593401992, −19.36996120464520581 (both 200 variants), and −36.276966742368865136 (both 400 variants).

**Transfer:** identify objective selections hidden by many auxiliaries; derive safe cumulative constraints; optimize the compact global relaxation and transfer its dual bound. Do not substitute latest start for completion deadline: that error invalidated earlier energy reasoning. Do not cite slightly higher floating-point printed values as literal exact bounds.

Source: [complete FHNW proof](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/dual-bound-audit-2026-09-14/proofs/fhnw-complete-proof.md).

## 2. Replace continuous geometry by order, matching and arithmetic

**Closed cases:** `fhnw-binschedule0/1/2` (15,958 / 55,158 / 2,428), `neos-3009394-lami` (5.5), `fhnw-binpack4-58` (infeasible).

Endpoint scheduling becomes interval-order chain cover, certified through matching/path cover or cliques; even-load arithmetic strengthens the continuous bound. In `lami`, a Hall-deficient threshold graph rules out values below 5.5. In binpack4-58, forced overlap on one axis makes the other two projections pairwise disjoint, but their required area exceeds the available area.

**Transfer:** prove a necessary projection before optimizing coordinates. Search for matching duals, antichains, area contradictions and attainable-load residues. Pure area is necessary, not sufficient for packing; this direction is exactly what a lower-bound/infeasibility argument needs. Source links for all cases are in the corpus index.

## 3. Eliminate labels and free flows, retaining discrete invariants

**Closed cases:** `neos-3594536-henty` (401,092), `neos-2978205-isar` (−11.925808687), `neos-4360552-sangro` (−8).

`henty` eliminates 4,966 free signed-flow variables using component balance, parity and a constructive lift. The reduced model closes numerically with two solvers; this remains numerical lower-bound evidence. `isar` aggregates repeated types and uses a Gale–Ryser-style realizability/lifting argument. `sangro` removes identity/inactive layers and excludes the next active-layer count in a covering relaxation; its evidence is exhaustive computation without a standalone proof trace.

**Transfer:** reducing dimension can be decisive, but do not relax away congruences or assert that a quotient is equivalent because its optimum happens to match a known solution. For a dual-only task, a proved covering relaxation can be sufficient even if every point does not lift.

## 4. Expose an exactly solvable graph core

**Closed cases:** `cvrpp-n16k8vrpi` (450), `dfn-bwin-DBE` (73,623.79), `neos-4355351-swalm` (33.45763), `neos-2629914-sudost` (48,180), `ns1631475` (11,100).

Respectively: route/subset partition DP; spanning-tree DP plus a cheap exclusion of all larger supports; a four-terminal forbidden-turn state-Steiner DP; exact QAP cut-chain enumeration; and cyclic-cutwidth exclusion plus load lattice. Large flow or assignment MIPs can encode small graph decisions.

**Transfer:** prove a crosswalk to the graph, use exact integer-scaled costs where justified, and count all states/cases. The strong `dfn` argument combines a precise small class with a lower bound for its entire complement. Do not solve the attractive class alone and assume it contains every optimum.

## 5. Search for a counting certificate before searching a large tree

**Closed cases:** `allcolor58` (42), `assign1-10-4` (422). **Still open:** `ramos3` (LB 156), `sorrell7` (LB −210).

`allcolor58` has 42 odd-demand stores whose even configurations each require a penalty; `assign1-10-4` uses exact categorical overlap counting. For `ramos3`, coverage inequalities plus their equality cases exclude a 155-point covering; finite lemma enumeration supports a complete global contradiction. `sorrell7` partitions a binary-string selection by Hamming weight, combines constant-weight counting bounds and proves cardinality ≤210. Neither of the latter two bounds alone proves optimality.

**Transfer:** start with aggregate counting, then inspect equality cases to strengthen a weak bound. A finite checker for one lemma does not establish the global summation argument. Sources: [ramos3 proof](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/dual-bound-audit-2026-09-14/proofs/ramos3-complete-proof.md), [sorrell7 proof](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/dual-bound-audit-2026-09-14/proofs/sorrell7-complete-proof.md).

## 6. Prove only the next impossible level

**Closed cases:** `graph40-40-1rand` (−9), `graph40-80-1rand` (−7), `bppc6-06` (208), `genus-sym-g31-8` / `genus-g31-8` (−23), `genus-sym-grafo5708-48` (−21).

The cut-packing instances use a full original-MPS map and independently checked LRAT refutations of the next cut count. `bppc6-06` extracts a tight-profile equality, then excludes target 207 with a checked refutation; large proof files are archived outside Git by hash, so an actual replay must obtain them. The genus results use specialized exhaustive algorithms, a different evidence type.

**Transfer:** a sharp attainable threshold can be much smaller than full optimization. Preserve all alternatives and arithmetic. In open genus siblings, completion of one face-count exclusion does not validate the next unfinished target. `graph40-20-1rand` cannot borrow a published optimum until graph identity is certified.

## 7. Transfer a theorem only after verifying the exact model

**Closed cases:** `a2864-99blp` (−257), `circ10-3` (242), `pythago7825` (infeasible). **Mixed closure evidence:** `cvrpb-n45k5vrpi` (751), `cvrpa-n64k9vrpi` (1,401).

The first three map respectively to a finite-geometry code-size theorem, a published CIRC10 optimal computation, and a published NAE-SAT UNSAT result. For the code bound, a forward map to the theorem's family suffices; extra original constraints do not invalidate it. The external computations were not all independently rerun locally.

CVRP needs more: the MPS permits a range of fleet sizes. A fixed-five or fixed-nine optimum applies only to that case; remaining route counts require numerical exclusions or exact bounds. The later CVRPB 60-second reproduction timed out instead of reproducing historical infeasibility. Retain the historical proof scope and this reproduction limitation.

**Transfer:** recover precise definitions and parameter coverage. Literature lookup should begin with structural identity and terminate in a checked applicability chain, not a matching title or objective number.

## 8. Strengthen duals without closing the original problem

| Family/cases | Productive mechanism | Boundary of the evidence |
|---|---|---|
| `rmine11/13/15/21/25` | Dualize the few capacity rows of a massive implication graph; min-cut closure, cover/clique cuts and rational flow=cut witnesses | Exact duals are not always stronger than archived numeric bounds. Continued multiplier/relaxation improvement remains meaningful |
| `mining` | Recover 967 paths and 21-state DP after relaxing 40 resource rows | Exact LB −835361895.5863052144840282387439; no new primal needed |
| `scpj4scip`, `scpk4`, `scpl4` | Exact dominance, rational dual, lattice rounding and complete branch-dual cutoffs | LB 107 / 283 / 214. Incomplete subsequent cutoffs do not increase these |
| `core4284-1064`, `core4872-1529`, `ivu06` | Forced-cost extraction, disjoint-row packing or full-column rational dual checks | A column omitted from verification or an invalid packing sum defeats the bound; consult exact names and evidence in the index |
| `graphdraw-mainerd`, `graphdraw-opmanager` | Unfixed-coordinate star subproblems with complete four-way separation branches; sum disjoint-edge costs | Exact LB 31,882 / 58,950; group optima are globally useful because they relax any original placement, not because they are small neighborhoods |
| `bley_xs1noM` | Derive finite safe M from actual variable bounds, replacing a numerically weak 10^20 constant where justified | Structural numeric-bound gain; prove the bound for each affected coefficient |
| `sing11` | Full-model root-cut work after local primal neighborhoods plateau | Numeric LB 18,853,382.0323116. This does not certify a portable bound or validate incomplete decomposition |
| `cmflsp40-36-2-10`, `siena1`, `neos-3355120-tarago`, `nag` | Full-model global numerical solver bounds | Preserve solver/model provenance; cmflsp's original runner is missing in the audit |

The graphdraw proof is particularly reusable: all coordinates in a small group remain free; original bounds justify conservative boxes; four separation directions cover every placement; each leaf has a rational LP bound; groups share vertices but not charged edges. Source: [complete graphdraw proof](https://github.com/Huangyc98/MIPLIB_openproblem/blob/b329d3812c5acf51733e0e9f7baabdda7b1008d2/docs/dual-bound-audit-2026-09-14/proofs/graphdraw-complete-proof.md).

The remaining closure, `minutedispatchstrategy`, illustrates the limit of numerical evidence: original-model zero-gap numerical closure is archived around 3109.9034777596576, but the newer audit retains a conflict with an old PDF primal value. It must not be advertised as an uncontested portable exact proof.

## 9. Failure lessons that change the next experiment

- `dws012-02`: decomposition metadata named hundreds of blocks, but no private variables supported the proposed independent pricing. Inspect the actual matrix separator.
- `sing`: closing all single-block neighborhoods is primal-local evidence. Switch to coupling convex hulls/global cuts for dual progress instead of relabeling local optima.
- `d20200`: pending subtrees block the claimed stronger cutoff. Maintain inherited bounds for every open leaf and combine by minimum.
- FHNW: latest-start/deadline confusion can make plausible energy cuts invalid. Tiny exhaustive counterexamples are a cheap route rejection tool, not a full validity proof.
- `pb-grow*`: a solver status at nonzero configured gap can look final without equality. Read bound values and gap tolerances.
- Repeated parameter changes or subgradient null steps do not constitute structural progress. Change formulation, oracle strength, stabilization or the complete cutoff being tested.

# Bound direction, scope and evidence

## Reduction contract

For a minimization MIP with feasible set F and cost f, construct a relaxed set R and map π such that every x∈F has π(x)∈R and g(π(x))≤f(x). Then any proved lower bound on min_R g is a lower bound on the original optimum. Extra constraints can be dropped; newly introduced constraints must be necessary. Lifting from R to F is unnecessary for a lower-bound-only claim. To claim an equivalent reformulation, establish both directions and objective correspondence.

Negate a maximization objective to reuse minimization reasoning, including its constant. Convert the bound back with its sign. For a negative minimization objective, −40 is a stronger lower bound than −42.

Restricted neighborhoods and fixing variables to an incumbent usually produce a subset of F. Their minimization optima are **not** global lower bounds. Valid symmetry representatives, safe dominance and reduced-cost fixing are exceptions only when their preservation conditions are proved. If solving only `f≤U`, justify U with a validated incumbent and translate the conditional result carefully; never publish a bound above U solely from the restricted model.

## Combining evidence

| Situation (minimization) | Safe operation |
|---|---|
| Multiple independent global lower bounds | Maximum |
| Exhaustive union of branches/cases | Minimum of all case lower bounds; include pending cases |
| Disjoint additive objective pieces, each relaxed independently | Sum their lower bounds, with complete cost accounting |
| Overlapping local groups | Prove a nonnegative allocation whose total charge for each cost term is ≤ its original weight; account for any remaining terms |
| Matching feasible U and proved L | Closure only at the stated evidence/tolerance level |
| Exact L, objective known in a+δZ, δ>0 | a+δ·ceil((L−a)/δ) |

No safe finite L is available from a branch whose search has not started unless inherited from a verified ancestor/global relaxation. Keep inherited bounds. Unfinished branches need not prohibit any improvement: they prevent improvement past their own certified bounds.

## Frequent decomposition errors

- **Lagrangian:** a feasible inner minimizer candidate gives an upper bound on the inner minimum. Use its certified lower bound, or solve the oracle exactly. Solver `ObjVal` is not interchangeable with `ObjBound`.
- **Column generation:** a minimization restricted-master optimum is generally an upper bound on the full-master LP optimum. Absence of a negative column in heuristic pricing is not a global certificate. Prove all reduced costs nonnegative, or use a rigorous correction with certified pricing lower bounds. For a block formulation with one convexity sum per block, a dual candidate yields the safe bound `bᵀπ + Σ_k(α_k + min(0, rLB_k))` when `rLB_k` lower-bounds every reduced cost in block k and all other dual sign conditions hold. Do not use this correction without those convexity constraints; rays require separate treatment.
- **Benders:** a feasible recourse solution gives an upper estimate, not a valid minimization optimality cut. Use dual feasible multipliers and globally valid RHS dependence. An LP dual cut still only supports the LP recourse relaxation when recourse has integer decisions.
- **Finite dictionaries:** cutting off unavailable columns can make the objective spuriously high. New pattern generation must cover the full admissible pattern universe or provide a valid pricing certificate.
- **Fixed vehicle count:** a theorem for K vehicles cannot exclude all other fleet sizes; prove minimum/maximum counts and exhaust the remainder.

## Evidence types to retain separately

1. **Global numerical solver bound:** correct original/derived model scope and solver log/API value. Record tolerances, best-bound attributes, statuses and versions. Useful research progress, not an exact rational certificate.
2. **Exact linear/combinatorial certificate:** independently checked rational multipliers, matching/cut witnesses, inequalities and model map. Checking a certificate against a derived JSON alone does not verify the original-model map.
3. **Exhaustive algorithm:** complete DP/enumeration with state coverage and arithmetic validation. A successful program run without a separate trace remains different from independent certificate replay.
4. **Checked refutation:** SAT/PB/branch proof with valid encoding, complete coverage and independent checker output. A proof hash without accessible proof data is not a replay.
5. **External theorem/computation transfer:** exact applicability crosswalk and identified external result. Distinguish reading the theorem from independently rerunning its computation.

Treat `OPTIMAL` at a nonzero configured MIP gap as tolerance closure, not equality. Do not infer infeasibility from `TIME_LIMIT`, `UNKNOWN`, or an ambiguous infeasible/unbounded status. A bound larger than a strictly feasible minimization objective is a contradiction to investigate, not an achievement.

When using decimals, parse the literal coefficients rather than binary floats. Use Fraction, rigorous outward rounding or arithmetic with checked inexact traps. Round a minimization lower bound downward for display, a maximization upper bound upward. Default decimal precision can silently round; printing 30 digits does not certify them. Only apply objective-lattice rounding after verifying the lattice and the pre-rounded lower bound. For every backend distinguish the raw global-bound attribute, any integrality-rounded bound, and the incumbent value. With COPT retain `Status` and `ObjBound`; with Gurobi compare the integrality-rounded `ObjBound` with `ObjBoundC` when debugging apparent discrepancies; with cuOPT record the installed version's documented dual-bound field and status. Never infer field equivalence from similar names.

For large full MIPs, a proof-producing backend may be more appropriate than hand-built certificates. [SCIP exact mode documentation](https://www.scipopt.org/doc-10.0.0/html/EXACT.php) describes rational solving and certificate workflows; verify local build support, certificate completion and checker availability before relying on it. Exact solving mode and an independently replayed certificate are distinct deliverables.

## Minimum audit record

Retain original model hash (specify compressed or decompressed bytes), parser/version, derived model hash and mapping, objective sense/offset, all added/fixed/removed items with justification, budget, solver status/log, numerical bound, exact bound if any, validation command/exit status and certificate hash. A compact ledger row should make it possible to distinguish a new bound, reproduction of a historical bound, and an evidence upgrade at the same value.

The primary metric needs no primal: report `L_best−L_initial` for min or `U_initial−U_best` for max, with each bound's evidence type. A valid positive change is dual improvement even when no feasible solution is known. If a validated incumbent U is independently available, optionally measure dual gap closure with fixed U: `(L_best−L_initial)/(U−L_initial)` for min, provided the denominator is positive. For max with fixed feasible L, use `(U_initial−U_best)/(U_initial−L)`. Do not blend numerical and exact series, moving incumbents or incomparable model versions. Without a primal witness, omit primal-gap metrics; do not launch primal work merely for reporting.

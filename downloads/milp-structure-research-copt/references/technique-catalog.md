# Technique catalog

This catalog explains what each method can legitimately establish and what must be checked before using it.

## Projection, quotient, and reformulation

### Exact projection

Eliminate variables that encode a choice already determined by a smaller core. To claim equivalence, document:

- a map from every original feasible point to the projected model with equal objective;
- a lifting procedure for every projected feasible point, or a precise statement that the projected model is only a relaxation;
- coefficient, bound, integrality, and objective checks on the lifted original point.

A one-way projection is still useful for a lower bound in minimization when it is a valid relaxation. Call it a relaxation, not a reduced equivalent model.

### Symmetry quotient

Quotient only by a verified automorphism of the full model. Group columns by exact coefficient and cost behavior, introduce orbit/type multiplicities, and prove that the aggregate margins can be realized. Flow, matching, or Gale-Ryser arguments are common lifting tools. Symmetry detection is also diagnostic: even a weak Lagrangian run can reveal repeated types worth quotienting.

### Compact extended formulation

Prefer a representation whose LP expresses the true combinatorial object: paths rather than pairwise time order, routes rather than arc fragments, or block convex hulls rather than independent local constraints. Measure both size and relaxation strength; smaller alone is not enough.

## Valid inequalities and lower bounds

### Conflict cuts

For binary selections `z_i,z_j`, add `z_i + z_j <= 1` only after proving that neither order or joint realization can satisfy the original model. Generate conflicts from exact windows/capacities, and validate on small exhaustive instances when possible.

### Energetic capacity cuts

For interval `[a,b]`, compute a safe lower bound `e_i(a,b)` on how much processing selected task `i` must execute inside the interval. Then

`sum_i e_i(a,b) z_i <= capacity * (b-a)`

is valid. Use outward rounding that weakens the inequality, enumerate only semantically valid endpoints, and keep a checker that recomputes each coefficient. This is especially effective when pairwise big-M order variables make the LP fractional.

### Suffix/prefix master

With a common safe deadline `D`, every selected job released at or after `t` must fit in `[t,D]`:

`sum_{i:r_i>=t} p_i z_i <= D-t`.

The model is generally a relaxation, not an exact scheduling formulation. If its bound equals a strictly audited feasible schedule, that equality proves optimality even without lifting every master solution.

### Lattice and invariant bounds

After proving an objective/load belongs to `a + g Z`, round any valid continuous/combinatorial bound to the next reachable value. Typical sources are parity, even loads, category counts, conservation, and rank. State the invariant separately from the numerical bound.

### Exact dual certificates

For a minimization LP relaxation, nonnegative row prices with the correct sign and column inequalities provide a lower bound. Convert floating multipliers to rational or directed-rounded values, verify every column inequality independently, and then use objective integrality only when proved. Disjoint-row packing is a simple solver-independent special case for set cover.

## Primal heuristics

### Structure-preserving construction

Construct directly in the recovered object—matching, route partition, schedule, sequence pair, closure set—and lift once. This usually outperforms arbitrary flips because every intermediate object preserves major constraints.

### Repair and recourse

Fix the discrete design transferred from a sibling or heuristic, then reoptimize continuous/local recourse. Audit the target instance afterward. Reject transfers based solely on matching names.

### Neighborhood sizing from evidence

- Concentrated LP fractionality: release the active blocks/times together.
- Several disconnected difference components: optimize components independently if shared rows permit.
- One large connected difference component: use multi-remove/multi-add, ejection chains, or component-wide LNS; one-flip local search is structurally incapable of reproducing the transition.
- Exhausted radius `k`: record only “no improvement in this exact neighborhood,” then choose radius/structure `>k`; never call it global optimality.

### Family transfer

Use easier siblings as controls for semantics, scaling, and method viability. A method that fails even on the easy control should not consume a long run on the hard sibling. A sibling optimum can seed the target only through a checked crosswalk.

## Decomposition

### Dantzig-Wolfe / column generation

Use when removing few master rows separates private block variables. Pricing must generate block-feasible extreme points or schedules, and the restricted master must preserve coupling. A DEC label is not sufficient evidence; compute private-variable counts and post-removal components.

### Benders decomposition

Use when a small discrete master fixes a tractable continuous, network, scheduling, or scenario recourse problem. Derive feasibility/optimality cuts from valid subproblem certificates. If subproblems share large discrete couplings, the split is probably cosmetic.

### Lagrangian relaxation

Relax few global couplings when the remaining subproblems are materially easier. Track valid dual values, serious/null steps, and control siblings. Failure at one multiplier initialization is evidence about that trajectory, not about the entire Lagrangian dual.

### Sparse physical coupling

In truss/structural design, coupling rows can be individually sparse: equilibrium, compatibility, and constitutive families may connect many member-local disjunctions without any wide row. Classify these families algebraically, then test components after removing only a semantically justified separator set. An equilibrium-capacity model formed by dropping compatibility/material equalities can be a valid minimization relaxation only after every retained/removed row class and objective term is audited. Member perspective or convex-hull formulations, Farkas/Benders cuts, and dual-sensitivity multi-member neighborhoods are then natural pilots.

## Exact decision and proof-producing search

### SAT/PB cutoff

Translate the residual claim into an exact decision problem, such as “there is no feasible solution with objective <= K.” Prove encoding equivalence or the direction needed for the claim. Preserve symbol maps and integer scaling. A SAT/PB engine's `UNSAT` status becomes portable evidence only when an independent proof checker accepts its DRAT/LRAT/VeriPB trace.

### Dynamic programming and exhaustive enumeration

Use when a graph width, subset, route count, rotation system, orbit, or state boundary is demonstrably small. Store recurrence definitions, exact arithmetic policy, state counts, hashes, and a witness/exclusion frontier. A reproducible exact program is stronger than a generic log but weaker than a compact standalone certificate unless it emits one.

### Theorem transfer

External results apply only after an exact crosswalk of instance, graph/data hash, objective convention, and assumptions. Separate the local mapping proof from the cited theorem. Do not count finding another author's result as a new algorithmic contribution.

## Solver use

Use commercial solvers for parsing, bounded diagnostics, repair, reduced models, and computational closure. Freeze model changes and parameters. Re-read the exported model independently and audit the original MPS. Solver `OPTIMAL` on a strengthened model is an original result only if every added constraint is valid and the relationship to the original is established.

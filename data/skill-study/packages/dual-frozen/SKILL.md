---
name: mip-dual-improve
description: "Continuously improve global dual bounds for hard MILP/MIPLIB problems using structural relaxations, valid cuts, decomposition, and cutoff exclusion. No primal search or improvement is required; an available solution or optional concurrent solver may supply auxiliary primal information. Use for weak or stalled dual bounds, not primal-only search."
---

# Mip Dual Improve

The sole optimization objective is to improve the best **global dual bound throughout the available budget**. For minimization raise the lower bound; for maximization lower the upper bound. A valid improvement over the stated dual baseline is a successful result even with no primal solution, no primal improvement, and no optimality proof. A first improvement is a checkpoint, not completion: continue strengthening the dual until the stopping conditions below apply.

## Keep primal work independent

Do not make primal construction, repair, polishing, improvement, or a primal report part of this skill's required workflow. Do not invoke a primal-improvement skill as a prerequisite. Start and continue dual research when no feasible solution is available.

When useful for cutoffs or multiplier targets, retrieve an already published/archived optimal solution or best-known feasible solution. Alternatively, run a solver concurrently to obtain a feasible solution using available resources. This is an optional auxiliary process: do not wait for it before advancing the dual, require it to improve the incumbent, or turn it into a separate custom primal-research task. Reserve resources for dual progress and respect the user's total time, thread, memory and concurrency limits; separate solver processes do not imply additional agent delegation.

Consume any returned solution asynchronously. Check model identity, objective sense and the validity needed before using its objective in pruning or a claimed gap; uncertain primal data remains a hint, never a basis for excluding original feasible solutions. If retrieval or the auxiliary solve fails, continue with dual methods that need no incumbent. A solution called optimal by a source is not itself a dual proof: inspect the associated proof or global-bound evidence before treating the problem as closed.

## Start with the correct model and baseline

Record the original file hash, objective sense/offset/scaling, variable domains, solver version, resource limits, and deadline. Keep the original untouched. Separate the initial reproducible numerical bound, historical reported bound, and independently certified bound. Read only the matching cases in [casebook.md](references/casebook.md); use `python scripts/case_lookup.py <instance-or-family>` for names and provenance in [corpus-index.json](references/corpus-index.json) across the 112-instance snapshot. Resolve helper paths relative to this skill directory. Repository conclusions are historical evidence, not current official MIPLIB status.

If the exact same model already has a verified global optimum or infeasibility conclusion, replay/inspect the relevant evidence and report closure. Do not spend the budget attempting an impossible improvement. An unresolved evidence discrepancy is not closure.

## Find what weakens the bound

Extract a compact matrix profile: objective support, row templates/senses, coefficient ranges, implied bounds, fractionality, repeated types, incidence components, linking rows and private block variables. Inspect sparse semantic couplings as well as wide rows. Distinguish a weak formulation from slow LPs, expensive separation, or a stalled global search tree.

Choose one or two falsifiable structural routes using [dual-playbook.md](references/dual-playbook.md). Prefer a cheap mathematical bound or compact projection when supported by the matrix. Use generic bound-focused branch-and-cut as a measured baseline or fallback; do not equate this skill with a parameter sweep. A proposed route needs a concrete executable experiment and a measurable bound target.

For every derived model write the implication: **each original feasible solution maps to a derived feasible solution whose minimization cost is no greater** (reverse the objective inequality for maximization). That one-way relaxation suffices for dual bounds. Claim equivalence only with a lifting argument. Additional cuts must hold for all relevant original feasible solutions. Fixed incumbent variables, restricted dictionaries, and local neighborhoods usually destroy this global implication.

## Continue adapting until the budget is used

Use wall-clock deadlines shared by all processes; charge analysis, construction, failed attempts, solving and validation to the same task budget. Respect user-specified batch sizes, CPU/RAM and concurrency limits. This skill does not authorize new agents, remote spending, or public submissions.

A flexible starting allocation is 10–15% diagnosis/baseline, 60–75% adaptive bound search, and 15–20% validation and consolidation. For a requested 90–150 minutes per instance, take short 5–15 minute diagnostic checkpoints, while preserving a productive longer solver run. These are planning defaults, not minimum runtimes or performance promises.

Maintain a portfolio of validated global routes. After improvement, save the model, bound evidence and elapsed time, then strengthen the same relaxation, generate another cut family, stabilize multipliers, or attack the next attainable cutoff. After two unproductive probes without new information, change the representation or oracle rather than repeating settings. Stop a failed route, not the whole task. Do not restart a productive tree merely to satisfy a checkpoint.

Combine independent minimization lower bounds by **maximum**. For exhaustive alternative cases/branches take the **minimum** of their lower bounds, including all unfinished cases. Sum subproblem bounds only when objective accounting and a feasible-set relaxation justify it. See [bound-validity.md](references/bound-validity.md) before publishing bounds or implementing decomposition.

Track numerical and exact progress separately. A valid full-model floating-point solver bound is useful: save and label it immediately. Do not spend most of the search budget certifying a weak bound while stronger structural routes remain feasible. Certify selected best candidates, ideally with cheap reusable checkers. For a rational linear-bound building block, see [linear-certificate.md](references/linear-certificate.md) and `scripts/verify_linear_bound.py`; it does not validate an MPS transformation or a whole branch tree.

End at the requested budget, user stop, accepted global closure, or a documented hard external blocker after useful fallbacks are exhausted. Lack of improvement alone is not a stopping reason. Never claim improvement, optimality, or infeasibility to satisfy a time target.

## Deliver evidence of progress

Save a compact chronological ledger with time, model hash/scope, route, cumulative resources, numerical bound, certified bound, proof/log paths, and pivot rationale. Report initial → best numerical and initial → best certified bound separately; include absolute dual improvement, first-improvement time and later checkpoints. Primal fields and gap calculations are optional: do not obtain a primal solution just to fill them. If an independently available validated incumbent is used, keep it fixed for gap-closure comparisons so primal changes do not masquerade as dual gains.

Return the best bound with its direction, scope and evidence type, a replay command, unresolved limitations, and the highest-value continuation experiment. Report an honest plateau when none of the routes improves the baseline.

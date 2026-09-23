---
name: milp-structure-research-copt
description: "Diagnose hard MILP or MIPLIB instances with COPT model access and route them to structure-specific reformulations, cuts, primal heuristics, decompositions, or proof-producing searches. Use when a generic COPT run stalls, when a bound or incumbent needs an auditable improvement, or when deciding what research direction a particular matrix structure supports; do not use for routine model construction or parameter-only tuning."
---

# MILP Structure Research with COPT

Treat the task as mathematical diagnosis, not as a solver-parameter contest. The goal is to find the smallest exact or safely relaxed decision space that still controls the desired claim.

## Workflow

1. **Freeze the claim and baseline.** State whether the target is a feasible incumbent, a better primal bound, a valid dual bound, feasibility/infeasibility, or global optimality. Record objective sense, authoritative MPS hash, incumbent source, published bounds, tolerances, and time budget. Locate and strictly replay the best available incumbent before using a short baseline run to classify the bottleneck.
2. **Read the untouched model before optimizing.** Use COPT for parsing and matrix access. Run `scripts/profile_mip_structure.py` when possible. Check expected row, column, and nonzero counts; a mismatch is an infrastructure failure, not a mathematical result.
3. **Recover semantics with evidence.** Combine row algebra, variable domains, names, official descriptions, sibling instances, decomposition files, and papers. Treat names and DEC files as hypotheses until matrix checks confirm them. When explaining an earlier agent's choice, also apply `references/decision-trace-audit.md`.
4. **Locate the bottleneck.** Separate these cases: missing/weak incumbent; strong incumbent but weak relaxation; feasibility unknown; small residual cutoff needing proof; or numerical/audit uncertainty. Do one short baseline run only if it will distinguish these cases. For decomposition, search repeated local templates and semantically verified sparse row-family separators; wide rows alone do not identify coupling.
5. **Generate at least two structural hypotheses.** For each, write the signal, claimed mapping, cheapest falsification test, expected artifact, and pivot condition. Use `references/structure-routing.md` to select candidates and `references/technique-catalog.md` for implementation details.
6. **Run bounded pilots, not broad campaigns.** Prefer a test that can disprove a proposed decomposition, quotient, cut, or neighborhood quickly. Keep negative results with their exact scope; use them to determine the next neighborhood radius or proof technology.
7. **Separate construction from proof.** A primal heuristic must produce a witness for the original MPS. A lower-bound method must remain a valid relaxation or emit a checkable certificate. Equality between independently audited primal and dual values is the desired closure pattern.
8. **Map back and verify independently.** Replay every witness against all original rows, bounds, and integrality conditions. For reductions, prove both projection and lifting when claiming equivalence. For SAT/PB, require a checked proof trace for a portable UNSAT claim.
9. **Report evidence scope and provenance.** Distinguish solver zero gap, exact enumeration, portable certificate, theorem transfer, and heuristic evidence. Apply the claim rules and stopping criteria in `references/evidence-and-stopping.md`.

## Decision discipline

- Do not infer problem semantics from a few names or rows, and do not call a solver status on a relaxation an original-model result.
- Do not promote a better-looking objective until strict integrality and original-row checks pass.
- Do not say why an earlier agent chose a direction unless the log records it. Label decision evidence as explicit, contemporaneous pivot, or retrospective inference.
- Avoid repeated generic parameter sweeps after the same primal/dual trajectory plateaus. Change the representation, relaxation, neighborhood scale, or certificate route instead.
- Keep summaries bounded. Large row dumps and repeated pagination are evidence-handling failures; store full machine artifacts and pass compact statistics plus stable paths to the reasoning model.

## Output contract

Produce:

1. a structure card with authoritative counts and semantic confidence;
2. a ranked route table with reasons and falsification tests;
3. an experiment ledger covering successes and negative results;
4. strict original-model audits for any candidate;
5. a final claim whose wording matches the evidence level;
6. the next high-value experiment when the instance remains open.

Use the compact schemas in `references/output-templates.md` so decisions and negative results remain machine-readable and survive handoffs.

For examples and anti-patterns drawn from the MIPLIB research repository, read `references/repository-casebook.md`.

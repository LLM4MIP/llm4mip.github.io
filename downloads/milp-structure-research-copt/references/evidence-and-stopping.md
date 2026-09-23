# Evidence, validation, and stopping rules

## Claim ladder

Use the strongest wording supported, and no stronger:

1. **Candidate only** — heuristic output not yet replayed.
2. **Strict feasible witness** — bounds, integrality, all original rows, and objective independently checked.
3. **Valid bound** — a relaxation/certificate has been checked in the correct objective direction.
4. **Computational closure** — strict witness and solver lower bound meet at stated tolerances on a proved-equivalent or safely strengthened model; no portable exact lower-bound trace.
5. **Exact exhaustive conclusion** — deterministic finite enumeration/DP with reproducible code and audit, but no compact independent trace.
6. **Portable exact certificate** — an independent checker validates the proof without trusting the optimizing solver.
7. **Theorem transfer** — exact local crosswalk plus an external published theorem/result.

Never collapse these levels into a single “proved by GPT” count.

## Minimum validation

### Primal witness

- Parse the untouched original MPS with a trusted reader.
- Check every variable bound and integrality condition at a stated tolerance; also provide a zero/decimal audit when the claim is sensitive.
- Evaluate every original row and the objective independently.
- Record MPS and witness hashes and provenance.
- Reject a better-looking public or generated solution if it relies on near-integer values beyond the strict policy.

### Lower bound or infeasibility

- State whether the model is equivalent, strengthened by valid cuts, or relaxed.
- Check cut signs, RHS semantics, coefficient rounding, and objective sense.
- For duals, verify every dual sign and column inequality using rational or directed-rounded arithmetic.
- For SAT/PB, retain the encoding map, solver status, proof hash, checker, checker version, and successful independent output.
- `UNKNOWN`, timeout, or a missing proof file establishes nothing about infeasibility.

### Reduction

- Exact quotient/equivalence: prove projection and lifting.
- Lower-bound relaxation: prove every original solution projects feasibly with unchanged or favorably bounded objective.
- Primal construction: lifting alone may suffice, but the lifted point must pass the original-model audit.

## Decision provenance

When explaining why an agent chose a route, mark one of:

- **A — explicit:** the contemporaneous method-selection or reasoning log states the signal and reason.
- **B — observed pivot:** artifacts show the structural observation first and the method change afterward, even if the rationale is terse.
- **C — retrospective inference:** the route is consistent with the structure, but the log does not establish that this caused the decision.

Do not rewrite C as A. If post-run operator work found the decisive invariant, say so explicitly.

## Stop and pivot rules

Stop a route when one of these conditions holds:

- parser counts or trusted-reader values disagree;
- a tiny exhaustive counterexample invalidates a proposed cut or mapping;
- a decomposition has no private blocks after removing the claimed master rows;
- several runs reproduce the same primal/dual plateau without new structural information;
- every radius-`k` or listed block neighborhood is exactly closed, so the next move must exceed that scope;
- a relaxation remains orders of magnitude below the incumbent after its intended structural strengthening;
- SAT/PB returns `UNKNOWN` repeatedly and cannot emit a checkable proof;
- generated artifacts exceed the reasoning interface budget and compact summaries are not available;
- numerical changes are below declared tolerances and have no exact structural interpretation.

A stop is not a failure if it eliminates a method class or determines the required next scale. Archive:

- what exact hypothesis was tested;
- the covered neighborhood/state/cutoff;
- parameters, time, and tool versions;
- why the result does or does not generalize;
- the next representation-changing experiment.

## Anti-patterns

- Guessing semantics from variable names and then forcing the model into a familiar class.
- Dumping hundreds of thousands of row signatures into model context.
- Treating official decomposition metadata as proof that Dantzig-Wolfe blocks are independent.
- Calling an invalid rounded near-integer solution a primal improvement.
- Treating local search exhaustion as a global bound.
- Treating a support-only relaxation as an algebraic proof.
- Reporting solver `UNSAT` without the independently checked trace requested by the evidence policy.
- Repeating generic solver settings after the bottleneck is known to be formulation strength.

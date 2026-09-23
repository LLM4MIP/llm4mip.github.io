# Decision-trace audit

Use this reference when the task asks why an earlier GPT/agent chose a route, or when archived prompts, controller state, chats, and reports disagree.

## Authority order

Prefer evidence in this order:

1. untouched original model, hashes, independently checked witness/certificate;
2. controller result ledger and operator-registered verification;
3. actually executed source, tool output, and machine artifacts;
4. contemporaneous method-selection and decision notes;
5. later final narrative;
6. prior archives and external prose.

A model's self-reported memory is not proof. A later report cannot establish what the model knew earlier unless the cited source was available in that turn.

## Reconstruct the timeline

For each material decision, record:

| Field | Content |
|---|---|
| time / turn | when the decision occurred |
| available facts | evidence already visible at that point |
| hypotheses | interpretations not yet proved |
| chosen route | the actual next action |
| rejected routes | explicit or implicit alternatives |
| expected information gain | what result would distinguish hypotheses |
| outcome | mathematical, infrastructure, or no information |
| pivot rule | stated or missing |
| evidence grade | A explicit, B observed pivot, C retrospective inference |

Then run a separate hindsight pass:

- **available but unused:** a cheap check or source already existed, so criticizing its omission is fair;
- **discovered later:** useful evidence arose only after the run, so do not claim the agent should have known it;
- **external seed:** the target or construction came from literature/another author;
- **project contribution:** a new mapping, witness, bound, or certificate was derived and checked locally.

## Failure taxonomy

- **Infrastructure:** missing file, parser mismatch, model-count mismatch, unavailable dependency.
- **Implementation:** a local bug with a known specification and bounded repair.
- **Representation:** correct code emits unbounded dumps, repeated pagination, or an unusable state space.
- **Semantic:** row algebra does not justify the inferred application meaning.
- **Mathematical:** the correctly implemented, correctly mapped method fails within a precisely described scope.

Repair infrastructure/implementation once when the repair is local and increases information. Repeated failures of the same type trigger a route review. Representation and semantic failures require changing the abstraction; they are not solved by longer execution.

## Framework statuses versus mathematical statuses

Do not translate `completed`, `success`, `reserved_handoff_budget`, token exhaustion, or a generated report into MILP progress. Mathematical ledger fields require independently accepted evidence:

- strict primal witness;
- checked lower bound;
- verified optimality/infeasibility certificate;
- otherwise `unknown` or an explicitly scoped negative result.

## `allcolor58` cautionary pattern

The archived autonomous run began with a sound rule—trusted structure audit and incumbent replay before semantic encoding—but later web/extractor failures caused repeated script repair and guessed coloring/sequence interpretations. Bounded memory then lost the prior conclusion that objective-zero candidates were invalid, and the agent returned to that attractive but false route. The controller correctly refused to accept the self-reported dual bound. A post-run operator check showed a single dominating row already excluded objective zero, while the later optimum-42 parity certificate came from separate work. This case demonstrates why decision rules must persist as gates, negative findings must remain in memory, and post-run discoveries must not be backfilled into the agent's contemporaneous rationale.

# Output templates

Use these compact records so negative results and evidence survive context compression.

## Structure card

```yaml
instance: ""
original_model:
  path: ""
  sha256: ""
  variables: 0
  rows: 0
  nonzeros: 0
objective:
  sense: "min|max"
  support_count: 0
baseline:
  primal: null
  dual: null
  source: ""
  tolerance: ""
semantic_facts: []
semantic_hypotheses: []
unknowns: []
matrix_signals: []
bottleneck: "primal|dual|feasibility|proof|audit"
```

## Route record

```yaml
route_id: "R1"
signal: ""
hypothesis: ""
decision_evidence: "A-explicit|B-observed-pivot|C-retrospective"
required_mapping: "projection|lifting|equivalence|cut-validity|encoding"
cheapest_falsification: ""
pilot:
  method: ""
  budget: ""
expected_artifact: "strict witness|valid bound|proof trace|negative scope"
success_gate: ""
stop_or_pivot: ""
```

## Experiment ledger row

| Field | Required content |
|---|---|
| ID / timestamp | stable identifier |
| model + hash | untouched or derived model and relation to original |
| route / hypothesis | exact claim under test |
| executed command / code hash | reproducibility |
| budget / versions | time, nodes, tokens, solver/checker versions |
| result | numerical status and artifact paths |
| independent audit | checker and pass/fail |
| mathematical scope | global, relaxation, fixed pattern, radius, blocks, cutoff |
| provenance | external, external-derived, project-derived, solver-generated |
| proof grade | candidate, witness, bound, computational, exact, portable, theorem |
| next decision | continue, repair once, change representation, or stop |

## Final claim

```yaml
claim:
  type: "primal|dual|optimal|infeasible|negative-local"
  value_or_scope: ""
  wording: ""
evidence:
  original_mps_audit: ""
  mapping_check: ""
  proof_or_solver_artifact: ""
  independent_checker: ""
provenance: ""
limitations: []
next_experiment: ""
```

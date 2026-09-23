# polygonpack5-15

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Verified feasible; open
- **Best verified result:** -55,494,687.647606651289167114364938... (strict repair)
- **Best bound or certificate:** no new global lower bound
- **Study result:** Improves the only audited official literal-zero solution but not the MIPLIB tolerance headline; global optimum open

## Interpretation

The benchmark study does not report a certified global optimum or infeasibility result for this instance. The archived work may still contain a stricter incumbent, a stronger lower bound, an exact structural reduction, a closed local neighborhood, or a documented negative experiment.

## Experiment workflow

1. Freeze the original model, baseline, objective convention, and acceptance tolerance.
2. Profile the untouched formulation and propose falsifiable structural hypotheses.
3. Run bounded primal, dual, reduction, or certificate experiments with explicit stopping rules.
4. Map useful results back to the original MPS and classify the resulting verification method.

## Download bundle

The sibling `.tar.gz` archive copies the related research material from this instance directory and adds this summary plus a package manifest. Only official raw `.mps`/`.mps.gz` inputs are omitted to avoid redistributing bulky benchmark source files; public solutions, hashes, derived proof models, runs, logs, and any proof traces present in the directory remain included. Files retained externally by hash cannot be embedded here.

## Provenance

Generated from the local `MIPLIB_openproblem` research archive for the LLM4MIP website. Read the source instance README and package manifest before reusing a numerical claim.

- **Source base commit:** `89a8abd0847941bdf774353a1983d5e6a00457a0` plus the disclosed 18 September working-tree reconciliation
- **Source README SHA-256:** `8ef27da1f430907eac6188b940efabcfa02860383ae149c3b4594548f548ceab`

## Package integrity

- **Archive:** `polygonpack5-15-findings.tar.gz`
- **Compressed bytes:** `633263`
- **SHA-256:** `23f583c98ee1115b3c1d1de9a6673d548dd5e1686a480365f896bc390cb4eadc`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/polygonpack5-15/README.md

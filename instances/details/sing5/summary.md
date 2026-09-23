# sing5

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Verified feasible; open
- **Best verified result:** 18,778,435.60767737 (strict)
- **Best bound or certificate:** 18,462,676.77864 (locally reproducible solver LB; 1.6815% gap)
- **Study result:** Imported run improves the prior local LB by 19,778.272826703; archived PDF-only LB 18,605,207.3 remains stronger; runtime metadata is inconsistent; global optimum open

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
- **Source README SHA-256:** `9015c095dcb3a3a96ff7e782f126e793781e11ef87e4775c34e2594a10dda0da`

## Package integrity

- **Archive:** `sing5-findings.tar.gz`
- **Compressed bytes:** `350596`
- **SHA-256:** `700c988c5508ef8b34ff00ace50035feddf6db39e0ac19389dc9c88ed1098dae`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/sing5/README.md

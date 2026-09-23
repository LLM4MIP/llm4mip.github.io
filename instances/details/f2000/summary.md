# f2000

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Verified feasible; open
- **Best verified result:** 1,810
- **Best bound or certificate:** 1,332 root
- **Study result:** Feasible minimum-prime-implicant witness; global optimum open

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
- **Source README SHA-256:** `762e3644517fd1e15e72df60b6ce8f4bd2494239e3332192de90b3e253650271`

## Package integrity

- **Archive:** `f2000-findings.tar.gz`
- **Compressed bytes:** `656624`
- **SHA-256:** `b544861af7aae7651e0b1704af3a336b16028e7eb1bc9f82d20d3a170c8219fa`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/f2000/README.md

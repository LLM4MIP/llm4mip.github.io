# sing11

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Verified feasible; open
- **Best verified result:** 19,108,639.4603941927675439822 (strict repair)
- **Best bound or certificate:** 18,853,382.0323116 (solver; 1.3358% gap)
- **Study result:** 1,200 s root-cut LB improves archived PDF-only LB by about 76,817.9; 74/74 blocks and 6 selected groups closed conditionally; global optimum open

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
- **Source README SHA-256:** `a94c6b37fbd0cc1fb338b2ccb41b69ed2c3458c96d8bb0e1baa9049480a8c895`

## Package integrity

- **Archive:** `sing11-findings.tar.gz`
- **Compressed bytes:** `697659`
- **SHA-256:** `e99cd402fdfadf78a0c8e4647f957f3645eada22a3d13c8f2234ad6de123d614`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/sing11/README.md

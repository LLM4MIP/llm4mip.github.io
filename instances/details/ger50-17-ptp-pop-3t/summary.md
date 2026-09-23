# ger50-17-ptp-pop-3t

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Verified feasible; open
- **Best verified result:** 5,224.5144 (strict)
- **Best bound or certificate:** 5,183.93592586653 (solver)
- **Study result:** Exact flow scaling; conflicting Gurobi 13 zero-gap output rejected; 0.7767% numerical gap; global optimum open

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
- **Source README SHA-256:** `e2f2afaa66f6efa30a78365774c4556b758147ae2b983ac4dd6839430ae3de42`

## Package integrity

- **Archive:** `ger50-17-ptp-pop-3t-findings.tar.gz`
- **Compressed bytes:** `32171`
- **SHA-256:** `c0fd3754b5c9c532ead6ced3ae54aefa7b885db4b67c15e21fe0594bf53132f4`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/ger50-17-ptp-pop-3t/README.md

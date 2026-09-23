# neos-3009394-lami

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 5.5
- **Best bound or certificate:** 5.5
- **Study result:** Optimal, exact Hall/matching certificate

## Certified optimality or infeasibility result

- **Conclusion:** OPT = 5.5
- **Main method:** exact bottleneck matching + Hall deficiency
- **Verification category:** PE — Portable exact certificate
- **Earlier source-table status:** self-contained exact certificate
- **Reconciliation rule:** The verification category above governs this summary when older instance or table wording differs.

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
- **Source README SHA-256:** `006aa5717c7578c8fab4e581710b38993394759a3bbedc4f137434472ab31bd5`

## Package integrity

- **Archive:** `neos-3009394-lami-findings.tar.gz`
- **Compressed bytes:** `39060`
- **SHA-256:** `9504f5520e54cb1195dfe562610f8d633f74d6e60b4090d6629f7ecdd7d73fbb`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/neos-3009394-lami/README.md

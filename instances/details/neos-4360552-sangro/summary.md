# neos-4360552-sangro

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** -8
- **Best bound or certificate:** -8
- **Study result:** Optimal, exact active-layer quotient and A=9 relaxed infeasibility

## Certified optimality or infeasibility result

- **Conclusion:** OPT = -8
- **Main method:** exact active-layer quotient + A=9 interval-chain infeasibility
- **Verification category:** EX — Specialized exact exhaustive computation without a standalone trace
- **Earlier source-table status:** exact exhaustive computation; no standalone proof trace
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
- **Source README SHA-256:** `2509bc198225fb3a51620948cb7c74a36aaa38d13b78b0124077fa2971187f06`

## Package integrity

- **Archive:** `neos-4360552-sangro-findings.tar.gz`
- **Compressed bytes:** `183453`
- **SHA-256:** `882f519f325f4ffff9e72d38562f813fcede43214552eb05fb07c121f0f2cddc`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/neos-4360552-sangro/README.md

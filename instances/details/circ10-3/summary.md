# circ10-3

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 242
- **Best bound or certificate:** 242 published
- **Study result:** Optimal, exact MPS crosswalk + published exhaustive result

## Certified optimality or infeasibility result

- **Conclusion:** OPT = 242
- **Main method:** exact MPS/TTP crosswalk + published exhaustive result
- **Verification category:** LT — Exact crosswalk plus published theorem or exhaustive result
- **Earlier source-table status:** literature-dependent theorem transfer
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
- **Source README SHA-256:** `daea6a1aa6cd12e9c46b496f2a5700d80ade6a68b8ea900ff54e217437ab9a0d`

## Package integrity

- **Archive:** `circ10-3-findings.tar.gz`
- **Compressed bytes:** `23734`
- **SHA-256:** `1ff69af9fbad108dc18caf6d99b844b772f918332f1fe7734ed9b20ead7b83c0`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/circ10-3/README.md

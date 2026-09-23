# pythago7825

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** —
- **Best bound or certificate:** published UNSAT theorem
- **Study result:** Infeasible, exact encoding/core crosswalk + published theorem; proof archive not replayed locally

## Certified optimality or infeasibility result

- **Conclusion:** infeasible
- **Main method:** exact NAE-SAT crosswalk + published UNSAT theorem
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
- **Source README SHA-256:** `5d5a2498ad546979018e8db84927a80950529ad3a6a25447fc1d4f35c7e88ef0`

## Package integrity

- **Archive:** `pythago7825-findings.tar.gz`
- **Compressed bytes:** `35485509`
- **SHA-256:** `0c18d633672347f5cd109d59d33cfb6974f2ebf7e1bde9648506130b4d538dc9`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/pythago7825/README.md

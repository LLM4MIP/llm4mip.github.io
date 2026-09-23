# a2864-99blp

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** -257
- **Best bound or certificate:** -257 published theorem
- **Study result:** Optimal, exact geometry crosswalk + published theorem; theorem computation not replayed locally

## Certified optimality or infeasibility result

- **Conclusion:** OPT = -257
- **Main method:** exact finite-geometry crosswalk + published theorem
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
- **Source README SHA-256:** `6812ae53802aa55f10ddc08af9d8f9a61b6ebc3cd3fc99d125ade44a193a0d54`

## Package integrity

- **Archive:** `a2864-99blp-findings.tar.gz`
- **Compressed bytes:** `1788900`
- **SHA-256:** `10e5547115950529b564719ab2531d6753239c62069ec7f3811e89ac2536d2a5`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/a2864-99blp/README.md

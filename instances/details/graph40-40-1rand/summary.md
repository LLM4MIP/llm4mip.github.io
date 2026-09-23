# graph40-40-1rand

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** -9 (9 cuts)
- **Best bound or certificate:** -9
- **Study result:** Optimal, original-MPS/CNF/LRAT certificate

## Certified optimality or infeasibility result

- **Conclusion:** OPT = -9
- **Main method:** original-MPS audit + ten-cut CNF/LRAT + witness
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
- **Source README SHA-256:** `1112244f6345b07c94aeca57afe9399be574dc852d8ca79fe7540a3794f6703f`

## Package integrity

- **Archive:** `graph40-40-1rand-findings.tar.gz`
- **Compressed bytes:** `728229`
- **SHA-256:** `5fcb923d67e6b056d6e557a1bf2d222063242072a526d44d0d612515f8738a11`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/graph40-40-1rand/README.md

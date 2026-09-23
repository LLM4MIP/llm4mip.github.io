# fhnw-binschedule1

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 55,158
- **Best bound or certificate:** 55,158
- **Study result:** Optimal, exact interval-order path-cover certificate

## Certified optimality or infeasibility result

- **Conclusion:** OPT = 55,158
- **Main method:** endpoint interval-order path cover + colored matching witness
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
- **Source README SHA-256:** `0e338ff58b2284f24d1fc14cb3d01f8545399d2e7363f0b003aa3dd4ff161b0d`

## Package integrity

- **Archive:** `fhnw-binschedule1-findings.tar.gz`
- **Compressed bytes:** `120272`
- **SHA-256:** `9337e1b07a2828c3beb4dc311042167a22088cfeea1a8e17548281b374637b84`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/fhnw-binschedule1/README.md

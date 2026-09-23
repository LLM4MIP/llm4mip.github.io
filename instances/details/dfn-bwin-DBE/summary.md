# dfn-bwin-DBE

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 73,623.79
- **Best bound or certificate:** 73,623.79
- **Study result:** Optimal, exact spanning-tree DP and cost exclusion

## Certified optimality or infeasibility result

- **Conclusion:** OPT = 73,623.79
- **Main method:** exact spanning-tree subset DP + ten-edge cost exclusion
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
- **Source README SHA-256:** `03837fed0d6890335cf8cfba0a0a15ec0bf5741a903da5237c3b49b3e72a1351`

## Package integrity

- **Archive:** `dfn-bwin-DBE-findings.tar.gz`
- **Compressed bytes:** `27221`
- **SHA-256:** `0b5cee42c76e918d1edea4dd038c62a5a7133d332c82755a2ea033b2f5f71b53`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/dfn-bwin-DBE/README.md

# neos-4355351-swalm

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 33.45763
- **Best bound or certificate:** 33.45763
- **Study result:** Optimal, exact state-Steiner DP and zero-violation witness

## Certified optimality or infeasibility result

- **Conclusion:** OPT = 33.45763
- **Main method:** exact forbidden-turn state-Steiner subset DP + witness
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
- **Source README SHA-256:** `e7e502188eabd31038087f68c51930bf8e78e0a670324419b1a33520a8f04c0f`

## Package integrity

- **Archive:** `neos-4355351-swalm-findings.tar.gz`
- **Compressed bytes:** `212807`
- **SHA-256:** `4ed61bea7dfa9d4f5df067d91c0a6998ae03be0aa6d43f16943650f40125cfa1`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/neos-4355351-swalm/README.md

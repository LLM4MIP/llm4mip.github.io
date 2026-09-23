# minutedispatchstrategy

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 3,109.9034777596576
- **Best bound or certificate:** 3,109.9034777596576 (Gurobi)
- **Study result:** Repository computational closure; official page still open; strict primal audit, not yet incorporated into or confirmed by MIPLIB, and no portable exact lower-bound certificate

## Certified optimality or infeasibility result

- **Conclusion:** solver-supported optimum approximately 3,109.9034777596576
- **Main method:** original official MPS + public MIP start + zero-gap Gurobi 13.0.1; no user cuts
- **Verification category:** NS — Strict primal audit plus floating-point zero-gap solver run
- **Earlier source-table status:** not incorporated into or confirmed by MIPLIB; v36 records =best= and the current page remains open; no primal improvement and no portable exact lower-bound certificate
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
- **Source README SHA-256:** `3b4631788c1dfee3bfe807c494e4dc5c244cb8828eab236a040a8a884e84d783`

## Package integrity

- **Archive:** `minutedispatchstrategy-findings.tar.gz`
- **Compressed bytes:** `1095649`
- **SHA-256:** `c86b811d702ab7f0b2c4b6db018e26974385b7e0694a31bf7d7b70dfa9e0e6a9`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/minutedispatchstrategy/README.md

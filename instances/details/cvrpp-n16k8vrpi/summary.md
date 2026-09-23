# cvrpp-n16k8vrpi

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 450
- **Best bound or certificate:** 450
- **Study result:** Optimal, exact dynamic program

## Certified optimality or infeasibility result

- **Conclusion:** OPT = 450
- **Main method:** capacity-feasible route DP + exact partition
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
- **Source README SHA-256:** `35cab24397e9f9d906415b035ecf584cb9942463f48b5fce4a2826a44a4de0d0`

## Package integrity

- **Archive:** `cvrpp-n16k8vrpi-findings.tar.gz`
- **Compressed bytes:** `56481`
- **SHA-256:** `46490f9f2735ac69a2f2d7c2b4c108e205212a6612045c65d2cc4b0bc6d2d074`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/cvrpp-n16k8vrpi/README.md

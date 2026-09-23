# cvrpb-n45k5vrpi

> Snapshot: 2026-09-18 UTC. This is a concise publication summary of the archived research state; it is not an official MIPLIB status change.

## Results and progress

- **Benchmark outcome:** Certified optimality / infeasibility
- **Best verified result:** 751 (new strict incumbent)
- **Best bound or certificate:** 751
- **Study result:** Optimal, mixed database/computational verification; no portable exact lower-bound trace

## Certified optimality or infeasibility result

- **Conclusion:** OPT = 751
- **Main method:** exact compiled-MPS projection + CVRPLIB five-route optimum + Gurobi exclusion for at least six routes
- **Verification category:** MX — Mixed database and commercial-solver verification
- **Earlier source-table status:** mixed database/computational optimality verification; no portable exact lower-bound trace
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
- **Source README SHA-256:** `ef221375d4007d8412b94f151d249e6add9420d5179938fa5e9974783a972fbc`

## Package integrity

- **Archive:** `cvrpb-n45k5vrpi-findings.tar.gz`
- **Compressed bytes:** `410499`
- **SHA-256:** `d0018d62206b8e379baffa9628d861eeb850104c1bfb409257c2268f00f1d057`
- **Pinned source README:** https://github.com/Huangyc98/MIPLIB_openproblem/blob/89a8abd0847941bdf774353a1983d5e6a00457a0/instances/cvrpb-n45k5vrpi/README.md

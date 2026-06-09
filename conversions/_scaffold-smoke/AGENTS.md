# Competitor-Pricing Digest (ICM workspace)

Layer 0 — workspace identity. Produces a weekly digest of competitor price changes.

## Purpose

Each week: collect competitors' current prices, compare against last week's
snapshot, and write a short digest of what moved and by how much.

## How this workspace works

Run stages in order: `01_collect` → `02_compare` → `03_digest`. Read each stage's
`CONTEXT.md`, load its inputs, do the process, write outputs to its `output/`. Review
at each boundary.

## Where to find things

- `CONTEXT.md` — Layer 1 routing.
- `_config/competitors.yaml` — Layer 3, the competitor + product list to track.
- `stages/NN_*/` — the pipeline.

## Structure

- `01_collect` — read the competitor list, gather current prices → this week's snapshot.
- `02_compare` — diff this week's snapshot against last week's → list of changes.
- `03_digest` — write the digest from the change list.

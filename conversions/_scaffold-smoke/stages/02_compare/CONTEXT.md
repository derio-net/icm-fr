# Stage 02 — Compare (Layer 2 contract)

## Inputs
- Layer 4 (working): ../01_collect/output/snapshot.md     # this week's prices
- Layer 4 (working): last-snapshot.md                     # last week's snapshot, if any

## Process
1. Read this week's snapshot and last week's (if present).
2. For each competitor/product pair, compute the change: new price, old price,
   absolute and percent delta. Flag new or discontinued listings.
3. Write the change list, largest movement first.

## Outputs
- changes.md -> output/

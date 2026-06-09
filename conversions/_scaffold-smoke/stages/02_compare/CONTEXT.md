# Stage 02 — Compare (Layer 2 contract)

## Inputs
- Layer 4 (working): ../01_collect/output/snapshot.md     # this week's prices
- Layer 4 (working): ../../shared/last-snapshot.md         # the previous run's snapshot, archived here between runs

## Process
1. Read this week's snapshot and last week's (if present).
2. For each competitor/product pair, compute the change: new price, old price,
   absolute and percent delta. Flag new or discontinued listings.
3. Write the change list, largest movement first.

## Outputs
- changes.md -> output/

> `shared/last-snapshot.md` is the prior week's snapshot. Between runs, archive this
> run's `01_collect/output/snapshot.md` to `shared/last-snapshot.md` (a one-line
> local script or manual copy) so next week's compare has a baseline. On the first
> ever run it is absent — treat every product as new.

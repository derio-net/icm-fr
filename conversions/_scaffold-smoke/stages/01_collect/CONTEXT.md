# Stage 01 — Collect (Layer 2 contract)

## Inputs
- Layer 3 (reference): ../../_config/competitors.yaml    # competitors + products to track

## Process
1. Read the competitor + product list.
2. Fetch each competitor's current price per product. This is mechanical — use a
   local script (e.g. `scripts/fetch-prices.py`, not built for this smoke test), not
   agent prose, so runs are deterministic and reproducible.
3. Record a snapshot: competitor, product, price, currency, date observed.

## Outputs
- snapshot.md -> output/

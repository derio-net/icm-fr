# Stage 01 — Collect (Layer 2 contract)

## Inputs
- Layer 3 (reference): ../../_config/competitors.yaml    # competitors + products to track

## Process
1. Read the competitor + product list.
2. For each product, look up the current price from each competitor's listing.
3. Record a snapshot: competitor, product, price, currency, date observed.

## Outputs
- snapshot.md -> output/

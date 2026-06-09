# Competitor-Pricing Digest — Task Routing (Layer 1)

Run all three stages in order weekly. Re-run a single stage to revise.

| Stage | Job | Read its contract |
|-------|-----|-------------------|
| 01_collect | Competitor list → this week's price snapshot | `stages/01_collect/CONTEXT.md` |
| 02_compare | This + last week's snapshot → change list | `stages/02_compare/CONTEXT.md` |
| 03_digest | Change list → weekly digest | `stages/03_digest/CONTEXT.md` |

## Shared resources

- `_config/competitors.yaml` — the competitors + products to track (Layer 3).

# Blog Post Pipeline — Task Routing (Layer 1)

Run both stages in order. To revise after an edit, re-run a single stage — its
inputs declare what it reads, so a change upstream means downstream may be stale.

| Stage | Job | Read its contract |
|-------|-----|-------------------|
| 01_outline | Topic brief → structured outline | `stages/01_outline/CONTEXT.md` |
| 02_draft | Approved outline → finished post in house voice | `stages/02_draft/CONTEXT.md` |

## Shared resources

- `_config/voice.md` — the house voice. Used by `02_draft`.

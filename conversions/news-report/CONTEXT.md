# News Report — Task Routing (Layer 1)

Run all four stages in order for a full report. To revise, re-run a single stage —
its Inputs declare what it reads, so an upstream edit means downstream may be stale.

| Stage | Job | Read its contract |
|-------|-----|-------------------|
| 01_select | Watchlist + today's report → topics to run | `stages/01_select/CONTEXT.md` |
| 02_gather | Run list → live articles per topic | `stages/02_gather/CONTEXT.md` |
| 03_analyze | Articles → per-topic sections (coverage + framing) | `stages/03_analyze/CONTEXT.md` |
| 04_assemble | Sections → final dated report | `stages/04_assemble/CONTEXT.md` |

## Shared resources

- `_config/topics.yaml` — the watchlist (Layer 3). Used by 01 and 02.
- `shared/bias-framework.md` — the 7 framing dimensions (Layer 3). Used by 03.

## Editing the watchlist

The original skill's "Topics mode" was an interactive editor for the watchlist.
In this workspace there is no separate mode: edit `_config/topics.yaml` directly
(every output is an edit surface). The schema is documented at the top of that file.

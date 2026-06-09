# News Report (ICM workspace)

Layer 0 — workspace identity. This workspace produces a multi-source news report
with framing and bias analysis, from a watchlist of topics. Converted from the
willikins `news-report` skill. Every claim must come from a live-retrieved article;
never synthesize from training knowledge.

## Purpose

Run a sequential pipeline over the configured topics and produce a dated report:
per-topic sections (what happened, source-coverage comparison, framing analysis,
attributed evidence), cross-topic intersections, and watchlist suggestions.

## How this workspace works

Run stages in order: `01_select` → `02_gather` → `03_analyze` → `04_assemble`.
For each, read its `CONTEXT.md`, load the inputs it lists, do the process, write the
outputs to its `output/`. Stop for human review at each boundary — the next stage
reads whatever you left.

## Where to find things

- `CONTEXT.md` — Layer 1, the stage routing table.
- `_config/topics.yaml` — Layer 3, the watchlist (the factory; edit to add/remove topics).
- `shared/bias-framework.md` — Layer 3, the 7 framing dimensions used in analysis.
- `stages/NN_*/` — the pipeline.

## Structure

- `01_select` — read the watchlist, drop topics already covered today → run list.
- `02_gather` — discover and fetch live articles for each topic on the run list.
- `03_analyze` — write per-topic sections (coverage comparison + framing analysis).
- `04_assemble` — cross-topic intersections, watchlist suggestions, final report.

> Converted artifact. See `CONVERSION_NOTES.md` for what did not map (Topics Mode,
> Team/parallel mode, headless execution) and the human last-mile.

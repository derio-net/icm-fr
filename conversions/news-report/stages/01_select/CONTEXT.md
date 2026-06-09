# Stage 01 — Select (Layer 2 contract)

## Inputs
- Layer 3 (reference): ../../_config/topics.yaml          # the watchlist
- Layer 4 (working): ../04_assemble/output/today-report.md   # the previous run's report, if any

## Process
1. Read the watchlist. Confirm it has at least one topic; if empty, stop and tell
   the user to configure topics in `_config/topics.yaml`.
2. Incremental check: if a report dated today already exists (the previous run's
   output, read above), parse it for already-covered topic sections (`#### <title>`)
   and remove those topics from the run list. If all topics are already covered, stop
   and say so (unless the user asked to regenerate in full).
3. Write the run list: the topics to process this run, highest priority first.

## Outputs
- run-list.md -> output/

> The live-retrieval fail-fast guard lives in `02_gather`, where retrieval actually
> happens — this stage only reads local files.

# Stage 01 — Select (Layer 2 contract)

## Inputs
- Layer 3 (reference): ../../_config/topics.yaml          # the watchlist
- Layer 4 (working): output/today-report.md               # today's report, if it already exists

## Process
1. Read the watchlist. Confirm it has at least one topic; if empty, stop and tell
   the user to configure topics in `_config/topics.yaml`.
2. Incremental check: if a report for today already exists in `output/`, parse it
   for already-covered topic sections (`#### <title>`) and remove those topics from
   the run list. If all topics are already covered, stop and say so (unless the user
   asked to regenerate in full).
3. Write the run list: the topics to process this run, highest priority first.

## Outputs
- run-list.md -> output/

> Note: the original skill also ran a fail-fast check that the live web-search tool
> is available, hard-stopping rather than fabricating from memory. Keep that guard:
> if no live retrieval is possible, stop here — do not proceed to 02.

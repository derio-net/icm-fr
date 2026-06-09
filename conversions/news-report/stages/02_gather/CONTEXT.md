# Stage 02 — Gather (Layer 2 contract)

## Inputs
- Layer 4 (working): ../01_select/output/run-list.md      # topics to process this run
- Layer 3 (reference): ../../_config/topics.yaml          # per-topic keywords + RSS feeds

## Process
0. **Fail-fast (no fabrication):** confirm live retrieval works — a trivial web
   search returns results. If it does not, stop and do not proceed: a report from
   training knowledge defeats the purpose. Write a one-line cancellation note to
   `output/` for auditability so a scheduled run leaves a trace.
1. For each topic on the run list, discover candidate articles:
   - Fetch the topic's RSS feeds (if any) and keep items whose title or summary
     matches the topic's keywords.
   - Run web searches on the topic's keywords, at least one with a recency signal:
     **2–3 queries if the topic has RSS feeds, 3–4 if it has none.** Skip searches
     that duplicate the RSS hits.
2. Deduplicate by URL. Collapse wire-service reprints to one source. Ignore
   aggregators (note the originating outlet). Target ≥ 4 distinct outlets per topic.
3. Fetch the full text of the 4–5 most relevant articles per topic. Use the local
   fetch helper for speed (parallel HTTP GET): `scripts/fetch.py`. For any article
   that is gated/JS-only/blocked, mark it "snippet only" and use the search/RSS
   summary — continue, do not stop.
4. Write one raw-articles file per topic: outlet, URL, date, author, full text or
   snippet, key quotes.

## Outputs
- articles/<topic-id>.md -> output/

> Every claim downstream must trace to an article gathered here. No memory fallback.

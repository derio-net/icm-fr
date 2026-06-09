# Stage 04 — Assemble (Layer 2 contract)

## Inputs
- Layer 4 (working): ../03_analyze/output/sections/       # per-topic sections
- Layer 3 (reference): references/report-skeleton.md      # the final report shape

## Process
1. Read every per-topic section.
2. **Cross-topic intersections** — if two or more topics genuinely intersect in
   today's coverage, write 2–4 attributed sentences. Omit the section if none.
3. **Watchlist suggestions** — 3–5 suggestions drawn only from signals that appeared
   in today's gathered articles (co-appearing topics, recurring adjacent stories).
   Each: topic name, the signal that flags it, type (`adjacent` | `emerging`).
4. Assemble the final report per report-skeleton.md, dated today. If today's report
   already existed (incremental run), append new sections before Cross-Topic
   Intersections and regenerate those two sections from all sections.

## Outputs
- today-report.md -> output/

> The next run's `01_select` reads this file (the previous report) for its
> incremental check. Each stage writes only its own `output/`; there is no
> cross-stage copy-back.

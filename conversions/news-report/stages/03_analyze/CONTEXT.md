# Stage 03 — Analyze (Layer 2 contract)

## Inputs
- Layer 4 (working): ../02_gather/output/articles/        # raw articles per topic
- Layer 3 (reference): ../../shared/bias-framework.md     # the 7 framing dimensions
- Layer 3 (reference): references/section-format.md       # the per-topic section template

## Process
For each topic, write a section following section-format.md:
1. **What happened** — 2–3 sentences, inline attribution, only what articles confirm.
2. **Coverage comparison** — a table: source | frame (3–5 words) | emphasized |
   downplayed/absent.
3. **Framing analysis** — 3–5 observations, each naming a dimension from
   bias-framework.md and quoting specific revealing text. Describe the choice, not
   "outlet X leans Y".
4. **Evidence summary** — each claim attributed to (outlet, date).

## Outputs
- sections/<topic-id>.md -> output/

> The original skill optionally parallelised this per topic (one teammate each).
> That is an execution optimisation, not part of the workspace: process topics in
> any order; the contract is identical per topic. See CONVERSION_NOTES.md.

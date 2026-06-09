# Setup Questionnaire — Competitor-Pricing Digest

Answer once, at setup. Your answers populate `_config/` (the factory); every weekly
run inherits them. (This is a smoke-test workspace, so the canned answers from the
generating interview are shown in brackets.)

1. **Which competitors do you track?** Name + listing URL for each.
   → `_config/competitors.yaml` › `competitors`
   [Acme Co, Globex]
2. **Which products do you compare across them?**
   → `_config/competitors.yaml` › `products`
   [widget-standard, widget-pro]
3. **What currency / region should prices be normalised to?**
   [not set for the smoke test]
4. **What change is worth highlighting?** (e.g. any move ≥ 5%, or top 5 by size)
   → drives the digest in stage 03
   [top 3–5 moves by size]

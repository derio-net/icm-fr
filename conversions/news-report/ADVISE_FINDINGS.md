# Advise Findings — news-report workspace

Produced by following `procedures/advise.md`. Non-generative review; the workspace
was not edited. Date: 2026-06-09.

## Step 1 — Structural pass (validator)

`python3 icm-core/validate.py conversions/news-report` → **exit 0, no findings.**
AGENTS.md, root CONTEXT.md, all 3 shims, four contiguous stages each with the three
contract sections — all present.

## Step 2 — Judgment pass

### Suggestions

1. **`02_gather` does two jobs** (discover candidate articles *and* fetch full text).
   *severity: suggestion.* This was a deliberate conversion choice (recorded in
   CONVERSION_NOTES judgment call #1) because the original ran them back-to-back. If
   you want a human review gate on the candidate URL list *before* spending fetches —
   e.g. to prune low-quality sources — split into `02_discover` → `03_fetch`
   (renumbering downstream). Otherwise leave as is; the combine is defensible.

2. **`04_assemble` carries three sub-jobs** (cross-topic intersections, watchlist
   suggestions, final assembly). *severity: suggestion.* Borderline against "one
   stage, one job". They share one input (the per-topic sections) and produce one
   deliverable, so a single stage is reasonable — but if the suggestions step grows,
   it is the natural thing to peel into its own stage.

### Informational

3. **Lost capability: Browser Mode.** *severity: informational (already recorded).*
   The original's JS/login-walled fetch path is not reproduced; gated pages degrade to
   "snippet only" (CONVERSION_NOTES "Did not map"). Not a workspace defect — a
   documented scope cut. Flagged here so a reviewer of the workspace alone (without
   the gap report) still sees it.

### Note — cross-run carry-over (by design, but call it out)

4. **`01_select`'s only per-run input is a cross-run carry-over**, not a run brief.
   It reads `../04_assemble/output/today-report.md` — the *previous run's* report — to
   skip already-covered topics. *severity: informational.* It is a legitimate
   `(working)` input (real producer: 04's `output/`, from the prior run) and is
   **absent on the first run**, where the contract correctly treats it as a fresh run.
   Worth naming because it is the fragile input: this pipeline is trigger-driven (by
   date), so there is no user brief, and a reviewer should confirm the first-run
   behaviour is handled — it is. Not a defect.

### Clean on

- **Layer 3 / Layer 4 tagging** — every input is correctly tagged (incl. the
  cross-run carry-over in finding 4).
- **No dangling working inputs** — every `(working)` path resolves to a producer
  (within-run `output/`, `shared/`, or the cross-run carry-over).
- **No cross-stage writes** — each stage writes only its own `output/` (the 02
  cancellation stub writes to 02's own `output/`).
- **Harness neutrality** — no contract names a search tool, browser harness, or
  agent/model.
- **Context scope** — no stage loads reference it does not use; `topics.yaml` appears
  in 01 and 02 because both genuinely use it (the list vs the per-topic keys).

## Verdict

Structurally clean; two stage-granularity suggestions and two informational notes (a
documented capability cut and the cross-run carry-over). Nothing requiring a fix
before use. The suggestions are exactly the kind of "stage 1" direction-setting edit
the methodology expects a human to make.

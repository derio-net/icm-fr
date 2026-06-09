# Mode: advise

Review an existing ICM workspace against the methodology and report findings.
**Non-generative** — this mode reads and judges; it does not modify the workspace's
contracts, outputs, or structure. Its output is a findings report: return it to the
user, or save it as a clearly-named review note (e.g. `ADVISE_FINDINGS.md`) that
sits alongside the workspace and is not part of the pipeline. Never edit the stage
contracts or outputs you are reviewing.

## Preamble — load the methodology (Layer 3)

Read first, every time:

- `icm-core/principles.md` — the 5 principles + 5-layer hierarchy + factory/product.
- `icm-core/conventions.md` — folder layout, stage-contract format, enforced vs
  documented rules.
- `icm-core/portability.md` — the harness shim registry (to judge shim completeness
  and the harness-neutrality rule).

## Step 1 — Structural pass (mechanical)

Run `python3 icm-core/validate.py <workspace>`. Every error it reports is a finding,
already located and explained. This covers the structural floor (AGENTS.md, root
CONTEXT.md, shims, at-least-one-stage, the three contract sections, contiguous
numbering). Do not re-derive these by hand — let the validator find them.

## Step 2 — Judgment pass (what the validator cannot check)

Read every stage contract and the reference layout. Check for the line-level and
design issues the validator does not see:

- **One stage, one job.** Does any stage do two jobs (e.g. fetch *and* analyse)?
  That is a split waiting to happen.
- **Layer 3 / Layer 4 mixing.** Are stable reference inputs and per-run working
  inputs both present but untagged or mis-tagged? Is the run brief tagged
  `(working)`, not `(reference)`?
- **Dangling working inputs.** Does every `(working)` input name a real producing
  location — a prior stage's `output/`, a `shared/` carry-over, the run brief, or a
  **cross-run carry-over** (a prior run's output, e.g. an incremental pipeline that
  reads last run's result; legitimately `(working)`, may be absent on the first run
  and the contract should say what happens then) — and not a bare filename nothing
  writes? Flag any `(working)` input whose producer you cannot point to.
- **Cross-stage writes.** Does any stage's Outputs write into another stage's folder?
  Each stage writes only its own `output/`.
- **Harness leakage.** Does any contract name a harness or tool (a specific search
  tool, a browser harness, an agent/model name)? Contracts must be neutral.
- **Context bloat.** Does a stage load reference files it does not use in its Process?
  Trim to what the stage needs. (A reference used by *several* stages is fine — that
  is what `shared/` and repeated `_config/` references are for; bloat is a file *this*
  stage's Process never touches.)
- **Missing review gate.** Are two transformations crammed into one stage with no
  reviewable artifact between them?
- **Mechanical work in prose.** Is deterministic work (fetch, format, move) described
  as agent prose instead of a local script?

## Step 3 — Report

Output a findings list. Saving it as a review note beside the workspace is fine;
modifying the workspace's contracts or outputs is not. For
each finding: **severity** (error / warning / suggestion), **location**
(stage + line or file), and a **concrete fix**. Lead with the validator's structural
errors, then the judgment findings. If the workspace is clean, say so plainly and
name what you checked.

> `advise` and `convert`/`scaffold` share the same rule set from opposite ends:
> the generators produce workspaces that should pass `advise`; `advise` is the check
> that they did. The canonical `icm-core/example/` workspace should be near-clean.

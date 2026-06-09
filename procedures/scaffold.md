# Mode: scaffold

Build a new ICM workspace from scratch, interview-driven. Same generation engine as
`convert`, but instead of ingesting an existing artifact you interview the user to
discover the workflow. Output bar: a complete, validator-clean workspace whose stage
contracts capture the intended pipeline, ready for the user's first-run setup.

## Preamble — load the methodology (Layer 3)

Read first, every time:

- `icm-core/principles.md` — the 5 principles + 5-layer hierarchy + factory/product.
- `icm-core/conventions.md` — folder layout, stage-contract format, enforced vs
  documented rules.
- `icm-core/portability.md` — the harness shim set every workspace must emit.

## Step 1 — Discovery (interview)

Ask the user, one topic at a time. Keep it short — you are mapping a pipeline, not
gathering requirements for a framework. Cover:

- **Domain & deliverable** — what does this workspace produce, each run? (a report,
  a video, a slide deck, a draft…)
- **The workflow** — what are the steps, in order, from input to deliverable?
- **Review points** — at which step boundaries does a human want to check and edit?
- **Stable vs per-run** — what stays the same every run (voice, brand, structure,
  conventions → Layer 3) versus what changes each run (the input, the topic → Layer 4)?
- **Mechanical work** — any steps that need no AI (fetch, format, send) → local scripts.

## Step 2 — Stage mapping

Turn the workflow into stages at the natural review boundaries ("one stage, one
job"). Each step that transforms input → reviewable output is a stage. Fold purely
mechanical work into local scripts a stage calls. Name the stages `NN_slug`,
contiguous from `01`. Confirm the stage list with the user before emitting.

## Step 3 — Emit the workspace

Copy `icm-core/templates/workspace/` to the output path and fill it in:

1. `AGENTS.md` — Layer 0: name, purpose, the stage list, where to find things.
2. `CONTEXT.md` — Layer 1: the stage-routing table.
3. The 3 shims come from the template unchanged (do not edit them).
4. For each stage, copy `icm-core/templates/stage/` to `stages/NN_slug/` and write
   its `CONTEXT.md` contract: `## Inputs` (each line tagged `(reference)` or
   `(working)`), `## Process`, `## Outputs` (`name -> output/`). Name no harness.
5. Place any Layer 3 reference the user already has in `_config/`/`shared/`. Leave
   stage `references/` for stage-scoped reference.

## Step 4 — Questionnaire design

Adapt `setup/questionnaire.md` (template stub) into the real first-run questions for
*this* workspace — the answers that populate `_config/` (the factory). This is where
"configure the factory, not the product" lives: the user answers once, every run
inherits it. Do not leave the stub unchanged.

## Step 5 — Validate

Run `python3 icm-core/validate.py <output-path>`. Fix the **output** until it exits
0. The validator checks structure only — self-check the Inputs `(reference)`/
`(working)` tagging and Outputs format by hand, and confirm the first stage's run
brief (if any) is tagged `(working)`. Then hand the workspace to the user to fill in
`_config/` via the questionnaire and run stage 01.

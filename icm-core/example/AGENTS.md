# Blog Post Pipeline (ICM example)

Layer 0 — workspace identity. This is a minimal, correct ICM workspace that turns a
topic into a short published blog post in two reviewed stages. It is the canonical
reference: the shape `templates/` produces, the thing `advise` measures against,
and a worked tutorial for reading ICM.

## Purpose

Take a one-line topic brief and produce a ~600-word blog post in the house voice,
with a human review gate after the outline and after the draft.

## How this workspace works

- Run stages in order: `01_outline` → `02_draft`.
- For each stage, read its `CONTEXT.md`, load the `## Inputs` it lists, do the
  `## Process`, write `## Outputs` into that stage's `output/`.
- Stop for human review at each boundary. The next stage reads whatever the human
  left in the previous `output/`.

## Where to find things

- `CONTEXT.md` — Layer 1 routing.
- `stages/01_outline/`, `stages/02_draft/` — the pipeline.
- `_config/voice.md` — Layer 3, the house voice (the factory; stable across runs).

## Structure

- `01_outline` — turn the topic brief into a structured outline.
- `02_draft` — turn the approved outline into a finished post in the house voice.

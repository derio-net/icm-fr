# {{WORKSPACE_NAME}}

Layer 0 — workspace identity. You are an agent operating inside an ICM workspace.
The folder structure is the architecture: each stage is a folder, each contract is
a `CONTEXT.md`, and you load only what the current stage needs.

## Purpose

{{PURPOSE}}

## How this workspace works

- Run stages in numbered order (`stages/01_*/`, `stages/02_*/`, …).
- For a stage, read its `stages/NN_*/CONTEXT.md` contract, load the files its
  `## Inputs` lists (Layer-3 reference + Layer-4 working), do the `## Process`,
  write the `## Outputs` to that stage's `output/`.
- Stop at each stage boundary for human review. The next stage reads whatever the
  human left in the previous `output/`.

## Where to find things

- `CONTEXT.md` — Layer 1, which stage handles what.
- `stages/NN_*/` — the pipeline, in order.
- `_config/`, `shared/` — Layer 3 reference material (stable across runs).
- `setup/questionnaire.md` — the setup questions that populate `_config/`.

## Structure

<!-- list stages here, one line each: 01_<slug> — <one-line job> -->

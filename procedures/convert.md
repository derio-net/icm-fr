# Mode: convert

Turn an existing artifact (a skill, a ruleset, a plugin) into an ICM workspace,
plus an honest gap report. Output bar (D6): **faithful structure, human finishes** —
a complete, correct folder tree with stage contracts that capture the artifact's
intent, plus a `CONVERSION_NOTES.md` flagging what needs human attention. Not
required: behaviour-identical reproduction.

## Preamble — load the methodology (Layer 3)

Read first, every time:

- `icm-core/principles.md` — the 5 principles + 5-layer hierarchy + factory/product.
- `icm-core/conventions.md` — folder layout, stage-contract format, enforced vs
  documented rules.
- `icm-core/portability.md` — the harness shim set every workspace must emit.

## Step 1 — Ingest

Read the whole target. For a skill: its `SKILL.md` (or entrypoint), every helper
script, and any rules/config it references. Build a mental model of: what it takes
as input, what it produces, and the sequence of transformations in between.

## Step 2 — Decompose & classify

Identify the natural **sequential breakpoints** — the points where one step's
output is reviewed before the next begins. Each becomes a stage ("one stage, one
job"). Then classify **every piece** of the original into exactly one of:

| Class | What it is | Where it lands |
|-------|-----------|----------------|
| **stage** | A step that does work (transforms input → output) | `stages/NN_slug/` |
| **Layer 3 reference** | A stable rule, voice guide, template, config | `_config/`, `shared/`, or a stage's `references/` |
| **Layer 4 working** | Per-run material (the run brief, fetched data, prior output) | a stage's `output/` |
| **local script** | Mechanical work needing no AI (fetch, move, format) | a plain script invoked by a stage |

**What does NOT map — surface, never drop.** ICM is sequential and human-reviewed.
These have no clean ICM home; record each in the gap report (Step 4):

- **Event-driven hooks** — triggers, not steps. They fire on events, not in
  sequence. An ICM stage cannot represent "run when X happens."
- **AI-driven mid-pipeline branching** — a stage that picks its own next stage.
  ICM allows a *human* to branch between stages, not the agent.
- **Concurrent / real-time agent coordination** — outside ICM's fit envelope.

## Step 3 — Emit the workspace

Copy `icm-core/templates/workspace/` to the output path and fill it in:

1. `AGENTS.md` — Layer 0: name, purpose, the stage list, where to find things.
2. `CONTEXT.md` — Layer 1: the stage-routing table.
3. The 4 shims come from the template unchanged (do not edit them).
4. For each stage, copy `icm-core/templates/stage/` to `stages/NN_slug/` and write
   its `CONTEXT.md` contract: `## Inputs` (each line tagged `(reference)` or
   `(working)`), `## Process`, `## Outputs` (`name -> output/`). Name no harness.
5. Place Layer 3 reference files in `_config/`/`shared/`/`references/`. Seed any
   obvious Layer 4 run input under the first stage if the original implies one.

## Step 4 — Gap report

Write `CONVERSION_NOTES.md` at the workspace root with these sections:

- **Acceptance** — fill the checklist (see below) once Step 5 passes.
- **Did not map** — every hook / branch / concurrency item from Step 2, and why.
- **Judgment calls** — every non-mechanical decision you made (where you put a
  breakpoint, how you classified an ambiguous piece).
- **Human last-mile** — the edits a person should make before first run (the
  paper's U-shaped "stage 1" direction-setting work).

## Step 5 — Validate

Run `python3 icm-core/validate.py <output-path>`. Fix the **output** until it exits
0 (never weaken the validator to pass). Then complete the Acceptance checklist:

- [ ] Correct numbered stages, each with a complete Inputs/Process/Outputs contract.
- [ ] Every original piece classified (stage / L3 / L4 / script) or listed in
      "Did not map".
- [ ] `AGENTS.md` + all 4 shims present (validator-confirmed).
- [ ] Gap report names every judgment call and unmapped piece.

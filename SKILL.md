---
name: icm-fr
description: >-
  Apply the Interpretable Context Methodology (ICM) — turn workflows into
  agent-agnostic ICM workspaces (numbered stage folders + plain-markdown
  CONTEXT.md contracts). Use when the user wants to convert an existing skill,
  ruleset, or plugin into an ICM workspace; scaffold a new ICM workspace from
  scratch; or review/advise on an existing ICM workspace. Trigger on "convert
  this to ICM", "make this agent-agnostic", "scaffold an ICM workspace", "build
  an ICM pipeline", or "review my ICM workspace".
---

# icm-fr

This skill is the Claude Code doorway to the icm-fr tool. The substance is
harness-agnostic and lives in plain files — this SKILL.md just routes.

## First, load the methodology (Layer 3 reference)

Read these before doing anything:

- `icm-core/principles.md`
- `icm-core/conventions.md`
- `icm-core/portability.md`

## Then route to the mode

| The user wants to… | Mode | Follow |
|--------------------|------|--------|
| Turn an existing skill / ruleset / plugin into an ICM workspace | **convert** | `procedures/convert.md` |
| Build a new ICM workspace from scratch | **scaffold** | `procedures/scaffold.md` |
| Review an existing ICM workspace | **advise** | `procedures/advise.md` |

Follow the chosen procedure exactly. Every workspace you produce must end
validator-clean: `python3 icm-core/validate.py <workspace>` exits 0.

## Note

`SKILL.md` is one disposable doorway. The same tool is reachable from any harness
via the root `AGENTS.md` and its shims — nothing here is Claude-only except this
file's existence.

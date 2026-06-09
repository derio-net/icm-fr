# icm-fr — tool entrypoint (Layer 0)

You are operating the **icm-fr** tool. It applies the Interpretable Context
Methodology (ICM): it turns workflows into agent-agnostic ICM workspaces — plain
folders of markdown any file-reading agent can run.

## What this tool does — three modes

Pick the mode that matches the request, then follow its procedure verbatim.

| Mode | When | Procedure |
|------|------|-----------|
| **convert** | Turn an existing skill / ruleset / plugin into an ICM workspace | `procedures/convert.md` |
| **scaffold** | Build a new ICM workspace from scratch (interview-driven) | `procedures/scaffold.md` |
| **advise** | Review an existing ICM workspace against the methodology | `procedures/advise.md` |

## Before any mode

Load the methodology as reference (Layer 3):

- `icm-core/principles.md` — the 5 principles + 5-layer hierarchy + factory/product.
- `icm-core/conventions.md` — folder layout, the stage-contract format, naming.
- `icm-core/portability.md` — the harness shim registry (every workspace emits it).

## Key facts

- Layer 0 of a generated workspace is **`AGENTS.md`**, not `CLAUDE.md` — for
  portability. Harness shims redirect to it.
- Validate any workspace you produce: `python3 icm-core/validate.py <workspace>`
  (exit 0 = clean). `scaffold` and `convert` must end validator-clean.
- `icm-core/example/` is the canonical, correct reference workspace.
- The paper this implements is in `source/` (arXiv:2603.16021, MIT).

# Portability & the Harness Shim Registry

ICM workspaces are agent-agnostic by construction: the substance lives in plain
markdown, and **`AGENTS.md` is the single Layer-0 file with real content**. Every
other entrypoint is a one-line shim that redirects to it. Any agent that can read
a folder can run the workspace — no skill ingestion required.

Both the icm-fr tool itself and every workspace it generates draw their shim set
from this registry.

## The canonical shim set

| File | Harness | Role | Status |
|------|---------|------|--------|
| `AGENTS.md` | Codex + generic | **Canonical Layer-0 content** | active |
| `CLAUDE.md` | Claude Code | redirect → AGENTS.md | active |
| `GEMINI.md` | Gemini CLI | redirect → AGENTS.md | active |
| `.github/copilot-instructions.md` | GitHub Copilot | redirect → AGENTS.md | active |
| `<tbd>` | Pi | redirect → AGENTS.md | verify-convention-first |
| `<tbd>` | Antigravity | redirect → AGENTS.md | verify-convention-first |
| `AGENTS.md` (native) | Hermes | redirect → AGENTS.md | verify-convention-first |

The four `active` rows are the conventions confident as of 2026-06. The
`verify-convention-first` rows are **not emitted** — they are placeholders so the
next person knows where to slot them in.

## The redirect template

Every shim contains exactly one short instruction (no workspace content):

```
This workspace uses AGENTS.md as its entrypoint.
Read ./AGENTS.md and follow it.
```

Because there is nothing but a redirect, there is nothing to drift: workspace
content has exactly one home.

## Adding a harness

1. Confirm the harness's instruction-file convention from primary docs (do **not**
   guess from naming). Note the exact filename and path.
2. Add a row to the table above, status `active`.
3. Add the filename to `DEFAULT_SHIMS` in `validate.py` **and** a fixture case in
   `test_validate.py`; run the tests.
4. Add the file to `templates/workspace/` so new workspaces emit it.
5. The validator will now require it in every workspace — which is the point.

> Keep `validate.py:DEFAULT_SHIMS` and the `active` rows here identical. The
> validator is the enforcement; this file is the spec.

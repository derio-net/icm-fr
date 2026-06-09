# icm-fr

Apply the **Interpretable Context Methodology (ICM)** — turn sequential,
human-reviewed, repeatable workflows into **agent-agnostic ICM workspaces**: plain
folders of markdown that any file-reading agent (Claude Code, Codex, Gemini CLI,
Copilot, …) can run. The folder structure replaces the framework.

ICM is the work of Jake Van Clief & David McDermott (University of Edinburgh),
*Folder Structure as Agent Architecture*, arXiv:2603.16021, MIT-licensed. The paper
and a visual guide are in [`source/`](source/). This repo is an implementation, not
the paper.

## Three modes

- **convert** — turn an existing skill / ruleset / plugin into an ICM workspace,
  plus an honest gap report of what didn't map cleanly. → `procedures/convert.md`
- **scaffold** — interview-driven generation of a new ICM workspace from scratch.
  → `procedures/scaffold.md`
- **advise** — review an existing ICM workspace against the methodology.
  → `procedures/advise.md`

## Why agent-agnostic

A workspace's only Layer-0 file with real content is `AGENTS.md`; `CLAUDE.md`,
`GEMINI.md`, and `.github/copilot-instructions.md` are one-line redirects to it.
Stage contracts name no harness. So a workspace built here runs anywhere. The
registry of supported harnesses lives in
[`icm-core/portability.md`](icm-core/portability.md).

## Layout

```
AGENTS.md + shims + SKILL.md   entrypoints (the tool's own doorways)
icm-core/                      the portable substance
  principles.md conventions.md portability.md   the methodology
  validate.py  test_validate.py                 the structural validator (lint)
  templates/                                     workspace + stage skeletons
  example/                                       a canonical, correct workspace
procedures/                    convert · scaffold · advise (documented procedures)
source/                        the ICM paper + visual guide
```

## Validate a workspace

```
python3 icm-core/validate.py <workspace>   # exit 0 = structurally clean
python3 icm-core/test_validate.py          # the validator's own tests
```

## License

MIT — see [LICENSE](LICENSE). Matches the upstream ICM license.

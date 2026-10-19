# icm-fr upstream parity: forms, richer contracts, restructure mode — Design Spec

*Date: 2026-10-19 · Status: Draft*

## Summary

icm-fr implements ICM (Van Clief & McDermott, arXiv:2603.16021v2, MIT) as a
pipeline-only tool. The upstream method repository
(`github.com/RinDig/Interpretable-Context-Methodology`, `_core/CONVENTIONS.md`,
MIT) and the upstream builder skill (`github.com/RinDig/icm-architect`, MIT) have
since moved well past what icm-fr encodes: table-shaped stage contracts with
section-level loading, optional Checkpoints and Audit sections, fifteen named
conventions, a placeholder-driven setup flow, and six workspace *forms* of which
the pipeline is only one. This spec brings icm-fr level with upstream, adds a
fourth mode (`restructure`), makes the validator form-aware, sharpens `scaffold`
and `advise` with an audit-first discovery interview and a set of maintenance
checks, and adds CI.

Every word added to the repo is written fresh. Upstream rules are paraphrased and
cited to the upstream repo or the paper. Ideas that came from studying free
community course material are restated in original prose with no quotation,
tables, or files carried over from it.

## Background: the gap

Diffing icm-fr against upstream (fetched 2026-10-19):

| Area | Upstream | icm-fr today |
|---|---|---|
| Inputs | table: source, file, section/scope, why | tagged bullet list, whole files only |
| Outputs | table: artifact, location, format | `name -> output/` bullets |
| Optional contract sections | Checkpoints, Audit | none |
| Conventions | 15 named patterns + guardrails | ~6 rules |
| Setup | `{{PLACEHOLDER}}` fill, conditional sections, `setup`/`status` triggers | questionnaire stub only |
| Workspace forms | pipeline, umbrella, record library, knowledge bundle, context map, system map | pipeline only (validator errors without `stages/`) |
| Modes | build, restructure (with reference-integrity gate), walk test | convert, scaffold, advise |
| Stage naming | `01-name` | `01_name` |

The paper itself also proposes a `Verify` section (§6.2) and the edit-source
principle (§6.3), neither of which icm-fr mentions.

## Decisions (from brainstorming, 2026-10-19)

1. **All six forms** are supported: conventions, templates, validator, advise.
2. **Tables are canonical; list-form contracts still validate, with a warning.**
   In-repo workspaces migrate to tables.
3. **New modes/features:** `restructure` mode; `setup` + `status` triggers with
   placeholder checks; audit-first `scaffold` discovery.
4. **Stage naming switches to `NN-slug`** (hyphen), matching upstream. Underscore
   stage folders become a validator error with a rename hint. In-repo workspaces
   migrate.
5. **Bundled `skills/` adopted** as harness-neutral Layer 3 reference.
6. **Guardrails as validator warnings:** size limits and the no-em-dash rule.
7. **Verification:** test fixtures plus a new GitHub Actions workflow.
8. Layer 0 stays `AGENTS.md` with shims (icm-fr's one deliberate departure).
9. One spec, one PR, phased by layer.

## Requirements

R1. Stage contracts use an Inputs table with columns Source, File/Location, Section/Scope, Why, and an Outputs table with columns Artifact, Location, Format; "Full file" is the explicit whole-file scope.
R2. The validator accepts the legacy tagged-list Inputs/Outputs form but emits a warning naming the stage and pointing to the table form.
R3. A stage contract may carry optional `## Checkpoints` (After Step, Agent Presents, Human Decides), `## Audit` (Check, Pass Condition, plus an attempt budget), `## Verify` (earlier output to re-read, criterion) and `## Human check` sections; the validator checks each present section's table shape.
R4. An Audit section states a maximum number of revision attempts; when the budget runs out the agent hands back the best attempt together with every check's result, and every attempt is judged against the original checks.
R5. A stage contract may carry a "Do not load" line naming material an eager agent would wrongly pull in.
R6. Stage folders are named `NN-slug`, two-digit, contiguous from 01; an underscore-separated stage folder is a validator error whose message gives the hyphen name.
R7. `conventions.md` states, in original wording with upstream citations, the conventions: one-way cross-references, selective section routing, canonical sources (one home per fact), CONTEXT.md as routing not content, tool prerequisites, bundled skills, specs as contracts, checkpoints, audits, value validation, docs over outputs, shared constants, and recursive routing inside large reference collections.
R8. A `(working)` input that points at a stage's `output/` must point at an earlier stage (or be declared a cross-run carry-over); the validator errors on a forward or self reference.
R9. An Outputs location outside the stage's own `output/` is a validator error.
R10. A reference folder (`_config/`, `shared/`, `skills/`, a design-system folder) that links into a stage folder is a validator warning (one-way references).
R11. `principles.md` adds the ten structural invariants, the edit-source principle and the U-shaped intervention pattern, each tied to the paper or upstream.
R12. A new `forms.md` describes the six forms (pipeline, umbrella, record library, knowledge bundle, context map, system map): how to choose by the repeating unit, each form's skeleton, defining moves, failure modes, and how forms nest.
R13. A workspace declares its form in `AGENTS.md` YAML front matter (`form: <name>`); a missing declaration is treated as `pipeline` with a warning; an unknown form is an error.
R14. Umbrella workspaces are validated recursively: each child pipeline is a full workspace with its own `AGENTS.md`, and a child that references a sibling child is a warning.
R15. Record-library workspaces must have a record template folder and an index log; a record whose file set differs from the template is a warning.
R16. Knowledge-bundle and context-map workspaces must have a schema file listing node types; a note whose front-matter `type` is missing or not in the schema is a warning; an unresolved link is informational only.
R17. System-map workspaces must have `map/` with a catalog, `CONTEXT.md`, schema and object index; an empty `processes/` or `effects/` folder is an error; a card marked `verified` without a citation and a date is an error.
R18. The validator warns on leftover `{{PLACEHOLDER}}` tokens, and errors on them when run with `--post-setup`; a malformed conditional section (`{{?NAME}}` without matching `{{/NAME}}`, or one not wrapping whole sections) is an error.
R19. The validator warns when a CONTEXT.md exceeds 80 lines, a reference file exceeds 200 lines, or the Layer-0 entry file exceeds 60 lines, and when any workspace markdown file contains an em dash.
R20. The validator warns when an identical non-trivial line appears in more than one Layer-3 file (duplicate-fact smell) and when a folder meant to persist is empty without a `.gitkeep`.
R21. The validator offers `--json` output listing every finding with level, code, path and message.
R22. A `status.py` script prints a pipeline diagram marking each stage COMPLETE (output files present, listing them) or PENDING.
R23. Generated workspaces recognise a `setup` trigger (run the questionnaire, fill placeholders, confirm none remain) and a `status` trigger (run or emulate `status.py`), described in their `AGENTS.md`.
R24. The questionnaire template follows upstream's design rules (flat, all at once, system-level only, derive don't ask, defaults, ask once, examples over descriptions), and each question names its placeholder, target files and type.
R25. A new `discovery.md` drives `scaffold`'s interview: who the output is for and what they do next, where information comes from and what breaks, a split between thinking/data, existing tools and AI, and an impact-by-risk score whose result sets how many review gates the workspace gets.
R26. `scaffold` and `convert` choose a form via `forms.md` before emitting, emit table contracts, and add Checkpoints/Audit where the stage is creative or produces binding, external or depended-upon output.
R27. A new `restructure` mode (`procedures/restructure.md`) turns an existing folder into an ICM workspace in place: inventory without moving, classify every file as catalog, contract, factory, product or dead, check every referrer (in-tree, relative, symlink, external) and case-folded destination collisions, propose a migration map for approval, then copy, verify parity, and only then remove, sending dead files to `_archive/`.
R28. `advise` adds: the cold walk test, a fresh-session orientation test, a "could a person do this without the AI" test, gate placement (after checkable work, before irreversible actions), dates and sources on facts that can expire, a corrections log where a fix made twice signals a missing check, `_archive/` hygiene, and the upstream patterns from R7; it consumes the validator's `--json` output.
R29. `portability.md` adds an enforcement ladder for irreversible actions (contract prose, harness permission settings, harness hooks) mapped per active harness, keeping stage contracts harness-neutral.
R30. Templates ship for every form (stage contract, record template, index log, node, object card, process card, schema, questionnaire) and the workspace template includes `_archive/` and `skills/` placeholders.
R31. `icm-core/example/` (pipeline) is migrated to hyphens and tables with one Checkpoint and one Audit, and a minimal canonical example ships for each other form; every example validates with no errors.
R32. `conversions/news-report` and `conversions/_scaffold-smoke` are migrated to the new conventions, validate with no errors, and news-report gets a fresh advise report.
R33. `AGENTS.md`, `SKILL.md` and `README.md` describe four modes and the forms, and the README credits the upstream repositories (MIT).
R34. A `.gitignore` excludes `__pycache__/` and `.DS_Store`, and the tracked `.pyc` is removed.
R35. A GitHub Actions workflow runs `test_validate.py` and validates every in-repo workspace (`icm-core/example*`, `conversions/*`) on every pull request and push to main, and `.devcontainer/fr-profiles.yaml` declares `ci: github-actions`.
R36. No course text, tables or files are copied into the repo; all new prose is original.

## Design

### Architecture

```
icm-core/
  principles.md     + invariants, edit-source, U-curve           (R11)
  conventions.md    rewritten: tables, optional sections, patterns (R1-R10, R18-R20, R23)
  forms.md          NEW: six forms                                (R12)
  discovery.md      NEW: audit-first interview                    (R25)
  portability.md    + enforcement ladder                          (R29)
  validate.py       form-aware validator, --json, --post-setup    (R2-R21)
  status.py         NEW: pipeline status diagram                  (R22)
  test_validate.py  fixtures per rule and per form
  templates/        stage/, workspace/, forms/<form>/, questionnaire (R24, R30)
  example/          pipeline example, migrated                    (R31)
  examples/<form>/  NEW: minimal example per non-pipeline form    (R31)
procedures/ convert.md scaffold.md advise.md restructure.md(NEW)  (R26-R28)
.github/workflows/ci.yml  NEW                                     (R35)
```

### Validator design

`validate_workspace(path, post_setup=False) -> list[Finding]` keeps its signature
(plus the keyword). `Finding` gains `path`. Levels: `error`, `warn`, `info`.
Exit 1 on any error.

Flow: read `AGENTS.md` front matter → resolve form → run **common checks**
(Layer 0/1 files, shims, placeholders, conditional sections, guardrails,
duplicate-fact smell, `.gitkeep`) → dispatch to the **form checker**. The
umbrella checker calls `validate_workspace` on each child and prefixes child
paths. Front matter is parsed with a minimal stdlib reader (`key: value` lines
between `---` fences) to keep the validator dependency-free.

Contract parsing: a section body is either a markdown table (header row,
separator row, data rows) or a bullet list. Tables are checked for the required
columns (case-insensitive header match). Lists trigger `LEGACY_LIST_CONTRACT`
(warn) and are checked by the existing tag rules. Path rules (R8, R9) resolve
backtick-quoted relative paths from the stage folder; template placeholders in
paths (`[topic-slug]`) are matched as wildcards.

Stage folder regex becomes `^(\d{2})-[a-z0-9][a-z0-9-]*$`; a folder matching
`^\d{2}_` raises `UNDERSCORE_STAGE` with the suggested hyphen name.

New finding codes are listed in `conventions.md` under "Enforced by validate.py",
and that list stays the single record of what is enforced.

### Contract format

```markdown
## Inputs
| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Previous stage (working) | `../01-outline/output/outline.md` | Full file | The approved outline |
| Config (reference) | `../../_config/voice.md` | "Rules" through "Avoid" | Tone |

Do not load: other stages' references, earlier runs.

## Process
1. ...

## Checkpoints
| After Step | Agent Presents | Human Decides |

## Audit
| Check | Pass Condition |
Budget: 3 attempts, then hand back the best attempt with every check's result.

## Outputs
| Artifact | Location | Format |
```

The `(working)` / `(reference)` tag moves into the Source column, so the Layer
3 / Layer 4 split stays visible.

### Forms

`forms.md` gives each form a selection test (the repeating unit), skeleton,
defining moves and failure modes, written in original prose and cited to
`icm-architect/references/forms.md`. The validator's per-form minimums are the
mechanical subset (R14-R17); everything else is advise-level.

### Procedures

- `scaffold`: discovery.md → form choice → stage/node mapping → emit → questionnaire → validate.
- `convert`: ingest → form choice → classify → emit tables → gap report → validate.
- `restructure`: inventory → classify (five roles) → reference integrity → propose → copy/verify/remove → walk test → validate.
- `advise`: `validate.py --json` → judgment pass (R28) → report.

### Migration

Renames use `git mv` so history follows. In-repo workspaces lose em dashes
(replaced with commas, colons or parentheses as reads best). The news-report
advise report is regenerated and dated.

## Verification

strategy: none

Mechanical rows are proved by `test_validate.py` fixtures (a passing and a
failing case per rule) and by validating every in-repo workspace, both run by the
new CI workflow on the PR. Prose rows are checked at plan and code review against
the requirement text. No row needs an installed build.

- icm-contract-tables: none — test_validate.py fixtures for table and legacy-list contracts, run in CI pre-merge
- icm-optional-sections: none — test_validate.py fixtures for Checkpoints/Audit/Verify/Human check shapes, run in CI pre-merge
- icm-stage-naming: none — test_validate.py fixtures for hyphen and underscore stage folders, run in CI pre-merge
- icm-path-rules: none — test_validate.py fixtures for back-pointing inputs, foreign outputs and reference back-links, run in CI pre-merge
- icm-form-declaration: none — test_validate.py fixtures for declared, missing and unknown forms, run in CI pre-merge
- icm-umbrella-form: none — fixture plus examples/umbrella validated in CI pre-merge
- icm-record-library-form: none — fixture plus examples/record-library validated in CI pre-merge
- icm-graph-forms: none — fixtures plus examples/knowledge-bundle and examples/context-map validated in CI pre-merge
- icm-system-map-form: none — fixture plus examples/system-map validated in CI pre-merge
- icm-setup-placeholders: none — test_validate.py fixtures for placeholders and conditional sections (with and without --post-setup), run in CI pre-merge
- icm-guardrails: none — test_validate.py fixtures for size, em-dash, duplicate-fact and .gitkeep warnings, run in CI pre-merge
- icm-json-output: none — test_validate.py asserts the --json shape, run in CI pre-merge
- icm-status-script: none — a status.py test over the pipeline example, run in CI pre-merge
- icm-methodology-docs: none — prose; checked at plan and code review against R7, R11, R12, R25, R29
- icm-procedures: none — prose; checked at code review against R26-R28, R33
- icm-examples-migrated: none — CI validates every example and conversion clean pre-merge
- icm-hygiene-ci: none — the PR's own CI run shows the workflow executing and no tracked .pyc

## Out of scope

- Automated tracking of output edits across runs (paper §6.3 "future version").
- Output provenance identifiers / markdown breakpoints (paper §6.2, speculative).
- Generating `AGENTS.md` twins (icm-fr keeps shims instead).
- A `Pi`/`Antigravity` shim (still verify-convention-first).

## Implementation Plans

| Plan | Status |
|---|---|
| _to be written by fr-plan_ | |

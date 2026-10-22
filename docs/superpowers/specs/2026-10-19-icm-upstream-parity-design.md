# icm-fr upstream parity: forms, richer contracts, restructure mode — Design Spec

*Date: 2026-10-19 (revised 2026-10-22 after spec review) · Status: Draft*

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
| Stage naming | split: the method repo uses `01-name`, icm-architect uses `01_name` | `01_name` |

The paper itself also proposes a `Verify` section (§6.2) and the edit-source
principle (§6.3), neither of which icm-fr mentions.

## Decisions

From brainstorming (2026-10-19):

1. **All six forms** are supported: conventions, templates, validator, advise.
2. **Tables are canonical; list-form contracts still validate, with a warning.**
   In-repo workspaces migrate to tables.
3. **New modes/features:** `restructure` mode; `setup` + `status` triggers with
   placeholder checks; audit-first `scaffold` discovery.
4. **Stage naming switches to `NN-slug`** (hyphen), following the method repo.
   Underscore stage folders become a validator error with a rename hint. This is a
   breaking change for workspaces outside the repo, called out in the README.
5. **Bundled `skills/` adopted** as harness-neutral Layer 3 reference.
6. **Guardrails as validator warnings:** size limits and the no-em-dash rule.
7. **Verification:** test fixtures plus a new GitHub Actions workflow.
8. Layer 0 stays `AGENTS.md` with shims (icm-fr's one deliberate departure).
9. One spec, one PR, phased by layer.

From spec review (2026-10-22):

10. **System maps are validated at `map/`**, never at the mapped subject's root.
11. **Canonical examples and in-repo conversions are clean of errors and
    warnings** (info findings allowed).
12. **A missing `(working)`/`(reference)` tag is an error in table contracts and a
    warning in legacy list contracts.**
13. **Template path placeholders use `[slug]` brackets**, matching upstream
    contracts; the repo's `<...>` style migrates. `{{NAME}}` stays reserved for
    setup placeholders.

## Constraints

C1. No text, tables or files from the studied course material (the operator's
local download under `HOMELAB/skool-downloader/downloads/cliefnotes/`) are copied
into the repo. Ideas drawn from it are restated in original prose. Where a rule
originates in the paper or an upstream repository, the new text cites that source
(R7, R11, R12 carry the citation obligation). Checked at code review by
spot-checking distinctive phrases of each new prose file against the course text
(no shared run of 12 or more words).

## Requirements

### Stage contracts

R1. Stage contracts use an Inputs table with columns Source, File/Location, Section/Scope, Why, and an Outputs table with columns Artifact, Location, Format (headers matched case-insensitively); "Full file" is the explicit whole-file scope.
R2. The validator accepts the legacy tagged-list Inputs/Outputs form but emits `LEGACY_LIST_CONTRACT` (warn) naming the stage and pointing to the table form.
R3. Every Inputs entry carries exactly one layer tag, `(working)` or `(reference)`: in a table, inside the Source cell; in a list, anywhere on the line. A missing or doubled tag is `MISSING_TAG`, an error in a table and a warning in a list.
R4. A Source cell may mark a cross-run carry-over with the token `carry-over` alongside `(working)` (e.g. `Previous run (working, carry-over)`). A carry-over input is exempt from R9's ordering rule, and the stage's Process must say what happens on the first run, when the file is absent.
R5. A stage contract may carry these optional sections, each validated for shape when present (`BAD_SECTION`, error, on a missing column):
- `## Checkpoints`, a table with After Step, Agent Presents, Human Decides;
- `## Audit`, a table with Check, Pass Condition, followed by a budget line;
- `## Verify`, a table with Earlier Output, Criterion;
- `## Human check`, prose naming one concrete act the reviewer performs.
R6. An Audit section's budget line matches `Budget: <N> attempts` (N a positive integer), optionally followed by text. A missing budget line is `MISSING_BUDGET` (warn). The contract format, and the conventions text, state that when the budget runs out the agent hands back the best attempt with every check's result, and that every attempt is judged against the original checks.
R7. `conventions.md` states, in original wording with citations to upstream or the paper:
- one-way cross-references;
- selective section routing;
- canonical sources (one home per fact);
- CONTEXT.md as routing, not content;
- tool prerequisites;
- bundled skills;
- specs as contracts;
- checkpoints and audits;
- value validation;
- docs over outputs;
- shared constants;
- recursive routing inside large reference collections;
- generated indexes are rebuilt by script, never hand-edited.
R8. A stage contract may carry a `Do not load:` line naming material an eager agent would wrongly pull in.

### Stage naming and paths

R9. A `(working)` Inputs path whose stage segment is `../NN-slug/output/` must name a stage with a lower number than the current stage, unless the entry is a carry-over (R4). A self or forward reference is `BACK_POINTER`, an error. The check reads only the stage segment, so a `[slug]` placeholder inside the filename is ignored, and a placeholder in the stage segment skips the check. File existence is not checked. The paths checked are backtick-quoted paths in table cells and the first relative path on each list line.
R10. An Outputs Location (table) or target (list) must begin with `output/`; anything else is `FOREIGN_OUTPUT`, an error.
R11. Stage folders are named `NN-slug`, two-digit, contiguous from 01, matching `^\d{2}-[a-z0-9][a-z0-9-]*$`. A folder matching `^\d{2}_` still counts as a stage for numbering and contract checks, and also raises `UNDERSCORE_STAGE` (error) with the suggested hyphen name. A folder under `stages/` that matches neither pattern raises `BAD_STAGE_NAME` (error) and is not counted. Existing test fixtures move to hyphens.
R12. A file under a Layer-3 folder (`_config/`, `shared/`, `skills/`, `references/`, or any top-level folder outside `stages/` whose own `CONTEXT.md` declares it reference) that contains a markdown link or a backtick-quoted relative path into `stages/` is `REFERENCE_BACKLINK` (warn).
R13. No in-repo workspace, template, or procedure contains an underscore stage name. A CI step greps those paths for `\b\d{2}_[a-z]` and fails on any hit outside the validator's own tests and this spec.

### Methodology docs

R14. `principles.md` adds the ten structural invariants (restated with hyphen numbering), the edit-source principle, the U-shaped intervention pattern, and the 2k to 8k token band per step, each tied to the paper or upstream.
R15. A new `forms.md` describes the six forms (pipeline, umbrella, record library, knowledge bundle, context map, system map):
- how to choose a form by the repeating unit;
- each form's skeleton, restated with hyphen numbering;
- each form's defining moves and failure modes;
- how forms nest;
- the validation root and required paths for each form (R17-R21).
R16. A new `discovery.md` drives `scaffold`'s interview:
- a don't-over-structure check first (a task done only once or twice gets a saved prompt, not a workspace);
- who the output is for and what they do next;
- where the information comes from and what breaks;
- a split between thinking and data, existing tools, and AI;
- an impact-by-risk score whose result sets how many review gates the workspace gets, plus where ICM is the wrong tool.

### Forms in the validator

R17. A workspace declares its form in YAML front matter of its root `AGENTS.md` (`form: <name>`, one of `pipeline`, `umbrella`, `record-library`, `knowledge-bundle`, `context-map`, `system-map`). A missing declaration is treated as `pipeline` with `MISSING_FORM` (warn); an unknown value is `UNKNOWN_FORM` (error). The validator reads front matter with a stdlib parser. Shims are unaffected: they still only redirect.
R18. Umbrella: each top-level folder containing its own `AGENTS.md` is a child workspace and is validated recursively under its own declared form, any of the six. Child findings are prefixed with the child path. A file in one child containing a relative path or link into a sibling child is `SIBLING_REFERENCE` (warn). Top-level folders without `AGENTS.md` are shared Layer-3 reference.
R19. Record library: requires `_templates/record-template/` and `_index/log.md`. Each folder under `records/` whose set of relative file paths differs from the template's is `RECORD_DRIFT` (warn). A missing required path is `MISSING_FORM_PATH` (error).
R20. Knowledge bundle and context map: requires `_meta/schema.md`, which lists node types as a markdown list under a `## Types` heading. Every other `.md` file under the workspace, except routing files, `_meta/` and `_templates/`, must carry front matter with `type:` in that list. Otherwise the file gets `NODE_TYPE` (warn). An unresolved relative link or wikilink is `UNRESOLVED_LINK` (info). A knowledge bundle also requires `bundle/index.md`.
R21. System map: validation runs with `map/` as the workspace root, and the subject repo above it is never checked. The root requires:
- `map/AGENTS.md` with `form: system-map`;
- `map/CONTEXT.md`;
- `map/_meta/schema.md`;
- `map/objects/_index.md`.
Rules:
- A `processes/` or `effects/` folder holding no file other than `.gitkeep` is `EMPTY_MAP_SHELF` (error).
- An object or process card whose front matter has `status: verified` needs a `verified:` date, a `revision:` (branch, commit, or vault revision) and at least one citation (a `path:line` or a file path in a `## See` section); otherwise `UNVERIFIED_CARD` (error).
R22. Common checks by form:
- Root `AGENTS.md`, root `CONTEXT.md`, shims, placeholders, conditional sections, guardrails and the duplicate-fact check apply to every form's root.
- Stage checks (R1-R12) apply to pipeline workspaces, and to any `stages/` folder inside another form.
- At a system-map root (`map/`), a missing shim is `MISSING_SHIM` at warn level, not error: the subject repo's own entry file already routes harnesses to `map/`.

### Setup, status and guardrails

R23. Leftover `{{NAME}}` placeholder tokens are `UNFILLED_PLACEHOLDER`: a warning normally, an error under `--post-setup`. `setup/questionnaire.md` is excluded from the scan, because it names the placeholders it fills. A `{{?NAME}}` without a matching `{{/NAME}}`, or one whose span does not start and end at heading boundaries, is `BAD_CONDITIONAL` (error).
R24. The guardrail warnings (`OVERSIZE`, `EM_DASH`) fire as follows:
- `OVERSIZE` fires when a routing `CONTEXT.md` exceeds 80 lines, a Layer-3 reference file exceeds 200 lines, or the root `AGENTS.md` exceeds 60 lines.
- `EM_DASH` fires when a workspace markdown file contains an em dash.
- Both skip `output/` folders (per-run artifacts) and `skills/` (bundled third-party files).
R25. A line of at least 40 characters, other than a heading, a table separator or a link-only line, that appears verbatim in two or more Layer-3 files is `DUPLICATE_FACT` (warn).
R26. Each of `stages/*/output/`, `stages/*/references/`, `_config/`, `shared/`, `skills/` and `_archive/` that exists but is empty, with no `.gitkeep`, is `MISSING_GITKEEP` (warn). System-map `processes/` and `effects/` are exempt, since R21 governs them. Git drops empty folders, so this check matters for local trees; CI proves it through fixtures.
R27. The validator takes `--json` and `--post-setup`. `--json` prints a JSON list of `{level, code, path, message}` objects. `Finding` gains `path`; levels are `error`, `warn` and `info`; the exit code is 1 on any error.
R28. A `status.py` script prints a pipeline diagram, one box per stage:
- **COMPLETE** when the stage's `output/` holds, at any depth, at least one file other than `.gitkeep`; the files are listed.
- **PENDING** otherwise.
- A stage feeding a carry-over shows its status normally, and the consuming stage shows "carry-over from NN".
The workspace template ships a copy at `scripts/status.py`, so a generated workspace runs without icm-fr installed.
R29. Generated workspaces describe a `setup` trigger and a `status` trigger in their `AGENTS.md`:
- `setup` runs the questionnaire, fills the placeholders, and confirms that `validate.py --post-setup` or a placeholder scan finds none left.
- `status` runs `scripts/status.py`, or applies its rule by hand.
R30. The questionnaire template follows upstream's design rules: flat, all at once, system-level only, derive don't ask, sensible defaults, ask once, examples over descriptions. Each question carries `Placeholder`, `Files` and `Type` fields; the placeholder name is written without braces, so R23 never flags it.

### Procedures and portability

R31. `scaffold` and `convert` choose a form via `forms.md` before emitting, emit table contracts, and add Checkpoints or an Audit where a stage is creative or produces binding, external or depended-upon output. `scaffold` runs `discovery.md` first.
R32. A new `restructure` mode (`procedures/restructure.md`) turns an existing folder into an ICM workspace in place:
- take an inventory without moving anything;
- find the hidden form via `forms.md`;
- classify every file as catalog, contract, factory, product or dead;
- check every referrer (in-tree, relative, symlink, external) and case-folded destination collisions;
- propose a migration map for approval;
- copy, verify parity, and only then remove, sending dead files to `_archive/`;
- finish with the walk test and the validator.
R33. `advise` consumes `validate.py --json` and adds these checks:
- the cold walk test, including the token band from R14;
- a fresh-session orientation test;
- a "could a person do this without the AI" test;
- gate placement (after checkable work, before irreversible actions);
- dates and sources on facts that can expire;
- a corrections log, where a fix made twice signals a missing check;
- `_archive/` hygiene;
- generated indexes never hand-edited;
- the conventions from R7.
R34. `portability.md` adds an enforcement ladder for irreversible actions (contract prose, harness permission settings, harness hooks), mapped for each active harness. Stage contracts stay harness-neutral.
R35. `AGENTS.md`, `SKILL.md` and `README.md` describe four modes and the six forms. The README credits the upstream repositories (MIT) and flags R11 as breaking for workspaces outside the repo.

### Templates, examples, migration

R36. Templates ship for:
- the stage contract (tables, all optional sections shown, `[slug]` paths);
- the workspace (`_archive/`, `skills/`, `scripts/status.py`, front matter, `setup`/`status` triggers);
- each non-pipeline form: record template, index log, node card, object card, process card and schema;
- the questionnaire.
Every template is free of em dashes.
R37. `icm-core/example/` (pipeline) is migrated to hyphens, tables and `[slug]` placeholders. It gains front matter, the setup and status triggers, one Checkpoint, and one Audit with a budget. `icm-core/examples/<form>/` ships one minimal canonical example per non-pipeline form. Every example validates with no errors and no warnings.
R38. `conversions/news-report` and `conversions/_scaffold-smoke` are migrated:
- hyphens, tables, front matter and triggers;
- `01-select`'s previous-report input marked as a carry-over (R4);
- every stage-name reference in their root files, contracts, `CONVERSION_NOTES.md` and `ADVISE_FINDINGS.md` updated.
Both validate with no errors and no warnings, and news-report gets a fresh, dated advise report.
R39. `procedures/*.md`, `icm-core/conventions.md` and the templates are migrated to hyphen stage names and `[slug]` placeholders.
R40. A `.gitignore` excludes `__pycache__/` and `.DS_Store`, and the tracked `.pyc` is removed.
R41. A GitHub Actions workflow runs on every pull request and push to main. It runs `test_validate.py`, validates each of `icm-core/example`, `icm-core/examples/*` and `conversions/*` (failing on any error or warning), and runs the R13 grep. Alongside it:
- `.devcontainer/fr-profiles.yaml` declares `ci: {type: github-actions}`;
- `.claude/rules/acceptance-matrix.md` and the `docs/acceptance/matrix.yaml` header stop saying no CI is configured;
- rows proved by CI move to `ci` and prose rows to `manual`, via `fr acceptance set-status`, with the reports regenerated in the same PR.

## Design

### Architecture

```
icm-core/
  principles.md     + invariants, edit-source, U-curve, token band  (R14)
  conventions.md    rewritten: tables, sections, patterns, codes    (R1-R13, R23-R26)
  forms.md          NEW: six forms, roots and required paths        (R15)
  discovery.md      NEW: audit-first interview                      (R16)
  portability.md    + enforcement ladder                            (R34)
  validate.py       form-aware validator, --json, --post-setup      (R1-R27)
  status.py         NEW: pipeline status diagram                    (R28)
  test_validate.py  fixtures per rule and per form
  templates/        stage/, workspace/ (+scripts/status.py), forms/<form>/  (R30, R36)
  example/          pipeline example, migrated                      (R37)
  examples/<form>/  NEW: minimal example per non-pipeline form      (R37)
procedures/ convert.md scaffold.md advise.md restructure.md(NEW)    (R31-R33)
.github/workflows/ci.yml  NEW                                       (R41)
```

`templates/workspace/scripts/status.py` is kept identical to
`icm-core/status.py`. A test asserts the two are byte-identical, so the copy
cannot drift.

### Validator flow

`validate_workspace(path, post_setup=False) -> list[Finding]`.

1. Parse root `AGENTS.md` front matter (lines `key: value` between `---`
   fences) and resolve the form (R17).
2. Run the common checks (R22): Layer 0/1 files, shims, placeholders and
   conditionals (R23), guardrails (R24), duplicates (R25), `.gitkeep` (R26).
3. Dispatch to the form checker:
   - pipeline: stages (R1-R12);
   - umbrella: recurse into children (R18);
   - record library (R19);
   - knowledge bundle or context map (R20);
   - system map (R21).
4. Return findings sorted by path. `main()` parses `--json` and `--post-setup`
   with `argparse`.

### Contract parsing

A section body is a markdown table (header row, separator row, data rows) or a
bullet list:

- **Table:** checked for the required columns and for the R3 tag in each Source
  cell.
- **List:** raises `LEGACY_LIST_CONTRACT`, and each line is checked for the R3 tag
  (warning level).
- **Paths:** R9 and R10 read only the stage segment and the leading `output/`.

### Contract format (canonical)

```markdown
## Inputs
| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Previous stage (working) | `../01-outline/output/[topic-slug]-outline.md` | Full file | The approved outline |
| Previous run (working, carry-over) | `../04-assemble/output/report.md` | "Covered items" | Skip what was covered; absent on first run |
| Config (reference) | `../../_config/voice.md` | "Rules" through "Avoid" | Tone |

Do not load: other stages' references, earlier runs' drafts.

## Process
1. ...

## Checkpoints
| After Step | Agent Presents | Human Decides |
|---|---|---|
| 2 | The outline | Whether the order and scope are right |

## Audit
| Check | Pass Condition |
|---|---|
| Length | 500 to 700 words |
Budget: 3 attempts, then hand back the best attempt with every check's result.

## Verify
| Earlier Output | Criterion |
|---|---|
| `../01-outline/output/[topic-slug]-outline.md` | Every outline section appears, in order |

## Human check
Read the opening paragraph aloud; edit it in place if it drags.

## Outputs
| Artifact | Location | Format |
|---|---|---|
| Draft | `output/[topic-slug]-draft.md` | Markdown, about 600 words |
```

### Migration

- Stage folders are renamed with `git mv`, so history follows.
- A rename sweep updates every stage-name reference in in-repo workspaces, the
  templates, the procedures and `conventions.md` (R38, R39). The R13 grep guards
  the sweep in CI.
- `<...>` path placeholders become `[...]`.
- Em dashes in workspaces and templates are replaced with commas, colons or
  parentheses, whichever reads best.
- The news-report advise report is regenerated and dated.

## Verification

strategy: none

Mechanical rows are proved by `test_validate.py` fixtures, a passing and a failing
case per rule, and by validating every in-repo workspace. Both run in the new CI
workflow on the PR. Prose rows are checked at plan and code review against the
cited requirements. No row needs an installed build. After merge, CI rows sit at
`ci` and prose rows at `manual` (R41).

- icm-contract-tables: none — R1-R3, R8: fixtures for table, list, missing-tag and doubled-tag contracts, run in CI pre-merge
- icm-optional-sections: none — R5, R6: fixtures for each section's shape and for budget present, missing and malformed, run in CI pre-merge
- icm-stage-naming: none — R11, R13: fixtures for hyphen, underscore and bad names, plus the CI grep, run pre-merge
- icm-path-rules: none — R4, R9, R10, R12: fixtures for back-pointers, carry-over, placeholder segments, foreign outputs and reference backlinks, run in CI pre-merge
- icm-form-declaration: none — R17, R22: fixtures for declared, missing and unknown forms, run in CI pre-merge
- icm-umbrella-form: none — R18: fixture with mixed-form children and a sibling reference, plus examples/umbrella, validated in CI pre-merge
- icm-record-library-form: none — R19: fixture with a drifted record, plus examples/record-library, validated in CI pre-merge
- icm-graph-forms: none — R20: fixtures for untyped and unknown-type nodes and unresolved links, plus examples/knowledge-bundle and examples/context-map, validated in CI pre-merge
- icm-system-map-form: none — R21: fixtures for a .gitkeep-only shelf and an uncited verified card, plus examples/system-map validated at map/, in CI pre-merge
- icm-setup-placeholders: none — R23, R29, R30: fixtures for placeholders (with and without --post-setup, questionnaire excluded) and conditionals, plus a test that the workspace template's AGENTS.md names both triggers and that each questionnaire question has its three fields, run in CI pre-merge
- icm-guardrails: none — R24-R26: fixtures for size, em-dash (with output/ and skills/ exempt), duplicate-fact and .gitkeep findings, run in CI pre-merge
- icm-json-output: none — R27: a test that asserts the --json shape and exit codes, run in CI pre-merge
- icm-status-script: none — R28: a status.py test over a fixture with nested output, a .gitkeep-only stage and a carry-over, plus the byte-identity test for the template copy, run in CI pre-merge
- icm-methodology-docs: none — R7, R14-R16, R34, C1: prose, checked at plan and code review against those requirements
- icm-procedures: none — R31-R33, R35: prose, checked at code review against those requirements
- icm-examples-migrated: none — R36-R39: CI validates every example and conversion with zero errors and warnings, and tests assert that a template exists per form and that the pipeline example carries Checkpoints and an Audit with a budget, pre-merge
- icm-hygiene-ci: none — R40, R41: the PR's own CI run shows the workflow executing, the grep passing and no tracked .pyc

## Out of scope

- Automated tracking of output edits across runs (paper §6.3, a "future version").
- Output provenance identifiers and markdown breakpoints (paper §6.2, speculative).
- Generating `AGENTS.md` twins (icm-fr keeps shims instead).
- A `Pi`/`Antigravity` shim (still verify-convention-first).

## Implementation Plans

| Plan | Status |
|---|---|
| _to be written by fr-plan_ | |

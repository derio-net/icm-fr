<!-- fr:journal-schema=2 -->
# Journal: 2026-10-19-icm-upstream-parity

<!-- fr:journal kind=discovery scope=spec id=operator-brief created=2026-10-19T21:19:05+00:00 input=true -->
### operator-brief · discovery · Operator brief

"study /Users/derio/Docs/projects/HOMELAB/skool-downloader/downloads/cliefnotes/ then tell me what you would like to improve in this repo"
then: "use this list as a seed for the fr-brainstorming. I'd like to incorporate as much as possible"
and: "the material is not from a paid community, they are free. I agree that they SHOULD NOT be copied into the repo. Do take the ideas and make surre to rewrite them in your own words."

<!-- fr:journal kind=discovery scope=spec id=upstream-diff created=2026-10-19T21:19:05+00:00 -->
### upstream-diff · discovery · Upstream ICM repos are far ahead of icm-fr

RinDig/Interpretable-Context-Methodology (_core/CONVENTIONS.md, 15 patterns, table contracts, Checkpoints/Audit) and RinDig/icm-architect (10 invariants, six forms, restructure mode, reference-integrity gate), both MIT, fetched 2026-10-19. source/ already holds paper v2.

<!-- fr:journal kind=decision scope=spec id=d-forms created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-forms · decision · Support all six forms

Pipeline, umbrella, record library, knowledge bundle, context map, system map.

<!-- fr:journal kind=decision scope=spec id=d-contracts created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-contracts · decision · Tables canonical, lists accepted with warning

In-repo workspaces migrate to tables.

<!-- fr:journal kind=decision scope=spec id=d-modes created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-modes · decision · Add restructure mode, setup/status triggers, audit-first scaffold

All three selected.

<!-- fr:journal kind=decision scope=spec id=d-verify created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-verify · decision · Fixtures plus a new CI workflow

No install program, so rows use strategy none, proved by test_validate.py in GitHub Actions.

<!-- fr:journal kind=decision scope=spec id=d-naming created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-naming · decision · Switch stage naming to NN-slug

Underscore stage folders become a validator error; in-repo workspaces migrate.

<!-- fr:journal kind=decision scope=spec id=d-skills created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-skills · decision · Adopt bundled skills/ as neutral Layer 3

Referenced like any reference file.

<!-- fr:journal kind=decision scope=spec id=d-guardrails created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-guardrails · decision · Size limits and em-dash rule as warnings

All upstream guardrails, warning level.

<!-- fr:journal kind=decision scope=spec id=d-no-copy created=2026-10-19T21:19:05+00:00 decided_by=operator -->
### d-no-copy · decision · Ideas only from course material

Course material is free but nothing is copied; all prose original; cite paper/upstream where a rule originates there.

<!-- fr:journal kind=finding scope=spec id=s1 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s1 · finding [open] (reviewer: in scope) · Tag rules assumed but absent; table tag not required

severity: major

<!-- fr:journal kind=finding scope=spec id=s2 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s2 · finding [open] (reviewer: in scope) · Cross-run carry-over has no syntax

severity: major

<!-- fr:journal kind=finding scope=spec id=s3 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s3 · finding [open] (reviewer: in scope) · Rename covers only git mv; about 70 stale references

severity: major

<!-- fr:journal kind=finding scope=spec id=s4 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s4 · finding [open] (reviewer: in scope) · New regex cascades NO_STAGES/NONCONTIGUOUS

severity: major

<!-- fr:journal kind=finding scope=spec id=s5 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s5 · finding [open] (reviewer: in scope) · Questionnaire placeholders break --post-setup

severity: major

<!-- fr:journal kind=finding scope=spec id=s6 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s6 · finding [open] (reviewer: in scope) · Per-form minimum paths unnamed

severity: major

<!-- fr:journal kind=finding scope=spec id=s7 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s7 · finding [open] (reviewer: in scope) · System-map validation root ambiguous

severity: major

<!-- fr:journal kind=finding scope=spec id=s8 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s8 · finding [open] (reviewer: in scope) · status trigger points at an absent script; COMPLETE underspecified

severity: major

<!-- fr:journal kind=finding scope=spec id=s9 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s9 · finding [open] (reviewer: in scope) · ci shape wrong; acceptance rule says no CI

severity: major

<!-- fr:journal kind=finding scope=spec id=s10 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s10 · finding [open] (reviewer: in scope) · CI glob matches the examples/ container

severity: major

<!-- fr:journal kind=finding scope=spec id=s11 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s11 · finding [open] (reviewer: in scope) · Templates keep em dashes; R19 scope unsettled

severity: minor

<!-- fr:journal kind=finding scope=spec id=s12 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s12 · finding [open] (reviewer: in scope) · No-errors bar lets examples ship warnings

severity: minor

<!-- fr:journal kind=finding scope=spec id=s13 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s13 · finding [open] (reviewer: in scope) · Path placeholder syntax mixed; existence unclear

severity: minor

<!-- fr:journal kind=finding scope=spec id=s14 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s14 · finding [open] (reviewer: in scope) · Optional section shapes unnamed

severity: minor

<!-- fr:journal kind=finding scope=spec id=s15 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s15 · finding [open] (reviewer: in scope) · Duplicate-fact and .gitkeep terms undefined

severity: minor

<!-- fr:journal kind=finding scope=spec id=s16 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s16 · finding [open] (reviewer: in scope) · Is a .gitkeep-only shelf empty?

severity: minor

<!-- fr:journal kind=finding scope=spec id=s17 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s17 · finding [open] (reviewer: in scope) · Verification rows lack R ids and overclaim

severity: minor

<!-- fr:journal kind=finding scope=spec id=s18 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s18 · finding [open] (reviewer: in scope) · R36 uncheckable, and the citation half was dropped

severity: minor

<!-- fr:journal kind=finding scope=spec id=s19 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s19 · finding [open] (reviewer: in scope) · Background naming row wrong

severity: minor

<!-- fr:journal kind=finding scope=spec id=s20 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s20 · finding [open] (reviewer: in scope) · Upstream builder content omitted

severity: minor

<!-- fr:journal kind=finding scope=spec id=s21 created=2026-10-22T05:04:29+00:00 state=open review_scope=in -->
### s21 · finding [open] (reviewer: in scope) · R10 targets not mechanical

severity: minor

<!-- fr:journal kind=decision scope=spec id=d-map-root created=2026-10-22T05:04:29+00:00 -->
### d-map-root · decision · System maps validated at map/

Never at the subject repo root.

<!-- fr:journal kind=decision scope=spec id=d-clean-examples created=2026-10-22T05:04:29+00:00 -->
### d-clean-examples · decision · Examples and conversions clean of errors and warnings

Info findings allowed.

<!-- fr:journal kind=decision scope=spec id=d-missing-tag created=2026-10-22T05:04:29+00:00 -->
### d-missing-tag · decision · Missing layer tag: error in tables, warning in lists

Matches the list-form leniency.

<!-- fr:journal kind=decision scope=spec id=d-placeholder-syntax created=2026-10-22T05:04:29+00:00 -->
### d-placeholder-syntax · decision · Template path placeholders use [slug]

Matches upstream; <...> migrates; {{NAME}} reserved for setup.

<!-- fr:journal kind=review scope=spec id=spec-review created=2026-10-22T05:04:29+00:00 -->
### spec-review · review · independent spec review: 21 findings, all fixed

fr-spec-reviewer, 10 major and 11 minor, all in scope; operator settled s1, s7, s12 and s13.

<!-- fr:journal kind=finding scope=spec id=s1-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s1 -->
### s1-resolved · finding [fixed] · resolves s1: Tag rules assumed but absent; table tag not required

R3 requires exactly one (working)/(reference) tag per Inputs entry: MISSING_TAG is an error in tables, a warning in lists.

<!-- fr:journal kind=finding scope=spec id=s2-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s2 -->
### s2-resolved · finding [fixed] · resolves s2: Cross-run carry-over has no syntax

R4 defines the `carry-over` Source token, exempts it from R9's ordering rule, and requires a first-run note; R38 migrates news-report 01-select to it.

<!-- fr:journal kind=finding scope=spec id=s3-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s3 -->
### s3-resolved · finding [fixed] · resolves s3: Rename covers only git mv; about 70 stale references

R38 and R39 sweep every stage-name reference in workspaces, templates, procedures and conventions; R13 adds a CI grep guard.

<!-- fr:journal kind=finding scope=spec id=s4-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s4 -->
### s4-resolved · finding [fixed] · resolves s4: New regex cascades NO_STAGES/NONCONTIGUOUS

R11: underscore folders still count as stages and also raise UNDERSCORE_STAGE; BAD_STAGE_NAME covers folders matching neither pattern; fixtures move to hyphens; the README flags the break.

<!-- fr:journal kind=finding scope=spec id=s5-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s5 -->
### s5-resolved · finding [fixed] · resolves s5: Questionnaire placeholders break --post-setup

R23 excludes setup/questionnaire.md from the scan; R30 writes placeholder names without braces.

<!-- fr:journal kind=finding scope=spec id=s6-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s6 -->
### s6-resolved · finding [fixed] · resolves s6: Per-form minimum paths unnamed

R18-R21 name exact paths and discovery rules; umbrella children are folders with their own AGENTS.md and may be any form.

<!-- fr:journal kind=finding scope=spec id=s7-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s7 -->
### s7-resolved · finding [fixed] · resolves s7: System-map validation root ambiguous

Operator decision 10: validate at map/. R21 and R22 define the map/ root and relax shims to warnings there.

<!-- fr:journal kind=finding scope=spec id=s8-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s8 -->
### s8-resolved · finding [fixed] · resolves s8: status trigger points at an absent script; COMPLETE underspecified

R28 ships scripts/status.py in the workspace template (byte-identity test), scans output/ recursively, ignores .gitkeep, and shows carry-over.

<!-- fr:journal kind=finding scope=spec id=s9-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s9 -->
### s9-resolved · finding [fixed] · resolves s9: ci shape wrong; acceptance rule says no CI

R41 writes ci: {type: github-actions}, updates the rule and matrix header, and moves rows to ci or manual via fr acceptance.

<!-- fr:journal kind=finding scope=spec id=s10-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s10 -->
### s10-resolved · finding [fixed] · resolves s10: CI glob matches the examples/ container

R41 validates icm-core/example, icm-core/examples/* and conversions/* individually.

<!-- fr:journal kind=finding scope=spec id=s11-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s11 -->
### s11-resolved · finding [fixed] · resolves s11: Templates keep em dashes; R19 scope unsettled

R36 makes templates em-dash free; R24 exempts output/ and skills/.

<!-- fr:journal kind=finding scope=spec id=s12-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s12 -->
### s12-resolved · finding [fixed] · resolves s12: No-errors bar lets examples ship warnings

Operator decision 11: examples and conversions must be clean of errors and warnings (R37, R38, R41); front matter and triggers are added.

<!-- fr:journal kind=finding scope=spec id=s13-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s13 -->
### s13-resolved · finding [fixed] · resolves s13: Path placeholder syntax mixed; existence unclear

Operator decision 13: [slug] brackets. R9 checks only the stage segment, with no existence check and a skip on placeholder segments; it states which list paths are checked.

<!-- fr:journal kind=finding scope=spec id=s14-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s14 -->
### s14-resolved · finding [fixed] · resolves s14: Optional section shapes unnamed

R5 names the columns for each section; R6 defines the budget-line grammar and MISSING_BUDGET (warn).

<!-- fr:journal kind=finding scope=spec id=s15-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s15 -->
### s15-resolved · finding [fixed] · resolves s15: Duplicate-fact and .gitkeep terms undefined

R25 sets 40 characters with exclusions; R26 lists the persistent folders and notes CI proves it through fixtures.

<!-- fr:journal kind=finding scope=spec id=s16-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s16 -->
### s16-resolved · finding [fixed] · resolves s16: Is a .gitkeep-only shelf empty?

R21: yes, EMPTY_MAP_SHELF is an error; R26 exempts processes/ and effects/; verified cards need a date, a revision and a citation.

<!-- fr:journal kind=finding scope=spec id=s17-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s17 -->
### s17-resolved · finding [fixed] · resolves s17: Verification rows lack R ids and overclaim

Each bullet now cites its R ids; trigger, questionnaire, per-form template and example-section tests are added; ci and manual end states stated.

<!-- fr:journal kind=finding scope=spec id=s18-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s18 -->
### s18-resolved · finding [fixed] · resolves s18: R36 uncheckable, and the citation half was dropped

Moved to Constraints C1 with the source location, a 12-word spot-check method and the citation obligation.

<!-- fr:journal kind=finding scope=spec id=s19-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s19 -->
### s19-resolved · finding [fixed] · resolves s19: Background naming row wrong

Row corrected (upstream is split); R14 and R15 restate invariants and skeletons with hyphens.

<!-- fr:journal kind=finding scope=spec id=s20-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s20 -->
### s20-resolved · finding [fixed] · resolves s20: Upstream builder content omitted

Added: form choice in restructure (R32), token band (R14, R33), generated-index rule (R7, R33), over-structuring check (R16).

<!-- fr:journal kind=finding scope=spec id=s21-resolved created=2026-10-22T05:04:29+00:00 state=fixed resolves=s21 -->
### s21-resolved · finding [fixed] · resolves s21: R10 targets not mechanical

R12 lists fixed Layer-3 folders, plus any folder whose CONTEXT.md declares it reference, and defines a link as a markdown link or backtick relative path.

<!-- fr:journal kind=decision scope=spec id=exit-baseline created=2026-10-22T05:04:30+00:00 -->
### exit-baseline · decision · exit when spec-review resolved

The exit when spec-review resolved; `fr verification set` and `deliver` compare against it.

```yaml
row_gates:
  icm-contract-tables: none
  icm-examples-migrated: none
  icm-form-declaration: none
  icm-graph-forms: none
  icm-guardrails: none
  icm-hygiene-ci: none
  icm-json-output: none
  icm-methodology-docs: none
  icm-optional-sections: none
  icm-path-rules: none
  icm-procedures: none
  icm-record-library-form: none
  icm-setup-placeholders: none
  icm-stage-naming: none
  icm-status-script: none
  icm-system-map-form: none
  icm-umbrella-form: none
row_kinds:
  icm-contract-tables: none
  icm-examples-migrated: none
  icm-form-declaration: none
  icm-graph-forms: none
  icm-guardrails: none
  icm-hygiene-ci: none
  icm-json-output: none
  icm-methodology-docs: none
  icm-optional-sections: none
  icm-path-rules: none
  icm-procedures: none
  icm-record-library-form: none
  icm-setup-placeholders: none
  icm-stage-naming: none
  icm-status-script: none
  icm-system-map-form: none
  icm-umbrella-form: none
run_gate: none
run_kind: none
```

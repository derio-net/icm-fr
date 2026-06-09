# icm-fr — Implementation Plan

Build the `icm-fr` skill: a Claude Code doorway plus a portable, agent-agnostic
`icm-core/` that operationalizes the Interpretable Context Methodology (ICM). The
skill offers three modes — **convert** (turn an existing artifact into an ICM
workspace + gap report), **scaffold** (interview → new workspace), and **advise**
(review an existing workspace) — over one shared methodology core.

Spec: `docs/superpowers/specs/2026-06-09-icm-fr-skill-design.md`.

## Approach

Phasing is **layered by capability** (Approach A): a foundation phase lays down
the portable substance and the tooling, then one phase per mode, then a manual
publish phase. Execution is **local and interactive** — no GitHub remote is
required until the final, operator-gated publish step.

The architectural spine is the spec's Approach C: the substance lives in plain
files (`icm-core/` + the procedures), and the Claude-specific `SKILL.md` is just
one disposable doorway. Portability is enforced mechanically — `AGENTS.md` is the
only root file with real content; `CLAUDE.md`, `GEMINI.md`, and the Copilot
instructions are one-line redirects; stage contracts name no harness.

## Phases

1. **Foundation** — The validator comes first (TDD): tests in `test_validate.py`
   pin the structural contract before `validate.py` exists. Then the methodology
   core (`principles.md`, `conventions.md`, `portability.md`), the templates, a
   hand-built canonical example workspace (which must pass the validator), and the
   repo's own doorways (root `AGENTS.md` + 3 shims + `SKILL.md` router + README).
   The validator and `conventions.md` describe the same rules from two angles —
   they must stay in sync.

2. **Convert + news-report** — Write `procedures/convert.md` (ingest → decompose &
   classify → emit → gap report), then run it against the willikins `news-report`
   skill as the worked integration test. Output lands in `conversions/news-report/`
   with a `CONVERSION_NOTES.md` gap report. Acceptance is validator-clean plus a
   human read-through against the spec's bar. The honest part: hooks and AI-driven
   branching don't become stages — the gap report says so out loud.

3. **Scaffold** — `procedures/scaffold.md` swaps convert's ingest+decompose for an
   interview. A throwaway smoke-test workspace proves the procedure emits a
   validator-clean tree.

4. **Advise** — `procedures/advise.md` is non-generative: run the validator for the
   structural subset, then add the judgment-level findings (a stage doing two jobs,
   mixed reference/working inputs, context bloat, missing review gates). Exercised
   against the example (near-clean) and the news-report conversion (real findings).

5. **[manual] Publish** — Operator-gated. Create `derio-net/icm-fr` public, push,
   set topics, confirm MIT + README render. Decide here whether converted
   workspaces stay as in-repo examples or move home.

## Testing

ICM artifacts are markdown, so the test harness is the structural validator
(`icm-core/validate.py`, built test-first in phase 1). Every mode runs it on its
output before declaring done. The news-report conversion is the end-to-end test
for the convert engine; a human checklist covers the judgment-level acceptance
that a validator cannot.

## Out of scope (v1)

Behavior-identical reproduction of converted skills; Pi / Antigravity / Hermes
shims (extension points only); semantic debugging / traceability; automated
mid-pipeline branching; converting event-driven hooks into stages.

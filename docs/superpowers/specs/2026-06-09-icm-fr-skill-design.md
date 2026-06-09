# icm-fr — Design Spec

*Date: 2026-06-09 · Status: Draft (brainstorming output, pre-plan)*

## Summary

`icm-fr` is a Claude Code skill (plus a portable, agent-agnostic core) that operationalizes the
**Interpretable Context Methodology (ICM)** — Van Clief & McDermott, University of Edinburgh,
March 2026 (arXiv:2603.16021, MIT-licensed). ICM replaces multi-agent orchestration frameworks
with filesystem structure: numbered stage folders, plain-markdown `CONTEXT.md` contracts, and a
five-layer context hierarchy, driven by a single agent reading the right files at the right moment.

The skill does three things over a shared ICM knowledge core:

1. **convert** — turn an existing artifact (first target: a willikins skill) into an ICM workspace,
   plus an explicit gap report.
2. **scaffold** — interview the user and generate a new ICM workspace from scratch.
3. **advise** — review an existing ICM workspace against the methodology and report findings.

The driving motivation is **agent-agnostic workflows**: an ICM workspace is plain files, so it can
run on any harness that reads a folder. The hard requirement is that *output workspaces* are
portable — not locked to Claude Code.

Source material is staged in `source/` (the paper PDF, a visual guide HTML, and a text extraction).

## Background: what ICM is (the load-bearing ideas)

- **Five-layer context hierarchy.** L0 identity ("where am I"), L1 task routing ("where do I go"),
  L2 stage contract ("what do I do"), L3 reference material ("what rules apply" — the *factory*,
  stable across runs), L4 working artifacts ("what am I working with" — the *product*, per-run).
  No agent reads everything; each stage loads ~2–8k focused tokens vs ~42k monolithic.
- **Five principles.** One stage / one job · plain text as the interface · layered context loading ·
  every output an edit surface · configure the factory, not the product.
- **Numbered stage folders** (`01_research/`, `02_script/`…) encode execution order. Each stage has
  a `CONTEXT.md` *contract*: Inputs (split L3 reference / L4 working) → Process → Outputs. Output of
  stage N is the input to stage N+1; a human reviews at each gate.
- **Workspace-builder.** ICM includes an ICM workspace whose output is a new workspace — the
  recursive heart of the methodology, and the conceptual basis for `scaffold` and `convert`.
- **Where it fits / doesn't.** Fits sequential, human-reviewed, repeatable workflows. Does *not* fit
  real-time multi-agent collaboration, high-concurrency, or complex AI-driven mid-pipeline branching.
  (This is why event-driven hooks do not map cleanly to ICM stages — see `convert`.)

## Decisions (from brainstorming, 2026-06-09)

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Three modes in v1: convert + scaffold + advise | Operator wants the full capability; convert and scaffold share one generation engine, advise is the separable third. |
| D2 | Architecture = thin Claude doorway + portable `icm-core/` (Approach C) | Only option that delivers the agent-agnostic property — substance lives in plain files; the skill format is one disposable entry point. |
| D3 | Output workspaces are agent-agnostic — **hard requirement** | The whole point. Layer 0 is `AGENTS.md`, not `CLAUDE.md`. |
| D4 | Compatibility layer at **both** levels: every generated workspace *and* the icm-fr tool itself get multiple harness doorways | Operator wants to run the converter from any harness, and every produced workspace to run anywhere. |
| D5 | Default shim set: `AGENTS.md` (canonical) + `CLAUDE.md` + `GEMINI.md` + `.github/copilot-instructions.md` | The four conventions confident as of 2026-06. Pi / Antigravity / Hermes are documented extension points, added after verifying each convention. |
| D6 | convert success bar = **faithful structure + gap report, human finishes** | Matches ICM's own U-shaped human-intervention model; behavior-identical reproduction is out of scope. |
| D7 | First worked conversion target: **willikins `news-report` skill** | Genuinely staged, reviewable, repeatable — cleanest ICM fit; operator knows it cold, so fidelity is easy to judge. |
| D8 | Repo: `derio-net/icm-fr`, public, MIT | Matches upstream ICM license; agent-agnostic workflows are a shareable artifact. |

## Architecture

```
derio-net/icm-fr/
├── README.md                        project overview, links to source paper, MIT license
├── LICENSE                          MIT
├── AGENTS.md                        ← tool doorway (canonical) → procedures/
├── CLAUDE.md                        ← thin shim → AGENTS.md
├── GEMINI.md                        ← thin shim → AGENTS.md
├── .github/copilot-instructions.md  ← thin shim → AGENTS.md
├── SKILL.md                         ← Claude Code skill doorway (mode router)
├── icm-core/                        ← the portable, agent-agnostic substance
│   ├── AGENTS.md                    methodology entrypoint (Layer 0 for the core)
│   ├── principles.md                the 5 principles + 5-layer hierarchy, canonical
│   ├── conventions.md               folder naming, stage-contract format, L3/L4 rules
│   ├── portability.md               shim registry + procedure to add a harness
│   ├── validate.(py|sh)             structural validator (lint pass for a workspace)
│   ├── templates/
│   │   ├── workspace/               AGENTS.md + 3 shims, CONTEXT.md, _config/, setup/
│   │   └── stage/                   CONTEXT.md contract template (Inputs/Process/Outputs)
│   └── example/                     one canonical, hand-built worked workspace
├── procedures/
│   ├── convert.md                   artifact → ICM workspace + gap report
│   ├── scaffold.md                  interview → ICM workspace
│   └── advise.md                    review an existing workspace against principles
└── source/                          paper PDF + visual guide + text extraction (staged)
```

Two ideas do the work:

- **`icm-core/` is itself a minimal ICM Layer-3 bundle.** Point any agent at `icm-core/AGENTS.md`
  and it can follow the methodology with no skill machinery. That is the portability guarantee made
  concrete.
- **`SKILL.md` + `procedures/` + the root shims are the convenience layer.** If they vanished, the
  methodology would still be fully usable from the core. The skill is a doorway, not a vault.

## Components

### The three modes (documented procedures over `icm-core/`, no bespoke framework)

Shared preamble for every mode: load `principles.md` + `conventions.md` + `portability.md` first
(the methodology as Layer-3 reference), then diverge.

**`convert` — artifact → ICM workspace + gap report (lead capability)**
1. **Ingest** the target (a willikins skill: `SKILL.md` + helper files + any rules it leans on).
2. **Decompose** into stages — identify natural sequential breakpoints ("one stage, one job").
   Classify every piece: *stage* (does work) · *Layer 3 reference* (rule/constraint/voice guide) ·
   *Layer 4 working artifact* · *local script* (mechanical, no AI).
3. **Emit** the numbered-folder workspace from `templates/`, writing a `CONTEXT.md` contract
   (Inputs split L3/L4 · Process · Outputs) per stage, plus `AGENTS.md` + the 3 shims.
4. **Gap report** (`CONVERSION_NOTES.md`) — explicitly flags pieces that did *not* map cleanly
   (e.g. event-driven hooks → not sequential, cannot be a stage), judgment calls made, and the
   last-mile edits a human should do. Honest accounting; nothing silently dropped.

**`scaffold` — interview → ICM workspace**
Same generation engine; an interview (the paper's setup questionnaire) replaces ingest+decompose.
Discovery (domain, workflow) → stage-mapping (natural breakpoints) → emit → questionnaire for
`_config/`.

**`advise` — review an existing workspace (non-generative)**
Read a workspace, critique against the 5 principles + 5 layers (stage doing two jobs? reference and
working artifacts mixed? context bloat? missing review gate? non-contiguous numbering?), output a
findings list. No file generation.

### Agnostic conventions & shim mechanics (mechanical, not aspirational)

- **`AGENTS.md` is the only file with real content** at any workspace root. Layer 0's job
  (where am I, what's here, where to find things) is harness-neutral prose.
- **Shims are dumb redirects.** Each of `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`
  contains one line: *"This workspace uses AGENTS.md as its entrypoint. Read ./AGENTS.md and follow
  it."* No drift risk — content lives in one place.
- **Stage `CONTEXT.md` contracts name no harness.** Inputs/Process/Outputs reference relative paths
  only — never "use the Task tool" or "Claude will…". Any agent maps the contract to its own
  primitives.
- **Local scripts stay plain.** The "mechanical work that doesn't need AI" is Python/shell invoked
  by path — already agnostic.
- **`portability.md` is the registry.** The canonical shim set, the one-line template per shim, and a
  documented procedure for adding a harness (Pi / Antigravity / Hermes slots, marked "verify
  convention before adding"). Both the tool and every generated workspace draw their shim set here.

### Validation

- **Structural validator** (`icm-core/validate.*`) — the agnostic equivalent of a lint pass. Checks a
  workspace for: `AGENTS.md` present · all configured shims present and pointing correctly · every
  stage folder has a `CONTEXT.md` with the three required sections (Inputs/Process/Outputs) ·
  numbering contiguous. `scaffold` and `convert` run it before declaring done. Written per the
  project preference for Python over bash where there's any parsing/state.
- **Canonical example workspace** (`icm-core/example/`) — one hand-built, correct ICM workspace
  (small, 2–3 stages) that triples as: the reference `advise` measures against, the shape
  `templates/` produces, and the thing a human reads to learn ICM.

## First test case: converting `news-report`

`news-report` (willikins skill) is the worked conversion. It is genuinely staged (topic watchlist →
fetch/search → per-source summarize → assemble/compare), human-reviewable at each gate, and
repeatable — a textbook ICM fit.

**Acceptance bar (matches D6 "faithful structure, human finishes"):**
1. Correct numbered stages with complete Inputs/Process/Outputs contracts.
2. Correct classification of news-report's pieces — topic config → L3 reference; fetched articles →
   L4 working; assembly logic → stages.
3. Emits `AGENTS.md` + all 3 shims.
4. Ships a `CONVERSION_NOTES.md` gap report naming every non-mechanical judgment call.

*Not required:* that the converted workspace runs byte-identical to the original skill.

## Testing approach

ICM artifacts are markdown, so "tests" are structural assertions run by the validator (see
Validation). The acceptance criteria for each component are expressed as validator checks plus, for
the worked conversion, a human read-through of `news-report`'s converted workspace against the
acceptance bar above.

## Out of scope (v1)

- Behavior-identical reproduction of converted skills (D6).
- Pi / Antigravity / Hermes shims (extension points only until conventions verified).
- Semantic debugging / source-level traceability (the paper's future-work; not v1).
- Automated mid-pipeline branching (outside ICM's fit envelope).
- Converting event-driven hooks into stages (flagged by `convert`, not supported).

## Implementation Plans

| Plan | Repo | Status | Notes |
|------|------|--------|-------|
| 2026-06-09-icm-fr-skill | `derio-net/icm-fr` | `2026-06-09-icm-fr-skill` | — |

## Open questions

- GitHub remote creation (`derio-net/icm-fr`) is deferred until the operator says go (outward-facing).
- Where converted workspaces live long-term (inside icm-fr as examples vs back in their home repo) —
  decide when the news-report conversion lands.

# ICM Workspace Conventions

The rules for an ICM workspace. Some are checked mechanically by `validate.py`;
others are conventions a human or reviewing agent upholds. The two are marked
explicitly below — do not assume "validator-clean" means "fully conformant".

**Enforced by `validate.py`** (keep the validator, its tests, and this list in
sync): root `AGENTS.md` present · root `CONTEXT.md` present · every active harness
shim present and redirecting to `AGENTS.md` · at least one stage · every stage has
a `CONTEXT.md` with real `## Inputs` / `## Process` / `## Outputs` H2 headings ·
stage numbers have no duplicates and run contiguously from `01`.

**Documented but NOT mechanically checked** (use `advise`, or a human, to enforce):
the Inputs `(reference)`/`(working)` tagging, the `name -> output/` Outputs format,
the harness-neutrality rule, and slug style. These are judgment-level — the
validator checks structure, not line-level content.

## Folder layout

```
workspace/
├── AGENTS.md                        Layer 0 — identity + structure map (real content)
├── CLAUDE.md · GEMINI.md            harness shims — one-line redirect to AGENTS.md
├── .github/copilot-instructions.md  harness shim — redirect to AGENTS.md
├── CONTEXT.md                       Layer 1 — workspace task routing
├── _config/                         Layer 3 — stable config (voice.md, design-system.md…)
├── shared/                          Layer 3 — reference shared across stages
├── setup/
│   └── questionnaire.md             setup questions that populate _config/ on first run
└── stages/
    ├── 01_<slug>/
    │   ├── CONTEXT.md               Layer 2 — the stage contract
    │   ├── references/              Layer 3 — reference scoped to this stage
    │   └── output/                  Layer 4 — this stage's working artifacts
    ├── 02_<slug>/ …
    └── NN_<slug>/ …
```

## Naming rules

- Stage folders: `stages/NN_slug/`, two-digit zero-padded number, **contiguous
  from `01`**. The number encodes execution order. No gaps (`01`, `03` with no
  `02` is an error).
- Slugs are lowercase, hyphen- or underscore-free single tokens where possible
  (`01_research`, `02_script`).

## The stage contract (`stages/NN_x/CONTEXT.md`)

Every stage contract has exactly these three sections, in this order:

```markdown
## Inputs
- Layer 4 (working): ../01_research/output/
- Layer 3 (reference): ../../_config/voice.md
- Layer 3 (reference): references/structure.md

## Process
Write a script based on the research output.
Follow the structure in structure.md. Match the tone in voice.md.

## Outputs
- script_draft.md -> output/
```

- **`## Inputs`** — one line per input. Each line is tagged `(working)` for Layer 4
  (per-run artifacts) or `(reference)` for Layer 3 (stable rules). This split is the
  control point of the whole system. A `(working)` input is usually the previous
  stage's `output/`. The **first stage's** per-run input is whatever enters the
  pipeline each run, and it is `(working)` even though it does not live in an
  `output/` folder. It takes one of three shapes:
  - a **run brief** the user supplies (e.g. `setup/brief.md`, a provided topic), or
  - a **trigger** (the run is driven by the date / a schedule, with no explicit
    brief — as in a daily report), often paired with
  - a **cross-run carry-over**: the previous run's output, read for incremental work
    (e.g. last run's report, to skip already-covered items). This is legitimately
    `(working)`, names a real producer (that stage's `output/`, from the prior run),
    and is **absent on the first run** — the contract must say what happens then.
- **`## Process`** — what the stage does, in plain prose or numbered steps.
- **`## Outputs`** — one line per artifact, `name -> output/`.

## The harness-neutrality rule

Stage contracts **name no harness and no harness-specific primitive**. Write
"read `../01_research/output/`, write `script_draft.md`" — never "use the Task
tool" or "Claude will…". Any agent maps the contract to its own primitives. The
only file that carries identity is `AGENTS.md`; everything downstream is portable
by construction.

## Handoffs & review gates

The output of stage N is the input to stage N+1 (its `output/` appears in N+1's
`## Inputs` as a `(working)` line). Between every pair of stages there is an
implicit human review gate: a person may open `stages/NN_x/output/`, edit it, and
the next stage reads whatever they left. Do not collapse two stages to "save a
gate" — the gate is a feature.

## Local scripts

Mechanical work that needs no AI (fetching data, moving files, formatting, sending
email) belongs in plain Python/shell scripts invoked by path, not in stage prose.
Scripts stay harness-agnostic too.

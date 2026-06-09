# ICM Principles & the Five-Layer Hierarchy

The canonical statement of the Interpretable Context Methodology, distilled for an
agent to load as Layer-3 reference before running any mode. Source: Van Clief &
McDermott, *Interpretable Context Methodology: Folder Structure as Agent
Architecture* (arXiv:2603.16021, MIT). Full text in `../source/`.

ICM's claim: for **sequential, human-reviewed, repeatable** workflows, filesystem
structure replaces framework-level orchestration. One agent reads the right files
at the right moment. The folder structure *is* the architecture.

## The five principles

1. **One stage, one job.** Each stage handles a single step and writes its output
   to its own folder. A stage that fetches data does not also filter it; a stage
   that filters does not also format. (McIlroy's Unix rule; Parnas's information
   hiding.)
2. **Plain text as the interface.** Stages communicate through markdown and JSON.
   No binary formats, no database connections, no proprietary serialization. Any
   tool that reads a text file can participate; any human with a text editor can
   inspect or modify any artifact.
3. **Layered context loading.** An agent loads only the context the current stage
   needs. Less irrelevant context means better output — this is prevention, not
   compression. Each stage runs at ~2,000–8,000 focused tokens instead of a
   ~40,000-token monolith full of material irrelevant to the step.
4. **Every output is an edit surface.** Each stage's intermediate output is a file
   a human can open, read, edit, and save before the next stage runs. The system
   picks up whatever the human left there.
5. **Configure the factory, not the product.** A workspace is set up once with the
   user's preferences, brand, and structure. Each run then produces a new
   deliverable using the same configuration.

## The five-layer context hierarchy

The agent loads layers top-to-bottom, but only what the current stage needs.

| Layer | File | Question it answers | Role | Typical size |
|-------|------|---------------------|------|--------------|
| L0 | `AGENTS.md` | "Where am I?" | Identity / structure map (Structural) | ~800 tok |
| L1 | `CONTEXT.md` | "Where do I go?" | Workspace task routing (Structural) | ~300 tok |
| L2 | stage `CONTEXT.md` | "What do I do?" | Stage contract (Structural) | 200–500 tok |
| L3 | reference material | "What rules apply?" | The **factory** — stable across runs | 500–2k tok |
| L4 | working artifacts | "What am I working with?" | The **product** — per run | varies |

> ICM names Layer 0 `CLAUDE.md`. icm-fr uses **`AGENTS.md`** instead, for
> agent-agnostic portability (see `portability.md`). Per-harness shims redirect to
> it. This is the one deliberate departure from the paper.

Layers 0–2 are **structural** (routing + instructions). Layers 3–4 are **content**.

## Layer 3 vs Layer 4 — the factory / product split

The distinction matters because the two ask different things of the model.

| | Layer 3: Reference (factory) | Layer 4: Working (product) |
|--|------------------------------|----------------------------|
| Changes between runs | No | Yes |
| Examples | `voice.md`, `design-system.md`, `conventions.md` | `research-output.md`, `script-draft.md` |
| Model should | **Internalize as constraints** | **Process as input** |
| Configured during | Workspace setup (once) | Pipeline execution (each run) |
| Lives in | `references/`, `_config/`, `shared/` | `output/` |
| Analogy | The recipe | The ingredients |

Mixing persistent rules with per-run artifacts in one undifferentiated context
window forces the model to sort them itself. Separating them in the folder
structure delivers already-organized context.

## Where ICM fits — and where it does not

**Fits:** sequential workflows (step 2 follows step 1), human review at each step,
the same pipeline run repeatedly with different input — content production,
research, training material, reporting.

**Does not fit** (use a real framework): real-time multi-agent collaboration,
high-concurrency systems, complex AI-driven mid-pipeline branching, anything
needing message-passing infrastructure. This is why **event-driven hooks do not
map to ICM stages** — they are triggers, not sequential steps.

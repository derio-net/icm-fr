# Conversion Notes — news-report → ICM

Source: `willikins/.claude/skills/news-report/` (`SKILL.md`, `bias-framework.md`,
`team-topic-prompt.md`) + `willikins/projects/news-report/topics.yaml`.
Converted: 2026-06-09. Bar: faithful structure, human finishes (D6).

## Acceptance

- [x] Correct numbered stages (01_select → 04_assemble), each with a complete
      Inputs/Process/Outputs contract.
- [x] Every original piece classified (below) or listed under "Did not map".
- [x] `AGENTS.md` + all 3 shims present (validator exit 0).
- [x] This report names every judgment call and unmapped piece.

## How the original mapped

| Original piece | Class | Lands in |
|----------------|-------|----------|
| Report Mode Step 0/1b (fail-fast + incremental dedup) | stage | `01_select` |
| Step 1 (discover: RSS + WebSearch) | stage | `02_gather` |
| Step 2 (fetch full article text) | stage (+ script) | `02_gather` + `scripts/fetch.py` |
| Step 3 (per-topic sections) | stage | `03_analyze` |
| Steps 4–5 (intersections, suggestions) + Step 6 (assemble) | stage | `04_assemble` |
| `bias-framework.md` (7 dimensions) | Layer 3 reference | `shared/bias-framework.md` |
| `topics.yaml` (watchlist) | Layer 3 reference | `_config/topics.yaml` |
| Step 3 section structure / Step 6 report skeleton | Layer 3 reference | stage `references/` |
| ThreadPoolExecutor `http_get` fetch | local script | `scripts/fetch.py` |
| Per-run topic + today's date | Layer 4 working | stage `output/` |

## Did not map (surfaced, not dropped)

- **Topics Mode** (interactive CRUD on the watchlist). Not a sequential pipeline —
  it is an editor. In ICM "every output is an edit surface", so this becomes:
  edit `_config/topics.yaml` directly. Documented in `CONTEXT.md` and the
  setup questionnaire. No stage represents it.
- **Team Mode / parallel teammates** (`team-topic-prompt.md`, one Sonnet teammate
  per topic, concurrent). This is concurrent agent coordination — outside ICM's
  sequential fit envelope. The *work* each teammate did is folded into `02_gather`
  and `03_analyze` (the per-topic contract is identical); the *parallelism* is an
  execution optimisation an agent may still apply, but it is not part of the
  workspace structure. `team-topic-prompt.md` itself was not copied — it is
  redundant with the stage contracts.
- **Headless/cron + subagent delegation** (`claude -p`, `delegation: staff:
  newsdesk`, "spawn Agent with model sonnet"). Harness-specific execution detail.
  ICM names no harness; how the workspace is invoked is the operator's choice. Not
  represented in any contract.
- **Browser Mode** (the `browser-harness new_tab` fallback for JS/login-walled
  pages). This was an *actual fetch path* that retrieved full content from
  JS-rendered or logged-in-paywalled sites. It is **not preserved** — `02_gather`
  degrades such pages to "snippet only" instead. This is a real capability loss, not
  a structural no-op; flagged in Human last-mile. (It is a harness-specific fetch
  path, not a stage, so it has no ICM home without a browser-capable local script.)

## Judgment calls

1. **Stage boundaries.** Split into 4 stages on the natural human-review gates:
   which topics run (01), the raw source material (02), the analysed sections (03),
   the assembled report (04). Discover (Step 1) and fetch (Step 2) were combined
   into `02_gather` — they are one job ("get the source material") and the original
   ran them back-to-back with no review between.
2. **`fetch.py` rewritten harness-agnostic.** The original called `browser-harness
   http_get`. To keep the workspace portable, the helper is plain stdlib
   `urllib` + `ThreadPoolExecutor`. Behaviour is close but not identical (no shared
   browser session, no Brave profile / saved logins) — see Human last-mile.
3. **WebSearch as a generic "web search" step.** The contract says "run web
   searches"; it names no specific tool, per the harness-neutrality rule. Whatever
   the running agent has (WebSearch, an MCP search tool) satisfies it.
4. **The hard-stop guard placed in `02_gather`, not `01_select`.** The original ran
   it in Step 0, but in the ICM split only `02_gather` exercises live retrieval
   (`01_select` reads local files), so the fail-fast belongs there. The original's
   cancellation-stub-for-audit write is kept as a note in 02's process. `01_select`
   now reads the previous run's report from `../04_assemble/output/` for its
   incremental check (no cross-stage copy-back).

## Human last-mile (before first run)

- **Verify the fetch path.** If you want the original's browser fallback (Brave +
  saved logins for paywalled sites), wire it into `scripts/fetch.py` or a sibling
  script; the stdlib version handles plain HTML only.
- **Confirm the web-search tool** available in your harness and that 02's "run web
  searches" maps to it.
- **Review `01_select`'s incremental logic** — it parses today's report for
  `#### <title>` headings; confirm that matches your report skeleton's heading level.
- **Decide on parallelism.** If you process many topics, you may want to fan out
  02/03 per topic for speed — that is an execution choice, not a workspace change.

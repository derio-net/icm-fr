# Acceptance Matrix — Backfill Rule (repo-wide)

## Rule

`docs/acceptance/matrix.yaml` is the registry of business-level acceptance
tests × verification levels × automation status. **Any PR that does one of
the following updates the matrix in the SAME PR:**

- adds or changes a spec `## Test Plan` (new spec ⇒ new rows; the CI
  staleness guard fails a spec with a Test Plan that no row cites)
- adds tests that verify an existing row (add the ref to `levels`, move
  `status` up: `not-implemented` → `unwired` → `ci`/`scheduled`)
- ships a surface or capability a `not-implemented` row waits on
- changes CI workflows that run matrix-referenced checks
- discovers a red acceptance: set `status: failing` — the
  `acceptance-report` workflow then FAILS by design until it is fixed or
  re-classified with reasoning in `notes`

Statuses move **explicitly, never silently**: `ci` | `scheduled` (automated
— the safe end) · `walked` (proven live, dated by its walk) · `manual` (a
process that is never automatable) · `unwired` (a test exists, not in CI —
debt) · `walk-owed` (a live or post-merge walk is owed — debt) ·
`not-implemented` (nothing exists — debt) · `failing` (fails CI).

## How

- Add rows: `fr acceptance add --id ... --capability ... --acceptance ...
  --origin <repo>:<path> --level unit=<repo>:<path> --status ... --notes ...`
- Check: `fr acceptance check` (refs, staleness, statuses; exit 2 on
  `failing`). Nag: `fr acceptance status` — **any agent session in this repo
  runs `fr acceptance status --brief` at session start** (Claude Code does it
  automatically via the super-fr SessionStart hook; other harnesses honor
  this line).
- Reports: THREE **committed, tracked** renderings of `matrix.yaml`, kept in
  sync — `docs/acceptance/report_local.html` (local links, viewable from a
  checkout), `docs/acceptance/report_linked.html` (github.com blob links), and
  `docs/acceptance/report_linked.md` (the linked report as **Markdown**, which
  github.com renders inline — committed `.html` is shown as source, not
  rendered). `fr acceptance add` regenerates **all three**; drift (incl.
  hand-edited status flips) is gated by `fr acceptance check` itself — it fails
  when any committed report is missing or stale. Regenerate by hand with `fr
  acceptance report --deterministic` (writes all three) and commit them.
  `docs/acceptance/report.html` is a separate **ad-hoc, gitignored** render: `fr
  acceptance report` (no flag) writes it git-stamped honoring `--link-mode`
  (github in CI, local otherwise); links resolve relative to sibling checkouts
  (`--sibling-root`, default `..`).
- CI: none is configured. `fr acceptance check` runs locally, and no row may
  move to `ci` until the repo has a CI config (`fr acceptance init --with-ci`
  scaffolds one).

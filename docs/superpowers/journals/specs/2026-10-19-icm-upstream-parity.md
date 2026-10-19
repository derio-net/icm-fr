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

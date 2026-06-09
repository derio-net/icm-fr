# {{WORKSPACE_NAME}} — Task Routing (Layer 1)

Given what the user wants to do, this maps to a stage. Run stages in order unless
re-running a single stage after an edit.

| Stage | Job | Read its contract |
|-------|-----|-------------------|
| 01_<slug> | <one-line job> | `stages/01_<slug>/CONTEXT.md` |
| 02_<slug> | <one-line job> | `stages/02_<slug>/CONTEXT.md` |

## Shared resources

- `_config/` — <what stable config lives here>
- `shared/` — <reference material used by more than one stage>

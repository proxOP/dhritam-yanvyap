# Reasoning Graph

## Node Definition (Agent Roles)
- `ROOT`: Composer entry point
- `DECOMPOSE`: Breakdown sub-tasks
- `FETCH_MARKET`: Market Agent execution
- `FETCH_SC`: Supply Chain Agent execution
- `VALIDATE`: Governance check
- `SYNTHESIZE`: Output generation

## Transitions
- `ROOT` -> `DECOMPOSE`
- `DECOMPOSE` -> `FETCH_MARKET` (Parallel)
- `DECOMPOSE` -> `FETCH_SC` (Parallel)
- `FETCH_*` -> `VALIDATE`
- `VALIDATE` (Pass) -> `SYNTHESIZE`
- `VALIDATE` (Fail) -> `TERMINATE`

## Termination Conditions
- **Success**: `SYNTHESIZE` completes with confidence > threshold.
- **Fail**: `VALIDATE` rejects output or timeout reached.
- **Partial**: One domain fails, but others succeed (if allowed by query).

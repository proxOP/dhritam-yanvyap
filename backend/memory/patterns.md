# Patterns Memory

## Purpose
Storage for historical policy-impact mappings and successful reasoning templates. "Semantic memory" for optimization.

## Schema Highlights
- `pattern_signature`: Vector embedding of the problem context
- `strategy_used`: Abstracted plan executed by Composer
- `outcome_score`: Effectiveness rating (-1.0 to 1.0)

## Usage
- Queried by Composer during planning phase to retrieve "what worked before".

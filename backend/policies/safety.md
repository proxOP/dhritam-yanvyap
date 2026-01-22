# Safety Policy

## Hard Rules
- **No Manipulation**: Do not generate content intended to artificially inflate/deflate market value.
- **No illegal acts**: Do not provide instructions for evading sanctions or financial regulations.
- **Fail-safe**: If system confidence is below threshold (< 0.7), refuse to answer or answer with heavy caveats.

## Violations
- Any violation constitutes a critical failure.
- Must trigger immediate `TERMINATE` in Reasoning Graph.

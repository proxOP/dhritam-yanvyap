# Composer Agent

## Responsibility
Orchestrates the problem-solving process. Decomposes queries, assigns tasks to agents, and synthesizes partial results.

## Inputs
- User query
- Available agent capabilities registry

## Outputs
- Execution plan (DAG of tasks)
- Final synthesized answer

## Constraints
- Must handle agent failures gracefully (retry or partial response)
- Optimizes for cost/latency balance

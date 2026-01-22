# Observer Agent

## Responsibility
Monitors the execution state of other agents and the overall reasoning graph. Detects stalls, loops, or errors.

## Inputs
- Agent heartbeat signals
- Reasoning graph state updates
- Resource usage metrics

## Outputs
- Health status report
- Interrupt signals (if infinite loop detected)
- Performance logs

## Constraints
- Must operate with low latency
- Cannot modify the reasoning graph directly (read-only monitoring)

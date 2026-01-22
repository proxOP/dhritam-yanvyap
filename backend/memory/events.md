# Events Memory

## Purpose
Structured event history storage. Serves as the audit log and "episodic memory" for agents.

## Schema Highlights
- `timestamp`: UTC ISO8601
- `actor`: Agent ID or User ID
- `action`: Type of action performed
- `payload`: Snapshot of data associated with the event
- `trace_id`: Link to parent request

## Retention
- Hot storage: 30 days
- Cold archival: Infinite

# API Routes

## REST Endpoints

### Ingestion & Analysis
- `POST /v1/ingest/document`
  - Accepts: PDF, CSV, Text
  - Returns: Job ID for ingestion pipeline
- `POST /v1/ingest/stream`
  - Accepts: Real-time market data stream
  - Returns: Stream connection status

### Intelligence & Reasoning
- `POST /v1/query`
  - Body: Natural language query
  - Returns: Synthesized answer + Reasoning Graph ID
- `GET /v1/graph/{graph_id}`
  - Returns: State of a specific reasoning chain

### System Status
- `GET /health`
  - Returns: System operational status
- `GET /metrics`
  - Returns: Agent performance metrics

## Contracts (High Level)

### Query Request
```json
{
  "query": "Impact of semiconductor shortage on automotive sector",
  "context_window": "6m",
  "depth": "deep"
}
```

### Query Response
```json
{
  "answer": "...",
  "confidence_score": 0.89,
  "sources": [...],
  "reasoning_trace_id": "uuid"
}
```

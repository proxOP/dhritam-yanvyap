# Request Lifecycle

## Flow Description

1. **Request Ingestion**
   - API Gateway receives `POST /v1/query`.
   - Request is validated and assigned a unique `trace_id`.

2. **Orchestration (LangGraph)**
   - API triggers LangGraph execution asynchronously.
   - Graph executes nodes: Observer -> Interpreter -> Domain -> Market -> SupplyChain -> Governance -> Confidence -> Composer.

3. **Agent Execution**
   - Each agent processes the shared state and appends its findings.
   - `Governance` checks intermediate outputs for compliance.

4. **Synthesis**
   - `Composer` synthesizes the final output from all agent contributions.
   - `Confidence` scores the result.

5. **Response**
   - Client polls `GET /v1/graph/{trace_id}` to retrieve the final state.

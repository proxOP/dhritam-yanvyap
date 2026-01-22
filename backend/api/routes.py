import uuid
from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from ..graph.graph import run_graph

router = APIRouter()

# Simple in-memory storage for Phase 1 demo
RESULTS = {}

class QueryRequest(BaseModel):
    query: str

async def process_graph(trace_id: str, query: str):
    result = await run_graph(query)
    RESULTS[trace_id] = result

@router.post("/v1/query")
async def query_intelligence(request: QueryRequest, background_tasks: BackgroundTasks):
    trace_id = str(uuid.uuid4())
    background_tasks.add_task(process_graph, trace_id, request.query)
    return {"reasoning_trace_id": trace_id}

@router.get("/v1/graph/{trace_id}")
async def get_graph_state(trace_id: str):
    result = RESULTS.get(trace_id)
    if not result:
        return {"status": "processing", "trace_id": trace_id}
    
    return {
        "status": "completed",
        "trace_id": trace_id,
        "result": result.get("final_output", {}),
        "full_state": result # For debugging/ReasoningView
    }

@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "dritam-intelligence"}

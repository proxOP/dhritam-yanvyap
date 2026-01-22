from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, END

# Import agents
from ..agents.observer_agent import observer_node
from ..agents.interpreter_agent import interpreter_node
from ..agents.domain_agent import domain_node
from ..agents.market_agent import market_node
from ..agents.supply_chain_agent import supply_chain_node
from ..agents.governance_agent import governance_node
from ..agents.confidence_agent import confidence_node
from ..agents.composer_agent import composer_node

# Define shared state
class GraphState(TypedDict):
    query: str
    candidate_events: Optional[List[Dict]]
    structured_events: Optional[List[Dict]]
    domains: Optional[Dict]
    market_impact: Optional[Dict]
    supply_chain_data: Optional[Dict]
    governance_data: Optional[Dict]
    confidence_metric: Optional[Dict]
    final_output: Optional[Dict]

# Define the graph
def create_graph():
    workflow = StateGraph(GraphState)

    # Add nodes
    workflow.add_node("observer", observer_node)
    workflow.add_node("interpreter", interpreter_node)
    workflow.add_node("domain", domain_node)
    workflow.add_node("market", market_node)
    workflow.add_node("supply_chain", supply_chain_node)
    workflow.add_node("governance", governance_node)
    workflow.add_node("confidence", confidence_node)
    workflow.add_node("composer", composer_node)

    # Add edges (Linear chain for Phase 1 as requested)
    workflow.set_entry_point("observer")
    workflow.add_edge("observer", "interpreter")
    workflow.add_edge("interpreter", "domain")
    workflow.add_edge("domain", "market")
    workflow.add_edge("market", "supply_chain")
    workflow.add_edge("supply_chain", "governance")
    workflow.add_edge("governance", "confidence")
    workflow.add_edge("confidence", "composer")
    workflow.add_edge("composer", END)

    # Compile
    app = workflow.compile()
    return app

# Expose the runnable graph
runnable_graph = create_graph()

# Helper to run the graph (triggered by API)
async def run_graph(query: str):
    initial_state = {"query": query}
    result = await runnable_graph.ainvoke(initial_state)
    return result

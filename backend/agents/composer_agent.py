# agents/composer_agent.py

def composer_node(state: dict):
    """
    Input: final state
    Output: Event Summary, Reasoning Chain, Beneficiary Hierarchy, etc.
    """
    print("--- Composer Agent ---")
    
    # Dummy logic to synthesize everything
    summary = {
        "event_summary": "Analysis of query: " + state.get("query", "Unknown"),
        "reasoning_chain": ["Observer", "Interpreter", "Domain", "Market", "SupplyChain", "Governance", "Confidence"],
        "beneficiaries": {
            "primary": "Technology Sector",
            "heirarchy": "Top-Down"
        },
        "geographic_scope": "Global",
        "confidence_score": state.get("confidence_metric", {}).get("score", 0.0),
        "time_horizon": "Short-term"
    }
    
    return {"final_output": summary}

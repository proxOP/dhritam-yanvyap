# agents/confidence_agent.py

def confidence_node(state: dict):
    """
    Input: full reasoning state
    Output: confidence_score and risk flags
    """
    print("--- Confidence Agent ---")
    
    # Dummy logic
    confidence = {
        "score": 0.88,
        "risks": ["Data latency > 5min", "Unverified secondary source"],
        "level": "HIGH"
    }
    
    return {"confidence_metric": confidence}

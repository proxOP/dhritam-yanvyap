# agents/domain_agent.py

def domain_node(state: dict):
    """
    Input: structured event
    Output: primary and secondary domains
    """
    print("--- Domain Agent ---")
    # structured_events = state.get("structured_events", [])
    
    # Dummy logic
    domains = {
        "primary": "Technology",
        "secondary": ["Automotive", "Supply Chain"]
    }
    
    return {"domains": domains}

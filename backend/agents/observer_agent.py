# agents/observer_agent.py

def observer_node(state: dict):
    """
    Input: raw query
    Output: candidate events
    """
    print("--- Observer Agent ---")
    query = state.get("query", "")
    
    # Dummy logic: simple keyword extraction as 'events'
    events = [{"text": query, "source": "user_input"}]
    
    return {"candidate_events": events}

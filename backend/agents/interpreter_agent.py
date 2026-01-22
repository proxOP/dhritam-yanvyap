# agents/interpreter_agent.py

def interpreter_node(state: dict):
    """
    Input: event text
    Output: structured event (type, action, target, geography, time)
    """
    print("--- Interpreter Agent ---")
    candidate_events = state.get("candidate_events", [])
    structured_events = []
    
    for event in candidate_events:
        # Dummy logic: structure the raw text
        structured_events.append({
            "type": "financial_query",
            "action": "analyze",
            "target": event.get("text"),
            "geography": "global",
            "time": "current"
        })
        
    return {"structured_events": structured_events}

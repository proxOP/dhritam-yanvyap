# agents/market_agent.py

def market_node(state: dict):
    """
    Input: domains + event
    Output: beneficiary and disadvantaged entities
    """
    print("--- Market Agent ---")
    # domains = state.get("domains")
    
    # Dummy logic
    impact = {
        "beneficiary": ["ChipCorp", "TechGiant"],
        "disadvantaged": ["LegacyAuto", "OldMech"]
    }
    
    return {"market_impact": impact}

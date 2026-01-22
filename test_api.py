import requests
import time
import sys

BASE_URL = "http://localhost:8000"

def test_flow():
    print("Testing /health...")
    try:
        r = requests.get(f"{BASE_URL}/health")
        print(r.json())
    except Exception as e:
        print(f"Health check failed: {e}")
        return

    print("\nTesting /v1/query...")
    query = {"query": "Impact of lithium shortage on EV market"}
    r = requests.post(f"{BASE_URL}/v1/query", json=query)
    data = r.json()
    print(f"Response: {data}")
    
    trace_id = data.get("reasoning_trace_id")
    if not trace_id:
        print("No trace_id returned!")
        sys.exit(1)

    print(f"\nPolling /v1/graph/{trace_id}...")
    for _ in range(10):
        r = requests.get(f"{BASE_URL}/v1/graph/{trace_id}")
        state = r.json()
        status = state.get("status")
        print(f"Status: {status}")
        
        if status == "completed":
            print("\nFinal Result:")
            print(state.get("result", {}))
            return
        
        time.sleep(1)
        
    print("Timeout waiting for completion.")

if __name__ == "__main__":
    # Wait for server to boot
    time.sleep(2) 
    test_flow()

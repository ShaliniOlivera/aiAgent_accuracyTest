import requests
import json
from config import API_URL

#SIMILARITY_THRESHOLD = 85
def send_request(test_input):
    
    request_data = {
        "type": "MESSAGE",
        "message": {
            "sender": {"email": "test@example.com"},
            "text": test_input
        }
    }

    try:
        response = requests.post(API_URL, json=request_data)
        response.raise_for_status()
        response_json = response.json()
        return response_json.get("text", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"\u274c API request failed: {e}")
    except json.JSONDecodeError:
        print(f"\u274c Failed to parse JSON. Raw response: {response.text}")

    return ""

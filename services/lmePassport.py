import requests
from typing import Dict

def submit_stock(payload: Dict, token: str) -> Dict:
    url = "https://www.lmepassport.com/api/doc-upload-service/records/inventory/import"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()  # Handle errors
    return response.json()

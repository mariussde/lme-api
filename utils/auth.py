import requests

def get_access_token(client_id: str, client_secret: str) -> str:
    url = "https://sam.ihsmarkit.com:443/sso/oauth2/realms/root/realms/Customers/access_token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "scope": "openid profile email",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # Ensure we catch HTTP errors
    return response.json()["access_token"]

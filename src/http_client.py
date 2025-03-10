# src/http_client.py
import requests


class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {'X-CMC_PRO_API_KEY': api_key}

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)
        return response.json()

class CMCHTTPClient(HTTPClient):
    def get_listings(self):
        result = self.get("/v1/cryptocurrency/listings/latest")
        return result.get("data", [])

    def get_currency(self, currency_id: int):
        result = self.get("/v2/cryptocurrency/quotes/latest", params={"id": currency_id})
        return result.get("data", {}).get(str(currency_id), {})

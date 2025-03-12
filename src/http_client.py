# src/http_client.py
import requests
# Importing the requests library to make HTTP requests

class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        # Initializing the HTTPClient with the base URL and API key
        self.base_url = base_url
        self.headers = {'X-CMC_PRO_API_KEY': api_key}
        # Setting the headers to include the API key

    def get(self, endpoint, params=None):
        # Method to make a GET request to the specified endpoint with optional parameters
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)
        return response.json()
        # Returning the JSON response

class CMCHTTPClient(HTTPClient):
    def get_listings(self):
        # Method to get the latest cryptocurrency listings
        result = self.get("/v1/cryptocurrency/listings/latest")
        return result.get("data", [])
        # Returning the list of cryptocurrencies

    def get_currency(self, currency_id: int):
        # Method to get the details of a specific cryptocurrency by its ID
        result = self.get("/v2/cryptocurrency/quotes/latest", params={"id": currency_id})
        return result.get("data", {}).get(str(currency_id), {})
        # Returning the details of the specified cryptocurrency

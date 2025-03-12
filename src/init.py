# src/init.py

from src.configPackege.config import settings
# Importing the settings object from the configuration package

from src.http_client import CMCHTTPClient
# Importing the CMCHTTPClient class from the http_client module

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)
# Creating an instance of the CMCHTTPClient with the base URL and API key from the settings

# src/routerPackage/CryptoData.py
from flask import Blueprint, jsonify, request
# Importing Blueprint, jsonify, and request from Flask for route creation, JSON responses, and handling HTTP requests

from src.init import cmc_client
# Importing the CoinMarketCap client from the initialization module

router = Blueprint('cryptocurrencies', __name__, url_prefix='/cryptocurrencies')
# Creating a Blueprint for the cryptocurrencies routes with the URL prefix /cryptocurrencies

@router.route('/', methods=['GET'])
def get_cryptocurrencies():
    # Route to get a list of all cryptocurrencies
    return jsonify(cmc_client.get_listings())
    # Return the list of cryptocurrencies in JSON format

@router.route('/<int:currency_id>', methods=['GET'])
def get_cryptocurrency(currency_id):
    # Route to get details of a specific cryptocurrency by its ID
    return jsonify(cmc_client.get_currency(currency_id))
    # Return the cryptocurrency details in JSON format

@router.route("/search", methods=["GET"])
def search_cryptocurrency():
    # Route to search for a cryptocurrency by query
    query = request.args.get("query")
    # Get the search query from the request arguments
    return jsonify(cmc_client.search(query))
    # Return the search results in JSON format

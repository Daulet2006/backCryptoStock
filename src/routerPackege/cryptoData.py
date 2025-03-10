# src/routerPackage/CryptoData.py
from flask import Blueprint, jsonify
from src.init import cmc_client

router = Blueprint('cryptocurrencies', __name__, url_prefix='/cryptocurrencies')

@router.route('/', methods=['GET'])
def get_cryptocurrencies():
    return jsonify(cmc_client.get_listings())

@router.route('/<int:currency_id>', methods=['GET'])
def get_cryptocurrency(currency_id):
    return jsonify(cmc_client.get_currency(currency_id))


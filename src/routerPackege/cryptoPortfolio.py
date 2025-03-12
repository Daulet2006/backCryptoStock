from flask import Blueprint, jsonify, request
# Importing Blueprint, jsonify, and request from Flask for route creation, JSON responses, and handling HTTP requests

from src.configPackege.config import db
# Importing the database object from the configuration package

from src.configPackege.models import CryptoAsset
# Importing the CryptoAsset model from the configuration package's models

router = Blueprint('crypto_assets', __name__, url_prefix='/crypto_assets')
# Creating a Blueprint for the crypto_assets routes with the URL prefix /crypto_assets


@router.route('/getAll', methods=['GET'])
def get_all_assets():
    # Route to get all crypto assets
    assets = CryptoAsset.query.all()
    if not assets:
        # Return message if the database is empty
        return jsonify({"message": "DB is null"}), 404
    list_asset = []
    for asset in assets:
        # Convert each asset to a dictionary and add it to the list
        result = [asset.to_dict()]
        list_asset.append(result)
    return jsonify(list_asset), 200
    # Return the list of assets in JSON format


@router.route('/get/<int:id>', methods=['GET'])
def get_asset_by_id(id):
    # Route to get a specific asset by ID
    asset = CryptoAsset.query.get(id)
    if not asset:
        # Return error message if the asset is not found
        return jsonify({"error": "Asset not found"}), 404
    return jsonify(asset.to_dict()), 200
    # Return the asset details in JSON format


@router.route('/add', methods=['POST'])
def add_asset():
    # Route to add a new crypto asset
    data = request.get_json()
    # Get the data from the request body

    existing_asset = CryptoAsset.query.filter_by(symbol=data['symbol']).first()
    if existing_asset:
        # Return error message if an asset with the same symbol already exists
        return jsonify({"error": "Asset with this symbol already exists"}), 400

    new_asset = CryptoAsset(
        name=data['name'],
        symbol=data['symbol'],
        price=data['price'],
        market_cap=data['market_cap'],
        volume_24h=data['volume_24h'],
        percent_change_1h=data['percent_change_1h'],
        percent_change_24h=data['percent_change_24h'],
        percent_change_7d=data['percent_change_7d']
    )
    # Create a new CryptoAsset object with the provided data

    db.session.add(new_asset)
    # Add the new asset to the database session
    db.session.commit()
    # Commit the session to save the asset to the database

    return jsonify(new_asset.to_dict()), 201
    # Return the new asset details in JSON format with a 201 Created status


@router.route('/update/<int:id>', methods=['PUT'])
def update_asset(id):
    # Route to update an existing crypto asset by ID
    asset = CryptoAsset.query.get(id)
    if not asset:
        # Return error message if the asset is not found
        return jsonify({"error": "Asset not found"}), 404

    data = request.json
    # Get the data from the request body

    for key, value in data.items():
        if hasattr(asset, key):
            setattr(asset, key, value)
    # Update the asset attributes with the provided data

    db.session.commit()
    # Commit the session to save the changes to the database
    return jsonify({"message": "Asset updated successfully!"}), 200
    # Return a success message in JSON format


@router.route('/delete/<int:id>', methods=['DELETE'])
def delete_asset(id):
    # Route to delete a crypto asset by ID
    asset = CryptoAsset.query.get(id)
    if not asset:
        # Return error message if the asset is not found
        return jsonify({"error": "Asset not found"}), 404

    db.session.delete(asset)
    # Delete the asset from the database session
    db.session.commit()
    # Commit the session to save the changes to the database
    return jsonify({"message": "Asset deleted successfully!"}), 200
    # Return a success message in JSON format

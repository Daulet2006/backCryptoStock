from flask import Flask
# Importing Flask from the Flask library to create the Flask application

from flask_cors import CORS
# Importing CORS from the Flask-CORS library to handle Cross-Origin Resource Sharing

from src.routerPackege.cryptoData import router as router_crypto
# Importing the cryptoData router and aliasing it as router_crypto

from src.routerPackege.cryptoPortfolio import router as router_portfolio
# Importing the cryptoPortfolio router and aliasing it as router_portfolio

from src.configPackege.config import app, db
# Importing the app and db objects from the configuration package

CORS(app, resources={r"/*": {"origins": ["http://localhost:5174","http://localhost:5173", "http://127.0.0.1:5174","http://127.0.0.1:5173" ]}})
# Enabling Cross-Origin Resource Sharing (CORS) for the Flask app with specified origins

app.register_blueprint(router_crypto)
# Registering the cryptoData router blueprint with the Flask app

app.register_blueprint(router_portfolio)
# Registering the cryptoPortfolio router blueprint with the Flask app

if __name__ == '__main__':
    with app.app_context():
        """Running the Flask app within the app context"""
        # db.drop_all()  # Uncomment to drop all tables
        # db.create_all()  # Uncomment to create all tables with the updated schema
    app.run(debug=True)
    # Running the Flask app in debug mode

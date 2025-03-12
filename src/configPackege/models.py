from datetime import datetime
# Importing the datetime module to work with date and time

from src.configPackege.config import db, app


# Importing the database object and Flask app instance from the configuration package

class CryptoCurrency(db.Model):
    # Defining the CryptoCurrency model for the crypto_currencies table
    __tablename__ = 'crypto_currencies'

    id = db.Column(db.Integer, primary_key=True)
    # Defining the primary key column
    name = db.Column(db.String(100), nullable=False)
    # Defining a column for the cryptocurrency name
    symbol = db.Column(db.String(20), nullable=False, unique=True)
    # Defining a unique column for the cryptocurrency symbol
    price = db.Column(db.Float, nullable=False)
    # Defining a column for the cryptocurrency price
    market_cap = db.Column(db.Float, nullable=False)
    # Defining a column for the cryptocurrency market cap
    volume_24h = db.Column(db.Float, nullable=False)
    # Defining a column for the 24-hour trading volume
    percent_change_1h = db.Column(db.Float, nullable=False)
    # Defining a column for the 1-hour price change percentage
    percent_change_24h = db.Column(db.Float, nullable=False)
    # Defining a column for the 24-hour price change percentage
    percent_change_7d = db.Column(db.Float, nullable=False)
    # Defining a column for the 7-day price change percentage
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Defining a column for the last update timestamp, with default and on-update values
    is_custom = db.Column(db.Boolean, default=False, nullable=False)

    # Defining a column to indicate if the entry is custom

    def __init__(self, name, symbol, price, market_cap, volume_24h, percent_change_1h, percent_change_24h,
                 percent_change_7d, updated_at, is_custom):
        # Initializing the CryptoCurrency object with the provided values
        self.name = name
        self.symbol = symbol
        self.price = price
        self.market_cap = market_cap
        self.volume_24h = volume_24h
        self.percent_change_1h = percent_change_1h
        self.percent_change_24h = percent_change_24h
        self.percent_change_7d = percent_change_7d
        self.updated_at = updated_at
        self.is_custom = is_custom

    def to_dict(self):
        # Converting the CryptoCurrency object to a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "symbol": self.symbol,
            "price": self.price,
            "market_cap": self.market_cap,
            "volume_24h": self.volume_24h,
            "percent_change_1h": self.percent_change_1h,
            "percent_change_24h": self.percent_change_24h,
            "percent_change_7d": self.percent_change_7d,
            "updated_at": self.updated_at,
            "is_custom": self.is_custom
        }


class CryptoAsset(db.Model):
    # Defining the CryptoAsset model for the crypto_assets table
    __tablename__ = 'crypto_assets'

    id = db.Column(db.Integer, primary_key=True)
    # Defining the primary key column
    name = db.Column(db.String(100), nullable=False)
    # Defining a column for the crypto asset name
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    # Defining a unique column for the crypto asset symbol
    price = db.Column(db.Float, nullable=False)
    # Defining a column for the crypto asset price
    market_cap = db.Column(db.Float, nullable=False)
    # Defining a column for the crypto asset market cap
    volume_24h = db.Column(db.Float, nullable=False)
    # Defining a column for the 24-hour trading volume
    percent_change_1h = db.Column(db.Float, nullable=False)
    # Defining a column for the 1-hour price change percentage
    percent_change_24h = db.Column(db.Float, nullable=False)
    # Defining a column for the 24-hour price change percentage
    percent_change_7d = db.Column(db.Float, nullable=False)
    # Defining a column for the 7-day price change percentage
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Defining a column for the creation timestamp, with a default value

    def to_dict(self):
        # Converting the CryptoAsset object to a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "symbol": self.symbol,
            "price": self.price,
            "market_cap": self.market_cap,
            "volume_24h": self.volume_24h,
            "percent_change_1h": self.percent_change_1h,
            "percent_change_24h": self.percent_change_24h,
            "percent_change_7d": self.percent_change_7d,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None
        }


with app.app_context():
    # Creating the database tables within the Flask app context
    db.create_all()
    print("✅ Tables created successfully!")
    # Printing a success message

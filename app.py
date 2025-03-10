from flask import Flask
from flask_cors import CORS
from src.routerPackege.cryptoData import router as router_crypto
from src.routerPackege.cryptoPortfolio import router as router_portfolio
from src.configPackege.config import app, db  # Добавляем импорт базы данных

CORS(app, resources={r"/*": {"origins": ["http://localhost:5174","http://localhost:5173", "http://127.0.0.1:5174","http://127.0.0.1:5173" ]}})

app.register_blueprint(router_crypto)
app.register_blueprint(router_portfolio)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Удаляем старую таблицу
        db.create_all()  # Создаем новую с полем updated_at
    app.run(debug=True)

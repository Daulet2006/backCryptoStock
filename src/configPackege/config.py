from pydantic_settings import BaseSettings, SettingsConfigDict
# Importing BaseSettings and SettingsConfigDict from pydantic_settings for configuration management

from flask import Flask
# Importing Flask from the Flask library to create the Flask application

from flask_sqlalchemy import SQLAlchemy
# Importing SQLAlchemy from the Flask-SQLAlchemy library for database management

import os
# Importing the os module for interacting with the operating system

from dotenv import load_dotenv
# Importing load_dotenv from the python-dotenv library to load environment variables from a .env file

load_dotenv("../../.env")
# Loading environment variables from the .env file located two directories up

class Settings(BaseSettings):
    # Defining a Settings class inheriting from BaseSettings for configuration settings
    CMC_API_KEY: str
    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding="utf-8")
    # Configuring the Settings class to load from the .env file with utf-8 encoding

settings = Settings()
# Creating an instance of the Settings class to access the configuration settings

app = Flask(__name__)
# Creating the Flask application instance

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Configuring the SQLAlchemy database URI from the environment variable

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Disabling SQLAlchemy track modifications to save resources

db = SQLAlchemy(app)
# Creating the SQLAlchemy object by passing the Flask app instance

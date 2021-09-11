import os
from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config import Config

login_manager = LoginManager()
client = MongoClient(Config.MONGO_DB_URI, port=27017)
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from .users.routes import users

    app.register_blueprint(users)

    return app
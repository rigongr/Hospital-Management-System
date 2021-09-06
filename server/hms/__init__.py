import os
from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from hms.config import Config


client = MongoClient(Config.MONGO_DB_URI, port=27017)
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    bcrypt.init_app(app)

    from hms.users.routes import users

    app.register_blueprint(users)

    return app
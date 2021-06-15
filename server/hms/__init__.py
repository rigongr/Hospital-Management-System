from flask import Flask, Blueprint
from flask_pymongo import PyMongo
from .config import Config

app = Flask(__name__)
app.config['MONGO_URI'] = Config.MONGO_URI
mongo = PyMongo(app)



def create_app(config_class=Config):
    
    from .users.routes import users    

    app.register_blueprint(users)

    return app
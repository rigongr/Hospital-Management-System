from flask import Flask, Blueprint

from flask_mysqldb import MySQL
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy


from .config import Config

app = Flask(__name__)
app.config['MONGO_URI'] = Config.MONGO_URI
app.config['SQLALCHEMY_DATABASE_URI'] = Config.POSTGRE_URI
mongo = PyMongo(app)
db = SQLAlchemy(app)



def create_app(config_class=Config):
    
    from .users.routes import users    

    app.register_blueprint(users)

    return app
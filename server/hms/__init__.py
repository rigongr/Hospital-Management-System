from logging import DEBUG
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

DEBUG = True
DB_URL = Config.DB_URL

app = Flask(__name__)
app.config['MONGO_URI'] = Config.MONGO_URI
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy, PostgreSQL & MongoDB
mongo = PyMongo(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    
    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)
    
    db.create_all()

    print('Creating tables.')
    print('Shiny!')


def create_app(config_class=Config):

    db.init_app(app)

    from .users.routes import users    

    app.register_blueprint(users)

    return app
from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

from hms import create_app, db
from hms.models import User
from dotenv import load_dotenv


app = create_app()
load_dotenv()
db.create_all()
db.session.commit()

# configuration
DEBUG = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
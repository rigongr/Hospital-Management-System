from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

from hms import create_app, db


app = create_app()
db.drop_all()
db.create_all()
db.session.commit()

# configuration
DEBUG = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
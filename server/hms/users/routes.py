from flask import Flask, jsonify, Blueprint
from flask_cors import CORS


users = Blueprint('users', __name__)

# sanity check route
@users.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('PONG! This is coming from the backend (Python, Flask).')
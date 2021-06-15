from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from hms import mongo


users = Blueprint('users', __name__)

users_collection = mongo.db.listingsAndReviews

# sanity check route
@users.route('/ping', methods=['GET'])
def ping_pong():
    air_bnb_data = mongo.db.listingsAndReviews.find()[2]
    keys = []
    for key in air_bnb_data:
        keys.append(key)
        
    print(keys)
    return jsonify(keys)
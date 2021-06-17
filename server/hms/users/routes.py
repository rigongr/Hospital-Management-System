from typing import List
from flask import Flask, jsonify, Blueprint, json
from flask_cors import CORS
from hms import mongo, db
from hms.models import User
from logger.logger import write_log


users = Blueprint('users', __name__)

users_collection = mongo.db.listingsAndReviews

# sanity check route
@users.route('/ping', methods=['GET'])
def ping_pong():
    air_bnb_data = mongo.db.listingsAndReviews.find()[2] # NoSQL Getting data from collection (MONGO)
    sql_user = User.query.filter_by(username="rigon").first()
    keys = []
    for key in air_bnb_data:
        keys.append(key)
    both_data: List[List, str] = keys, "Username: " + sql_user.username + "\nID: " + str(sql_user.id)
    return jsonify(both_data)
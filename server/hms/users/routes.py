from typing import List
from flask import jsonify, Blueprint
from hms import mongo, db
from hms.models import Doctor
from logger.logger import write_log
import random

users = Blueprint('users', __name__)

users_collection = mongo.db.listingsAndReviews

# sanity check route
@users.route('/ping', methods=['GET'])
def ping_pong():
    users = Doctor.query.all()
    for user in users:

        db.session.delete(user)
        db.session.commit()
    
    doc = Doctor(f"Doctor{random.randint(0, 999)}", f"doctor{str(random.randint(0, 99999))}@gmail.com", "testing123", random.randint(0, 123456),  "Doctor Test")
    doc.register()
    sql_user = Doctor.query.all() #Postgres Data
    
    keys = [] # MongoDB Data
    air_bnb_data = mongo.db.listingsAndReviews.find()[2] # NoSQL Getting data from collection (MONGO)
    for key in air_bnb_data:
        keys.append(key)
    both_data: List[List, str] = keys, f"{sql_user}"
    return jsonify(both_data)
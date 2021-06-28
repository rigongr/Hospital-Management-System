from typing import List
from flask import jsonify, Blueprint
from hms import mongo, db
from hms.models import Doctor, Pharmacy, Drug, Patient, Appointment
from logger.logger import write_log
import random
from datetime import datetime

users = Blueprint('users', __name__)

users_collection = mongo.db.listingsAndReviews

# sanity check route
@users.route('/ping', methods=['GET'])
def ping_pong():
    users = Doctor.query.all()
    pharmacies = Pharmacy.query.all()

    for user in users and pharmacies:

        db.session.delete(user)
        db.session.commit()

    pharmacy = Pharmacy(f"Pharmacy{random.randint(0, 999)}", f"pharmacy{str(random.randint(0, 99999))}@gmail.com", "testing123", random.randint(0, 123456),  random.randint(0, 2000))
    pharmacy.register()

    doc = Doctor(f"Doctor{random.randint(0, 999)}", f"doctor{str(random.randint(0, 99999))}@gmail.com", "testing123", random.randint(0, 123456),  "Doctor Test")
    doc.register()
    
    pat = Patient(f"Patient{random.randint(0,999)}", 123456, f"patient{str(random.randint(0,999))}@gmail.com", "patient123", "Prishtina")
    pat.register()

    appointment = Appointment(datetime.today(), "Buy this... buy that... whatever", pat.id, doc.id)
    appointment.register()

    
    drug = Drug('Ibuprofen', 0.25, 253, 1)
    drug.register()
    
    drug2 = Drug('Paracetamol', 0.50, 532, 1)
    drug2.register()
    
    sql_user = Doctor.query.all() #Postgres Data
    
    keys = [] # MongoDB Data
    air_bnb_data = mongo.db.listingsAndReviews.find()[2] # NoSQL Getting data from collection (MONGO)
    for key in air_bnb_data:
        keys.append(key)
    both_data: List[List, str] = keys, f"{sql_user}"
    return jsonify(both_data)
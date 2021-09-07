from typing import List

from flask import jsonify, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from hms import client
from hms.models import Doctor, Pharmacy, Drug, Patient, Appointment

from logger.logger import write_log


users = Blueprint('users', __name__)

db = client.hms_db
users_collection = db.users


@users.route('/ping', methods=['GET'])
def ping_pong():
    
    doc = Doctor("Doc1", "Filan Fisteku", 38349700700, "ff@gmail.com", "bajram curri", "filan123", "Heart Surgeon")

    doc.register("Doc1", "Filan Fisteku", 38349700700, "ff@gmail.com", "bajram curri", "filan123", "Heart Surgeon")
    
    login_user(doc)

    return doc.json()
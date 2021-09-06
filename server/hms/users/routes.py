from typing import List

from flask import jsonify, Blueprint

from hms import client
from hms.models import Doctor, Pharmacy, Drug, Patient, Appointment

from logger.logger import write_log


users = Blueprint('users', __name__)

db = client.hms_db
users_collection = db.users

# sanity check route
@users.route('/ping', methods=['GET'])
def ping_pong():
    return 'pong'
from os import write
from typing import List, Optional

from flask import jsonify, Blueprint, request
from flask_login import login_user, current_user, logout_user, login_required

from hms import client
from hms.models import Doctor

from logger.logger import write_log


users = Blueprint('users', __name__)

db = client.hms_db
users_collection = db.users


@users.route('/ping', methods=['GET', 'POST'])
def ping_pong():
    if request.method == 'POST':
        write_log('POST METHOD')
        write_log(request.get_json())
        
    doc = Doctor("Doc1", "Filan Fisteku", 38349700700, "ff@gmail.com", "bajram curri", "filan123", "Heart Surgeon")

    doc.register("Doc1", "Filan Fisteku", 38349700700, "ff@gmail.com", "bajram curri", "filan123", "Heart Surgeon")
    
    login_user(doc)
    return doc.json()
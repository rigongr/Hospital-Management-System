from os import write
from typing import List, Optional

from flask import jsonify, Blueprint, request
from flask.wrappers import Response
from flask_login import login_user, current_user

from backend.hms import client, bcrypt
from backend.hms.models import Doctor, Patient
from backend.utils.token_generator import generate_login_token
from backend.logger.logger import write_log


users = Blueprint('users', __name__)

db = client.hms_db

patients_collection = db.patients


@users.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        payload = request.get_json()
        username = payload["username"]
        full_name = payload["full_name"]
        email = payload["email"]
        phone = payload["phone"]
        street_address = payload["street_address"]
        pw = payload["password"]
        password = bcrypt.generate_password_hash(pw).decode('utf-8')
        find_user = Patient.get_by_email(email)
        if find_user is None:
            Patient.register(username, full_name, phone, email, password, street_address)
            return {
                "status_code": 201, 
                "status": "Created", 
                "detail": "Patient registered successfully. He may now continue to log in."
            }, 200
        else:
            return {
                "status_code": 304, 
                "status": "Not Modified", 
                "detail": "This email already exists. Please, choose another one. "
            }, 404
    else:
        return {
            "status_code": 304,
            "status": "Method not allowed"
        }


@users.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        payload = request.get_json()
        email = payload["email"]
        password = payload["password"]
        find_user = patients_collection.find_one({"email": email})
        if Patient.login_valid(email, password) and find_user is not None:
            return jsonify({
                "status": 'Success',
                "status_code": 200,
                "detail": "Log in successful.",
                "access_token": generate_login_token(),
            }), 200
        else:
            return {
                "status_code": 404,
                "status": "Error",
                "detail": "Wrong email/password. Please, try again."
            }, 404

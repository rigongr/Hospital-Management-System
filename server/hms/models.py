from flask.wrappers import Request
from pymongo import HASHED
import requests
from requests.exceptions import RequestException
from requests.models import HTTPError
from . import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, default=1)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)
    speciality = db.Column(db.String(100), default="Newbie Doctor")

    def __repr__(self):
        return f"""
                Doctor ID: {self.id},
                Full name: {self.full_name},
                Phone number: {self.phone_number},
                Email: {self.email},
                Speciality: {self.speciality}

        """
    def __init__(self, full_name, email, password, phone_number, speciality):
        self.full_name = full_name
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.speciality = speciality
    

    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
        except RequestException as error:
            print(error)


class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.Integer)
    total_stock = db.Column(db.Integer, default=100)
    drugs = db.relationship('Drug', backref='pharmacy', lazy=True)

    def __init__(self, name, email, password, phone, total_stock):
        self.total_stock = total_stock
        self.email = email
        self.name = name
        self.phone = phone
        self.password = password

    def __repr__(self):
        return f"""
                Pharmacy ID: {self.id},
                Pharmacy Name: {self.name},
                Total Stock: {self.total_stock},
                Email: {self.email},
                Phone: {self.phone},
                Drugs: {self.drugs},
        """

    def id_to_name(id):
        pharmacy = Pharmacy.query.filter_by(id=id).first()
        pharmacy_name = pharmacy.name
        return pharmacy_name
    
    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
        except RequestException as error:
            print(error)


class Drug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)
    pharmacy_id = db.Column(db.Integer, db.ForeignKey('pharmacy.id'), default=1)


    def __init__(self, name, price_per_unit, quantity, pharmacy_id):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.pharmacy_id = pharmacy_id
    
    def __repr__(self):
        id = self.pharmacy_id
        pharmacy_name = Pharmacy.id_to_name(id)
        return f"""
                Drug name: {self.name},
                Price per unit: {self.price_per_unit}$,
                Quantity: {self.quantity},
                Pharmacy: {pharmacy_name}
        """

    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
        except RequestException as error:
            print(error)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(50), nullable=False)
#    # email = db.Column(db.String(120), unique=True, nullable=False)
#    # created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#    # last_login = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def json(self):
#         return {
#             "username": self.username,
#             "password": self.password,
#         }
    
#     def user_register(uname: str, password: str):

#         if (uname and password):
#             user = User(username=uname, password=password)

#             try:
#                 db.session.add(user)
#                 db.session.commit()
#             except RequestException as error:
#                 print(error)
#         else:
#             raise HTTPError
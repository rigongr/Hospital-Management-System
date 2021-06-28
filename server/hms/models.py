from flask import app
from flask.wrappers import Request
import requests
from requests.exceptions import RequestException
from requests.models import HTTPError
from . import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



# # # # # Appointment model # # # # # 

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    prescription = db.Column(db.String(500))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), default=1)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), default=1)

    def __init__(self, date, prescription, patient_id, doctor_id):
        self.date = date
        self.prescription = prescription
        self.patient_id = patient_id
        self.doctor_id = doctor_id
    
    
    def __repr__(self):
        return f"""
                Date: {self.date},
                Prescription: {self.prescription},
                From Doctor {self.doctor_id} to Patient {self.patient_id}.
        """


    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
        except RequestException as error:
            print(error)



# # # # # Patient model # # # # #

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, default=1)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)
    home_address = db.Column(db.String(120))
    appointments = db.relationship('Appointment', backref='patient', lazy=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), default=1)


    def __repr__(self):
        return f"""
                Patient ID: {self.id},
                Full name: {self.full_name},
                Phone number: {self.phone_number},
                Email: {self.email},
                Home address: {self.home_address},
                Appointments: {self.appointments},
                Doctor: {self.doctor_id},
        """
    

    def __init__(self, full_name, phone_number, email, password, home_address):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.home_address = home_address
    

    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
        except RequestException as error:
            print(error)



# # # # # Doctor model # # # # #

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, default=1)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)
    speciality = db.Column(db.String(100), default="Newbie Doctor")
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
    patients = db.relationship('Patient', backref='doctor', lazy=True)


    def __init__(self, full_name, email, password, phone_number, speciality):
        self.full_name = full_name
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.speciality = speciality


    def __repr__(self):
        return f"""
                Doctor ID: {self.id},
                Full name: {self.full_name},
                Phone number: {self.phone_number},
                Email: {self.email},
                Speciality: {self.speciality},
                Appointments: {self.appointments},
                Patients: {self.patients}

        """


    def register(self):
        try:
            db.session.add(self)
            db.session.commit()
        except RequestException as error:
            print(error)
    

    def id_to_name(id):
        doctor = Doctor.query.filter_by(id=id).first()
        doctor_name = doctor.name
        return doctor_name
    



# # # # # Pharmacy model # # # # # 

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



# # # # #  Drug model  # # # # # 

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
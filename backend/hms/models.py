from backend.logger.logger import write_log
import datetime
import os
import uuid


from flask import session
from flask_login import UserMixin

from backend.hms import client, bcrypt, login_manager


today_skeleton_format = datetime.datetime.today()
today = today_skeleton_format.strftime("%b %d %Y %H:%M:%S")

db = client.hms_db

patients_collection = db.patients
doctors_collection = db.doctors
pharmacies_collection = db.pharmacies
departments_collection = db.departments


class UserBaseModel(UserMixin):
    
    def __init__(self, username, full_name, phone, email, password, street_address=None, date_registered=None, _id=None):
        self.username = username
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.password = password
        self.street_address = None if street_address is None else str(street_address)
        self.date_registered = today
        self._id = uuid.uuid4().hex if _id is None else str(_id)

    def is_authenitcated(self):
        return self._authenticated

        
    def is_anonymous(self):
        return False

    def is_active(self):
        return True


    def get_id(self):
        return self.username
    

# # # # # Doctor model # # # # # 
class Doctor(UserBaseModel):

    def __init__(self, username, full_name, phone, email, password, street_address, speciality, date_registered=None, _id=None):
        super().__init__(username, full_name, phone, email, password, street_address, date_registered, _id)
        self.speciality = speciality


    @classmethod 
    def get_by_username(cls, username):
        user = doctors_collection.find_one({"username" : username})
        if user is not None:
            return cls(**user)


    @classmethod 
    def get_by_email(cls, email):
        user = doctors_collection.find_one({"email" : email})
        if user is not None:
            return cls(**user)


    @staticmethod
    def login_valid(email, password):
        verify_user = Doctor.get_by_email(email)
        if verify_user is not None:
            return bcrypt.check_password_hash(verify_user.password, password)
        return False


    @classmethod
    def register(cls, username, full_name, phone, email, password, street_address, speciality):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(username, full_name, phone, email, password, street_address, speciality)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False

    def json(self):
        return {
            "username": self.username,
            "full_name": self.full_name,
            "phone": self.phone,
            "street_address": self.street_address,
            "email": self.email,
            "password": self.password,
            "speciality": self.speciality,
            "date_registered": self.date_registered
        }
        
    def save_to_mongo(self):
        doctors_collection.insert(self.json())


# # # # # Patient model # # # # #

class Patient(UserBaseModel):

    def __init__(self, username, full_name, phone, email, password, street_address, date_registered=None, _id=None):
        super().__init__(username, full_name, phone, email, password, street_address, date_registered, _id)
    

    @classmethod 
    def get_by_username(cls, username):
        user = patients_collection.find_one({"username" : username})
        if user is not None:
            return cls(**user)


    @classmethod 
    def get_by_email(cls, email):
        user = patients_collection.find_one({"email" : email})
        if user is not None:
            return cls(**user)


    def save_to_mongo(self):
        patients_collection.insert(self.json())
        

    @classmethod
    def register(cls, username, full_name, phone, email, password, street_address):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(username, full_name, phone, email, password, street_address)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False


    @staticmethod
    def login_valid(email, password):
        verify_user = Patient.get_by_email(email)
        if verify_user is not None:
            write_log(verify_user.street_address)
            return bcrypt.check_password_hash(verify_user.password, password)
        return False

    def json(self):
        return {
            "username": self.username,
            "full_name": self.full_name,
            "phone": self.phone,
            "street_address": self.street_address,
            "email": self.email,
            "password": self.password,
            "date_registered": self.date_registered
        }

        
# # # # # Pharmacy model # # # # #

class Pharmacy():
    ...

    def __init__(self):
        ...

    def __repr__(self):
        ...
    
    

    def register(self):
        ...



# # # # # Appointment model # # # # #

class Appointment():
    ...


    def __init__(self):
        ...


    def __repr__(self):
        ...


    def register(self):
        ...
    

    def id_to_name(id):
        ...


# # # # #  Drug model  # # # # # 

class Drug():
    ...


    def __init__(self):
        ...
    
    def __repr__(self):
        ...

    def register(self):
        ...


class Department():

    def __init__ (self, name, _id=None):
        self.name = name
        self._id = _id if id is not None else str(_id)

    @classmethod
    def register(cls, name):
        department = cls.get_by_name(name)
        if department is None:
            new_department = cls(name)
            new_department.save_to_mongo()
            return True
        else:
            return {
                "status": "Not Modified",
                "status_code": "302",
                "detail": "Department already exists."
            }


    @classmethod
    def get_by_name(cls, name):
        department = departments_collection.find_one({"name": name})
        if department is not None:
            return cls(**department)


    def list_all_departments():
        departments = {}
        all_departments = departments_collection.find()
        for department in all_departments:
            departments.append({"name": department})
        if len(department) == 0:
            return {
                "status": "Success",
                "status_code": "304",
                "detail": "No departments are avilable."
            }
        return {
            "status": "Success",
            "status_code": 200,
            "departments": departments
        }


    def json(self):
        return {
            "name": self.name
        }


    def save_to_mongo(self):
        departments_collection.insert(self.json())


@login_manager.user_loader
def load_user(username):
    user = patients_collection.find_one({'username' : username})
    if not user:
        return None
    a = UserBaseModel(username=user['username'], email=user['email'], password=user['password'])
    return a
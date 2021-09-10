import os
import uuid

from datetime import date

from flask import session
from flask_login import UserMixin

from hms import client, bcrypt, login_manager


today = date.today()

db = client.hms_db
users_collection = db.users
pharmacies_collection = db.pharmacies


class UserBaseModel(UserMixin):
    
    def __init__(self, username, full_name, phone, email, street_address, password, _id=None, date_registered=today):
        self.username = username
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.street_address = street_address
        self.password = password
        self.date_registered = date_registered
        self._id = uuid.uuid4().hex if _id is None else str(_id)

    def is_authenitcated(self):
        return self._authenticated

        
    def is_anonymous(self):
        return False

    def is_active(self):
        return True


    def get_id(self):
        return self.username


    @classmethod 
    def get_by_username(cls, username):
        user = users_collection.find_one({"username" : username})
        if user is not None:
            return cls(**user)


    @classmethod 
    def get_by_email(cls, email):
        user = users_collection.find_one({"email" : email})
        if user is not None:
            return cls(**user)


    @staticmethod
    def login_valid(email, password):
        verify_user = UserBaseModel.get_by_email(email)
        if verify_user is not None:
            return bcrypt.check_password_hash(verify_user.password, password)
        return False


    @classmethod
    def register(cls, username, full_name, phone, email, street_address, password, speciality):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(username, full_name, phone, email, street_address, password, speciality)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False


# # # # # Doctor model # # # # # 
class Doctor(UserBaseModel):

    def __init__(self, username, full_name, phone, email, street_address, password, speciality, _id=None):
        super().__init__(username, full_name, phone, email, street_address, password, _id)
        self.speciality = speciality


    def json(self):
        return {
            "username": self.username,
            "full_name": self.full_name,
            "phone": self.phone,
            "street_address": self.street_address,
            "speciality": self.speciality,
            "email": self.email,
            "password": self.password,
            "speciality": self.speciality
        }


    def save_to_mongo(self):
        users_collection.insert(self.json())


# # # # # Pharmacy model # # # # #

class Patient():
    ...

    def __init__(self):
        ...

    def __repr__(self):
        ...
    
    

    def register(self):
        ...
        

# # # # # Patient model # # # # #

class Patient():
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


@login_manager.user_loader
def load_user(username):
    user = users_collection.find_one({'username' : username})
    if not user:
        return None
    a = UserBaseModel(username=user['username'], email=user['email'], password=user['password'])
    return a
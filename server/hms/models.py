from . import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
   # email = db.Column(db.String(120), unique=True, nullable=False)
   # created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   # last_login = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            "username": self.username,
            "password": self.password,
        }
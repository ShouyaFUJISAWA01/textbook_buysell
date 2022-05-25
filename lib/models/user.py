from email.policy import default
from lib.db import db
import datetime

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    tel = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    updated = db.Column(db.DateTime, nullable=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    book = db.relationship('Book', backref='user', uselist=False)
    
    def __init__(self, name, address, tel, email, password, updated):
        self.name = name
        self.address = address
        self.tel = tel
        self.email = email
        self.password = password
        self.updated = updated
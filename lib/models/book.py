from lib.db import db
from datetime import datetime

class Book(db.Model):
    
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    isbn_no = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    updated = db.Column(db.DateTime, nullable=True)
    created = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, user_id, isbd_no, title, author, publisher, price, category, status, updated):
        self.user_id = user_id
        self.isbn_no = isbd_no
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.category = category
        self.status = status
        self.updated = updated
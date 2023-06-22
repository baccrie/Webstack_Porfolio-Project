from ShopWE import app, db
from uuid import uuid4, UUID
from datetime import datetime


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(30), unique=True, nullable=False)
    last_name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50))
    date_created = db.Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Admin - {self.username}'

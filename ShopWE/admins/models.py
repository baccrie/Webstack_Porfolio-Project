from ShopWE import app, db
from uuid import uuid4, UUID
from datetime import datetime
from ShopWE.blog.models import Post, Comment


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(30), unique=True, nullable=False)
    last_name = db.Column(db.String(30), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False, unique=True)

    password = db.Column(db.String(50))
    date_created = db.Column(DateTime, default=datetime.utcnow)

    # Relationships
    posts = db.relationship('Post', backref='author')
    comments = db.relationship('Comment', backref='author')


    def __repr__(self):
        return f'Admin - {self.username}'

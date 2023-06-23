from ShopWE import app, db
from ShopWE.products.models import Product
from ShopWE.blog.models import Comment

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    orgnanisation_phone_number = db.Column(db.String(30), nullable=False, unique=True)

    password = db.Column(db.String(50))
    date_created = db.Column(DateTime, default=datetime.utcnow)

    products = db.relationship('Product', backref='owner')

    # Relationship
    comments = db.relationship('Comment', backref='author')
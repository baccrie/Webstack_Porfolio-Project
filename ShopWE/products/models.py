from ShopWE import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=False)
    price = db.Column(db.Numeric(), default=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    image_1 = db.Column(db.String(150), nullable=False, default='image_1.jpg')
    image_1 = db.Column(db.String(150), nullable=False, default='image_1.jpg')
    image_1 = db.Column(db.String(150), nullable=False, default='image_1.jpg')

    brand_id = db.Column(db.Integer, nullable=False, db.ForeignKey('brand.id'))
    category_id = db.Column(db.Integer, nullable=False, db.ForeignKey('category.id'))



class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    products = db.relationship('Product', backref='brand')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    products = db.relationship('Product', backref='category')




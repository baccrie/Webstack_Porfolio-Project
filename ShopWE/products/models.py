from ShopWE import db
from datetime import datetime
from ShopWE.vendors.models import Vendor

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
    vendor_id = db.Column(db.Integer, nullable=False, db.ForeignKey('vendor.id'))

    def __repr__(self):
        return f'Product - {self.name}'

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    products = db.relationship('Product', backref='brand')

    def __repr__(self):
        return f'Brand - {self.name}'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    products = db.relationship('Product', backref='category')

    def __repr__(self):
        return f'Category - {self.name}'
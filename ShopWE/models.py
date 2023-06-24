from ShopWE import db, login_manager
from datetime import datetime
from flask import session
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    user_type = session.get('type')
    if user_type == 'Admin':
        return Admin.query.get(int(id))
    elif user_type == 'Vendor':
        return Vendor.query.get(int(id))
    elif user_type == 'Customer':
        return Customer.query.get(int(id))



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=False)
    price = db.Column(db.Numeric(8, 1), default=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    

    image_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image.jpg')

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))

    def __repr__(self):
        return f'Product - {self.name}'

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    products = db.relationship('Product', backref='brand')
    image = db.Column(db.String(150), nullable=False, default='brand.jpg')

    def __repr__(self):
        return f'Brand - {self.name}'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    products = db.relationship('Product', backref='category')
    image = db.Column(db.String(150), nullable=False, default='category.jpg')

    def __repr__(self):
        return f'Category - {self.name}'

class Vendor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(30), nullable=False, unique=True)

    password = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    image_1 = db.Column(db.String(150), nullable=False, default='vendor.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='vendor.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image.jpg')

    # Relationship
    comments = db.relationship('Comment', backref='posterV')
    products = db.relationship('Product', backref='owner')

    def __repr__(self):
        return f'Vendor - {self.name}'

class Admin(db.Model, UserMixin):
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
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    posts = db.relationship('Post', backref='poster')
    comments = db.relationship('Comment', backref='posterA')


    def __repr__(self):
        return f'Admin - {self.username}'
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    # Relationships
    comments = db.relationship('Comment', backref='post')
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))

    def __repr__(self):
        return f'Post - {self.title}'

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False, unique=True)

    password = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    comments = db.relationship('Comment', backref='posterC')

    def __repr__(self):
        return f'Customer - {self.username}'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    # Relationships
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))


    def __repr__(self):
        return f'Comment'
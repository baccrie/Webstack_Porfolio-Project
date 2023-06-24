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

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))

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

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(30), nullable=False, unique=True)

    password = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    comments = db.relationship('Comment', backref='posterV')
    products = db.relationship('Product', backref='owner')



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


class Customer(db.Model):
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

    # Relationship
    comments = db.relationship('Comment', backref='posterC')


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
        return f'Customer - {self.username}'
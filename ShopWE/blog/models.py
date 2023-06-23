from ShopWE import app, db
from ShopWE.admins.models import Admin
from ShopWE.customers.models import Customer
from ShopWE.vendors.models import Vendor

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    # Relationships
    comments = db.relationship('Comment', backref='post')
    poster_id = db.Column(db.Integer, db.ForeignKey('admin.id'))







class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    # Relationships
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    customer_id = db.Column(db.Integer, db.Foreignkey('customer.id'))


    
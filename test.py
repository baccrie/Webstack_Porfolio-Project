#!/usr/bin/python3
from ShopWE import app, db
from ShopWE.models import Admin, Vendor, Post, Product, Category, Brand, Comment, Customer


app.app_context().push()
"""
db.create_all()

# create Brand ansd Category
brand1 = Brand(name='Oraimo')
category1 = Category(name='Electronics')

# Create a vendor
vendor1 = Vendor(name='Alasks shop', email='bakarerilwan1@gmail.com', country='Nigeria', state='Oyo', city='Ibadan', phone='63t79y8900y3')


db.session.add(vendor1)
db.session.add(brand1)
db.session.add(category1)
db.session.commit()

# Product
vend = Vendor.query.filter_by(id=1).first()
bra = Brand.query.filter_by(id=1).first()
cat = Category.query.filter_by(id=1).first()

product1 = Product(name='Freepod 4', description='tmp', vendor_id = vend.id, brand_id=bra.id, category_id=cat.id)
db.session.add(product1)
db.session.commit()
"""
product = Product.query.first()
print(product.owner)
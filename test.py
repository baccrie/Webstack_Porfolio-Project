#!/usr/bin/python3
from ShopWE import app, db
from ShopWE.models import Admin, Vendor, Post, Product, Category, Brand, Comment, Customer


app.app_context().push()
db.create_all()

# create Brand ansd Category
cust = Customer(username='baccrie', email='bakarerilwan1@gmail.com', first_name='Rilwan', last_name='Bakare', country='Nigeria', state='Oyo', city='Ibadan', phone_number='09099983887')
db.session.add(cust)
db.session.commit()
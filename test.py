#!/usr/bin/python3
from ShopWE import app, db
from ShopWE.models import Admin, Vendor, Post, Product, Category, Brand, Comment, Customer


app.app_context().push()


brand2 = Brand(name='Techno')
brand3 = Brand(name='Toshiba')
brand4 = Brand(name='Hp')
brand5 = Brand(name='Samsung')
brand6 = Brand(name='LG')
brand7 = Brand(name='Itel')

cat2 = Category(name='Mobile')
cat3 = Category(name='Phones and accessories')
cat4 = Category(name='Clothing')
cat5 = Category(name='Shoe')
cat6 = Category(name='Laptop')

db.session.add(brand2)
db.session.add(brand3)
db.session.add(brand4)
db.session.add(brand5)
db.session.add(brand6)
db.session.add(brand7)

db.session.add(cat2)
db.session.add(cat3)
db.session.add(cat4)
db.session.add(cat5)
db.session.add(cat6)


db.session.commit()
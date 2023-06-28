from flask import request, render_template, url_for, redirect
from ShopWE import app
from ShopWE.models import Category, Brand, Product
from ShopWE.models import Admin, Customer, Comment, Vendor, Post


def brands():
    brands = Brand.query.all()
    return brands

def categories():
    categories = Category.query.all()
    return categories

@app.route('/')
@app.route('/home')
def home():
    products = Product.query.all()
    return render_template('home.html', brands=brands(), categories=categories(), products=products)
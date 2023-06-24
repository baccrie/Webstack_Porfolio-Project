from flask import request, render_template, url_for, redirect
from ShopWE import app
from ShopWE.models import Category, Brand, Product
# from ShopWE import Admin, Customer, Comment, Vendor, Post


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
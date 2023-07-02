from flask import request, render_template, url_for, redirect
from ShopWE import app
from ShopWE.models import Category, Brand, Product
from ShopWE.models import Admin, Customer, Comment, Vendor, Post
from ShopWE.generic import brands, categories, posts

@app.route('/')
@app.route('/home')
def home():
    products = Product.query.all()
    posts = Post.query.limit(4).all()
    return render_template('home.html', brands=brands(), categories=categories(), products=products, posts=posts)


@app.route('/test')
def test():
    products = Product.query.all()
    return render_template('test.html', products=products)
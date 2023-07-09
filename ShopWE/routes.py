from flask import request, render_template, url_for, redirect
from ShopWE import app
from ShopWE.models import Category, Brand, Product
from ShopWE.models import Admin, Customer, Comment, Vendor, Post
from ShopWE.generic import brands, categories, posts
from flask_login import current_user


@app.route('/')
@app.route('/home')
def home():
    brands = Brand.query.join(Product, (Brand.id == Product.brand_id)).all()
    categories = Category.query.join(Product, (Category.id == Product.category_id)).all()
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=5)
    posts = Post.query.limit(4).all()
    return render_template('home.html', brands=brands, categories=categories, products=products, posts=posts)

@app.route('/home/products/brands/<string:name>')
def brands(name):
    brand_id = Brand.query.filter_by(name=name).first()
    brands = Brand.query.join(Product, (Brand.id == Product.brand_id)).all()
    categories = Category.query.join(Product, (Category.id == Product.category_id)).all()
    page = request.args.get('page', 1, type=int)
    products = Product.query.filter_by(brand_id=brand_id.id).paginate(page=page, per_page=2)
    posts = Post.query.limit(4).all()
    return render_template('brand_home.html', brands=brands, categories=categories, products=products, posts=posts)

@app.route('/home/products/categories/<string:name>')
def categories(name):
    category_id = Category.query.filter_by(name=name).first()
    categories = Category.query.join(Product, (Category.id == Product.category_id)).all()
    brands = Brand.query.join(Product, (Brand.id == Product.brand_id)).all()
    page = request.args.get('page', 1, type=int)
    products = Product.query.filter_by(category_id=category_id.id).paginate(page=page, per_page=3)
    posts = Post.query.limit(4).all()
    return render_template('category_home.html', brands=brands, categories=categories, products=products, posts=posts)

@app.route('/test')
def test():
    products = Product.query.all()
    return render_template('test.html', products=products)
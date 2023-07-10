from flask import request, render_template, url_for, redirect
from ShopWE import app
from ShopWE.models import Category, Brand, Product
from ShopWE.models import Admin, Customer, Comment, Vendor, Post
from ShopWE.generic import brands, categories, posts
from flask_login import current_user


@app.route('/')
@app.route('/home')
def home():
    """
    Display all product and also paginating
    """
    brands = Brand.query.join(Product, (Brand.id == Product.brand_id)).all()
    categories = Category.query.join(Product, (Category.id == Product.category_id)).all()
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=15)
    posts = Post.query.limit(4).all()
    return render_template('home.html', brands=brands, categories=categories, products=products, posts=posts)

@app.route('/home/products/brands/<string:name>')
def brands(name):
    """
    Display all product filtered by brand
    """
    brand_id = Brand.query.filter_by(name=name).first()
    brands = Brand.query.join(Product, (Brand.id == Product.brand_id)).all()
    categories = Category.query.join(Product, (Category.id == Product.category_id)).all()
    page = request.args.get('page', 1, type=int)
    products = Product.query.filter_by(brand_id=brand_id.id).paginate(page=page, per_page=2)
    posts = Post.query.limit(4).all()
    return render_template('brand_home.html', brands=brands, categories=categories, products=products, posts=posts)

@app.route('/home/products/categories/<string:name>')
def categories(name):
    """
    Display all product filtered by category
    """
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

@app.errorhandler(404)
def page_not_found(e):
    """
    handling Client error
    """
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    """
    handling Server error
    """
    return render_template('error/500.html'), 404
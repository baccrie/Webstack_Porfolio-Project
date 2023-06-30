from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.customers.forms import CustomerRegister
from ShopWE.vendors.forms import VendorRegister
from ShopWE.auth.forms import Login
from ShopWE.models import Product, Vendor
from ShopWE.generic import brands, categories

product = Blueprint('product', __name__)

@product.route('/product/<int:id>', methods=['POST', 'GET'])
def singleproduct(id):
    product = Product.query.get_or_404(id)

    return render_template('product/product.html', product=product, brands=brands(), categories=categories())
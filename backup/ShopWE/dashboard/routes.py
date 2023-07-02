from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.customers.forms import CustomerRegister, UpdateCustomerInfo, UpdateCustomerPassword
from ShopWE.vendors.forms import VendorRegister, UpdateVendorInfo, UpdateVendorPassword
from ShopWE.auth.forms import Login
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Activity, Post, Admin
from ShopWE.dashboard.forms import Addproduct, Addbrand, Addcategory, Updateproduct
from ShopWE.generic import save_image
from flask import current_app
import os

dash = Blueprint('dash', __name__)

@dash.route('/dash/home')
@login_required
def home():
    form1 = Addbrand()
    posts = Post.query.limit(4).all()
    products = Product.query.order_by(Product.date.desc()).limit(5).all() 
    total = len(current_user.activities)
    last_five = total - 5
    activities = current_user.activities[last_five:total]
    return render_template('dashboard/home.html', form1=form1, posts=posts, products=products, activities=activities)



@dash.route('/dash/<int:id>/profile', methods=['POST', 'GET'])
@login_required
def profile(id):
    user_profile = Customer.query.get_or_404(id)
    form = UpdateCustomerInfo()
    form1 = UpdateCustomerPassword()

    print(form.errors)
    if request.method == 'POST':
        print(form.errors)
    if form.validate_on_submit():
        user_profile.email = form.email.data
        user_profile.username = form.username.data
        user_profile.first_name = form.first_name.data
        user_profile.last_name = form.last_name.data
        user_profile.country = form.country.data
        user_profile.state = form.state.data
        user_profile.city = form.city.data
        user_profile.address = form.address.data
        user_profile.number = form.number.data
        user_profile.about = form.about.data

        db.session.commit()
        flash(f'Successful', 'success')
        return redirect(url_for('dash.home'))
    
    
    form.email.data = current_user.email
    form.username.data = current_user.username
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.country.data = current_user.country
    form.state.data = current_user.state
    form.address.data = current_user.address
    form.city.data = current_user.city
    form.number.data = current_user.phone
    form.about.data = current_user.about
   

    return render_template('dashboard/profile.html', form=form, form1=form1)

@dash.route('/dash/addbrand', methods=['POST', 'GET'])
@login_required
def addbrand():
    if request.method == 'POST':
    #newBrand = Brand(name=form1.name.data)
        newBrand = request.method.get('name')
        db.session.add(newBrand)
        #db.session.commit()
        flash(f'Brand has been successfully added', 'success')
        return redirect(url_for('dash.addproduct'))

    return render_template('dashboard/home.html')
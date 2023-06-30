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

    if isinstance(current_user, Admin):
        user_profile = Admin.query.get_or_404(id)
        form = UpdateCustomerInfo()

    elif isinstance(current_user, Customer):
        print('Yes')
        form = UpdateCustomerInfo()
        form1 = UpdateCustomerPassword()
        user_profile = Customer.query.get_or_404(id)

        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.country.data = current_user.country
        form.state.data = current_user.state
        form.address.data = current_user.address
        form.city.data = current_user.city
        form.number.data = current_user.phone
        form.about.data = current_user.about

    elif isinstance(current_user, Vendor):
        user_profile = Vendor.query.get_or_404(id)
        form = UpdateVendorInfo()
        form1 = UpdateVendorPassword()
        print('yes')

        form.email.data = current_user.email
        form.name.data = current_user.name
        form.country.data = current_user.country
        form.state.data = current_user.state
        form.address.data = current_user.address
        form.city.data = current_user.city
        form.number.data = current_user.phone
        form.about.data = current_user.about

        print('yes')

    if form.validate_on_submit():
        print('no')

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
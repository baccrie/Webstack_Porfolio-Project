from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required
from ShopWE.customers.forms import CustomerRegister
from ShopWE.auth.forms import Login
from ShopWE.models import Customer

auth = Blueprint('auth', __name__)

@auth.route('/auth/login', methods=['POST', 'GET'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Successfully Login', 'primary')
            return redirect(url_for('home'))
        elif user and not bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'Invalid password', 'primary')
        elif not user:
            flash(f'user dosent exist', 'primary')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)

@auth.route('/auth/customer/register', methods=['POST', 'GET'])
def customer_register():
    form = CustomerRegister()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        customer = Customer(username=form.username.data, email=form.email.data, first_name=form.first_name.data,
                            last_name=form.last_name.data, country=form.country.data, state=form.state.data, city=form.city.data,
                            phone_number=form.number.data, password=hashed_password)
        db.session.add(customer)
        # db.session.commit()
        flash(f'Welcome home {customer.username}', 'success')
        return redirect(url_for('home'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
def logout():
    return 'Succussfully logged out'
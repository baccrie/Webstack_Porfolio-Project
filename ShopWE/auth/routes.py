from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required
from ShopWE.customers.forms import CustomerRegister
from ShopWE.models import Customer

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Successfully Logged In'

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
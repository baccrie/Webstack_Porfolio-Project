from ShopWE import app, db
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required
from ShopWE.customers.forms import CustomerRegister

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Successfully Logged In'

@auth.route('/auth/customer/register', methods=['POST', 'GET'])
def customer_register():
    form = CustomerRegister()

    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
def logout():
    return 'Succussfully logged out'
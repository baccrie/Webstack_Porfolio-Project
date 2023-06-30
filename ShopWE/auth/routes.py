from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.customers.forms import CustomerRegister
from ShopWE.vendors.forms import VendorRegister
from ShopWE.auth.forms import Login
from ShopWE.models import Customer, Vendor, Admin, Activity

auth = Blueprint('auth', __name__)

@auth.route('/auth/login', methods=['POST', 'GET'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()
        if not user:
            user = Vendor.query.filter_by(email=form.email.data).first()
        if not user:
            user = Admin.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if isinstance(user, Customer):
                session['type'] = 'Customer'
                new_activity = Activity(content='You logged in', category='success', customer_id=user.id)

            elif isinstance(user, Vendor):
                session['type'] = 'Vendor'
                new_activity = Activity(content='You logged in', category='success', vendor_id=user.id)
    
            elif isinstance(user, Admin):
                session['type'] = 'Admin'
                new_activity = Activity(content='You logged in', category='success', admin_id=user.id)

            db.session.add(new_activity)
            print(new_activity.category)
            db.session.commit()
            login_user(user)
            flash('Successfully Login', 'primary')
            print(current_user.email)
            print(session['type'])
            return redirect(url_for('home'))
        elif user and not bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'Invalid password', 'danger')
        elif not user:
            flash(f'user dosent exist', 'danger')
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
        new_activity = Activity(content='Your account was registered', customer_id=customer.id)
        db.session.add(new_activity)
        db.session.commit()
        flash(f'Successfully registerd pls login!', 'primary')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, role='customer')


@auth.route('/auth/vendor/register', methods=['POST', 'GET'])
def vendor_register():
    form = VendorRegister()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        vendor = Vendor(name=form.name.data, email=form.email.data, country=form.country.data,
                        state=form.state.data, city=form.city.data,
                            phone=form.number.data, password=hashed_password)
        
        db.session.add(vendor)
        new_activity = Activity(content='Your account was registered', vendor_id=vendor.id, category='success')
        db.session.add(new_activity)

        #db.session.commit()
        flash(f'Successfully registered pls login!', 'primary')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, role='vendor')


@auth.route('/logout')
def logout():
    if not current_user.is_authenticated:
        flash('You re not logged in pls login first!', 'danger')
        return redirect(url_for('auth.login'))
    
    if isinstance(current_user, Customer):
        new_activity = Activity(content='You logged out', category='danger', customer_id=current_user.id)

    if isinstance(current_user, Vendor):
        new_activity = Activity(content='You logged out', category='danger', vendor_id=current_user.id)
    
    if isinstance(current_user, Admin):
        new_activity = Activity(content='You logged out', category='danger', admin_id=current_user.id)

    db.session.add(new_activity)
    db.session.commit()
    logout_user()
    flash('Logout successful', 'success')
    return redirect(url_for('auth.login'))
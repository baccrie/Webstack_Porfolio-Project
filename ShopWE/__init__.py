from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_migrate import Migrate
from ShopWE.dashboard.forms import Addbrand, Addcategory
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E-Commerce.db'
app.config['SECRET_KEY'] = 'hbaq78gqidbiq8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
ckeditor = CKEditor(app)
login_manager = LoginManager(app)

"""
@app.context_processor
def base():
    form1 = Addbrand
    return dict(form1=form1)
"""


from ShopWE.auth.routes import auth
from ShopWE.customers.routes import customer
from ShopWE.dashboard.routes import dash
from ShopWE.blog.routes import blog
from ShopWE import routes

app.register_blueprint(auth)
app.register_blueprint(customer)
app.register_blueprint(dash)
app.register_blueprint(blog)

login_manager.login_view = 'auth.login'
login_manager.login_message = 'You must log-in to access this page'
login_manager.login_message_category = 'danger'
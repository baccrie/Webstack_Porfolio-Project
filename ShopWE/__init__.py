from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E-Commerce.db'
app.config['SECRET_KEY'] = 'hbaq78gqidbiq8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from ShopWE.auth.routes import auth
from ShopWE.customers.routes import customer
from ShopWE import routes

app.register_blueprint(auth)
app.register_blueprint(customer)

login_manager.login_view = 'auth.login'
from flask import Flask, redirect, url_for, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E-Commerce.db'
app.config['SECRET_KEY'] = 'hj6usgj76duabjahyuUgy'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# login_manager = LoginManager(app)

from ShopWE import routes
from ShopWE.auth.routes import auth

# login_manager.login_view = 'auth.login'
# login_manager.login_message = 'You must log-in to access this page'
# login_manager.login_message_category = 'info'


app.register_blueprint(auth)

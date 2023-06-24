from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E-Commerce.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from ShopWE.auth.routes import auth
from ShopWE import routes

app.register_blueprint(auth)
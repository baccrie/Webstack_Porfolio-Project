from flask import Flask, redirect, url_for, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E-Commerce.db'


db = SQLAlchemy(app)



# app.register_blueprint(customers)
from ShopWE import routes



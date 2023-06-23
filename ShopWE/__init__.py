from flask import Flask, redirect, url_for, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E-Commerce.db'
app.config['SECRET_KEY'] = 'hj6usgj76duabjahyuUgy'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)




# app.register_blueprint(customers)
from ShopWE import routes
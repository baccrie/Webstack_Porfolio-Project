from flask import Flask, redirect, url_for, render_template
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
# from ShopWE.customers.routes import customers


app = Flask(__name__)
# app.register_blueprint(customers)
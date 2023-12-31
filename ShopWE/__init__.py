from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_migrate import Migrate
from ShopWE.dashboard.forms import Addbrand, Addcategory
from flask_ckeditor import CKEditor
from sqlalchemy import MetaData

'''
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
'''

#metadata = MetaData(naming_convention=convention)



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E-Commerce.db'
HOST = os.environ.get('MYSQL_HOST')
PASSWORD = os.environ.get('MYSQL_PASSWORD')
DATABASE = os.environ.get('MYSQL_DATABASE')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{PASSWORD}@{HOST}/{DATABASE}'
app.config['SECRET_KEY'] = 'hbaq78gqidbiq8'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db, render_as_batch=True)
ckeditor = CKEditor(app)
login_manager = LoginManager(app)



from ShopWE.auth.routes import auth
from ShopWE.customers.routes import customer
from ShopWE.dashboard.routes import dash
from ShopWE.blog.routes import blog
from ShopWE.products.routes import product
from ShopWE.carts.routes import cart
from ShopWE import routes

app.register_blueprint(auth)
app.register_blueprint(customer)
app.register_blueprint(dash)
app.register_blueprint(blog)
app.register_blueprint(product)
app.register_blueprint(cart)

login_manager.login_view = 'auth.login'
login_manager.login_message = 'You must log-in to access this page'
login_manager.login_message_category = 'danger'
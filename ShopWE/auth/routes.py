from ShopWE import app, db
from flask import Blueprint
from flask_login import login_required

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Successfully Logged In'
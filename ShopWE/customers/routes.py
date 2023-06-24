from flask import Blueprint, render_template, url_for
from ShopWE.customers.forms import CustomerRegister


customer = Blueprint('customer', __name__)
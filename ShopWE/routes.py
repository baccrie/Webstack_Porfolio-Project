from flask import request, render_template, url_for, redirect
from ShopWE import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


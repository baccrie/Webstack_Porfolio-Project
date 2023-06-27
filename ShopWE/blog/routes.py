from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Post, Comment
from ShopWE.blog.forms import Blogpost

blog = Blueprint('blog', __name__)

@blog.route('/dash/addpost')
@login_required
def addpost():
    form = Blogpost()

    return render_template('dashboard/add_post.html', form=form)

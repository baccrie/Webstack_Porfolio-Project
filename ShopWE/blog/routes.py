from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Post, Comment
from ShopWE.blog.forms import Blogpost, UpdateBlogPost

blog = Blueprint('blog', __name__)

@blog.route('/dash/addpost')
@login_required
def addpost():
    form = Blogpost()
    return render_template('dashboard/add_post.html', form=form)

@blog.route('/dash/<int:id>/updatepost', methods=['POST', 'GET'])
@login_required
def updatepost(id):
    form = UpdateBlogPost()
    post_to_update = Post.query.get_or_404(id)
    if form.validate_on_submit():
        pass

    form.title.data = post_to_update.title
    return render_template('dashboard/update_post.html', form=form)
from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Post, Comment, Admin
from ShopWE.blog.forms import Blogpost, UpdateBlogPost
from ShopWE.generic import save_image, category, brand

blog = Blueprint('blog', __name__)


@blog.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    return render_template('post/posts.html', posts=posts, categories=category(), brandsd=brand())



@blog.route('/dash/addpost', methods=['GET', 'POST'])
@login_required
def addpost():
    form = Blogpost()
    if not isinstance(current_user, Admin):
        flash(f'This page is only accessible to admins', 'danger')
        return redirect(url_for('home'))
    
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data)
        if form.image.data:
            image_name = save_image(form.image.data, 'blogposts')
            new_post.image_1 = image_name
        
        db.session.add(new_post)
        db.session.commit()
        flash(f'Posts successfully added', 'success')
        return redirect(url_for('blog.addpost'))
    
    return render_template('dashboard/add_post.html', form=form)

@blog.route('/dash/<int:id>/updatepost', methods=['POST', 'GET'])
@login_required
def updatepost(id):
    form = UpdateBlogPost()
    post_to_update = Post.query.get_or_404(id)

    if not isinstance(current_user, Admin):
        flash(f'This page is only accessible to admins', 'danger')
        return redirect(url_for('home'))
    
    if form.validate_on_submit():
        pass

    form.title.data = post_to_update.title
    return render_template('dashboard/update_post.html', form=form)
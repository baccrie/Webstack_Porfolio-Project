from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Post, Comment, Admin, Activity
from ShopWE.blog.forms import Blogpost, UpdateBlogPost
from ShopWE.generic import save_image, categories, brands
from flask import current_app
import os

blog = Blueprint('blog', __name__)


@blog.route('/posts')
@login_required
def posts():
    """
    Showing all Blog Post
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page=page, per_page=4)
    return render_template('blog/posts.html', posts=posts, categories=categories(), brands=brands())



@blog.route('/dash/addpost', methods=['GET', 'POST'])
@login_required
def addpost():
    """
    Adds new post to the db
    """
    form = Blogpost()
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data)
        if form.image.data:
            image_name = save_image(form.image.data, 'blogposts')
            new_post.image_1 = image_name
            
        new_activity = Activity(content='You Published a new blog post', category='success', admin_id=current_user.id)
        db.session.add(new_activity)
        db.session.add(new_post)

        db.session.commit()
        flash(f'Posts successfully added', 'success')
        return redirect(url_for('blog.addpost'))
    
    return render_template('blog/add_post.html', form=form)


@blog.route('/dash/<int:id>/updatepost', methods=['POST', 'GET'])
@login_required
def updatepost(id):
    """
    Updating an existing post
    """
    form = UpdateBlogPost()
    post_to_update = Post.query.get_or_404(id)

    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    if form.validate_on_submit():
        post_to_update.title = form.title.data
        post_to_update.content = form.content.data

        if form.image.data:
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/blogposts/' + post_to_update.image))
                post_to_update.image = save_image(form.image.data, 'blogposts')
            except:
                post_to_update.image = save_image(form.image.data, 'blogposts')

        new_activity = Activity(content='You updated a blog post', category='info', admin_id=current_user.id)
        db.session.add(new_activity)
        db.session.commit()
        flash(f'Post has been updated', 'success')
        return redirect(url_for('blog.updatepost', id=post_to_update.id))

    form.title.data = post_to_update.title
    form.content.data = post_to_update.content
    return render_template('blog/update_post.html', form=form)

@blog.route('/blog/posts')
def allposts():
    """
    Admin panel show all blog post
    """
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    posts = Post.query.all()
    return render_template('blog/all_posts.html', posts=posts)

@blog.route('/blog/<int:id>/post')
def single_post(id):
    """
    Single post page
    """
    post = Post.query.get_or_404(id)
    return render_template('blog/single_post.html', post=post)

@blog.route('/blog/<int:id>/deletepost')
@login_required
def delete_post(id):
    """
    Deletes existing post
    """
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    post_to_delete = Post.query.get_or_404(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    flash(f'Post has been deleted successfully', 'info')
    return redirect(url_for('blog.allposts'))
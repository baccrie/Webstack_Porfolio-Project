import os
import secrets
from flask import current_app
from ShopWE.models import Brand, Category, Post

def save_image(photo, type):
    random_hex  = secrets.token_hex(8)
    _, file_ext = os.path.splitext(photo.filename)
    file_name = random_hex + file_ext
    file_path = os.path.join(current_app.root_path, f'static/images/{type}', file_name)
    photo.save(file_path)
    return file_name

def brands():
    brands = Brand.query.all()
    return brands

def categories():
    categories = Category.query.all()
    return categories

def posts():
    posts = Post.query.all()
    return posts
from flask import request, render_template, url_for, redirect, Blueprint, session, flash
from ShopWE import app
from ShopWE.models import Category, Brand, Product
from ShopWE.models import Admin, Customer, Comment, Vendor, Post
from ShopWE.generic import brands, categories, posts

cart = Blueprint('cart', __name__)

@cart.route('/<int:id>/addcart', methods=['POST'])
def add_to_cart(id):
    product_to_add = Product.query.get_or_404(id)
    if 'cart' not in session:
        session['cart'] = {
            id : {
                'name': product_to_add.name,
                'price': product_to_add.price,
                'discount': product_to_add.discount,
                'quantity': 1,
                'image': product_to_add.image_1,
                'author': product_to_add.owner.name
            }
        }

    else:
        print('carts in session')
        """if product_to_add.owner.name == session['cart'][id]['author']:
            flash(f'You cant add products from different vendors to cart', 'danger')
            return redirect(url_for('dash.home'))"""
        
        if not str(id) in list(session['cart'].keys()):
            print('its present')
            new = {
                str(id): {
                'name': product_to_add.name,
                'price': product_to_add.price,
                'discount': product_to_add.discount,
                'quantity': 1,
                'image': product_to_add.image_1,
                'author': product_to_add.owner.name
            }
            }
            session['cart'].update(new)
            session.modified = True
            print(session['cart'])
        for key, product in session['cart'].items():
            if (id == int(key)):
                product['quantity'] += 1
    
    return redirect(request.referrer)

@cart.route('/clear')
def clear():
    session.pop('cart')

    # print(session['cart'])
    return "deleted"
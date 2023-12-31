from flask import request, render_template, url_for, redirect, Blueprint, session, flash
from ShopWE import app
from ShopWE.models import Category, Brand, Product
from ShopWE.models import Admin, Customer, Comment, Vendor, Post
from ShopWE.generic import brands, categories, posts
from flask_login import login_required

cart = Blueprint('cart', __name__)

def add_cart(obj):
    session['cart'].update(obj)
    session.modified = True


@cart.route('/<int:id>/addcart', methods=['POST'])
def add_to_cart(id):
    """
    Add new item to cart
    """
    product_to_add = Product.query.get_or_404(id)
    if 'cart' not in session:
        session['cart'] = {}
        obj = {
            str(id) : {
                'name': product_to_add.name,
                'price': product_to_add.price,
                'discount': product_to_add.discount,
                'quantity': 1,
                'image_1': product_to_add.image_1,
                'image_2': product_to_add.image_2,
                'author': product_to_add.owner.name,
                'category': product_to_add.category.name,
                'brand': product_to_add.brand.name,
                'vendor': product_to_add.owner.name
            }
        }

        add_cart(obj)

    else:

        if not str(id) in list(session['cart'].keys()):
            print('its present')
            new = {
                str(id): {
                'name': product_to_add.name,
                'price': product_to_add.price,
                'discount': product_to_add.discount,
                'quantity': 1,
                'image_1': product_to_add.image_1,
                'image_2': product_to_add.image_2,
                'author': product_to_add.owner.name,
                'category': product_to_add.category.name,
                'brand': product_to_add.brand.name,
                'vendor': product_to_add.owner.name
                }
            }
            add_cart(new)
        
        elif str(id) in list(session['cart'].keys()):
            flash('product has been added already', 'danger')
            print(session['cart'])
            return redirect(request.referrer)
            

    return redirect(request.referrer)


@cart.route('/carts')
@login_required
def cart_items():
    """
    Display all cart items with details
    """
    if 'cart' not in session:
        flash(f'Cart is empty , pls add products to cart', 'info')
        return redirect(url_for('home'))
    subtotal = 0
    total = 0

    print(session['cart'])
    for key, value in session['cart'].items():
        print(value)
        subtotal += float(value['price'])
        total += float(value['price']) - (float(value['discount']) / 100 * float(value['price']))
    subtotal = f'{subtotal:.0f}'
    total = f'{total:.0f}'
    return render_template('cart/cart.html', total=total, subtotal=subtotal)

@cart.route('/cart/<int:id>/remove')
@login_required
def delete_item(id):
    """
    Delete a particular item from the cart
    """
    if 'cart' not in session:
        flash(f'Cart is empty , pls add products to cart', 'info')
        return redirect(url_for('home'))
    else:
        session['cart'].pop(str(id))
        flash(f'Product successfully removed', 'danger')
        # return redirect(url_for('home'))
        return redirect(url_for('cart.cart_items'))

@cart.route('/clear')
def clear():
    """
    Removes all items from carts
    """
    if 'cart' in session:
        session.pop('cart')
    # print(session['cart'])
    flash(f'All cart items successfully removed', 'info')
    return redirect(url_for('home'))
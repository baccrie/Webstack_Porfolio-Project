from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.customers.forms import CustomerRegister
from ShopWE.vendors.forms import VendorRegister
from ShopWE.auth.forms import Login
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Activity, Post, Admin
from ShopWE.dashboard.forms import Addproduct, Addbrand, Addcategory, Updateproduct
from ShopWE.generic import save_image
from flask import current_app
import os

dash = Blueprint('dash', __name__)

@dash.route('/dash/home')
@login_required
def home():
    form1 = Addbrand()
    posts = Post.query.limit(5).all()
    products = Product.query.order_by(Product.date.desc()).limit(5).all()
    activities = current_user.activities[:5]
    return render_template('dashboard/home.html', form1=form1, posts=posts, products=products, activities=activities)


@dash.route('/dash/addproduct', methods=['POST', 'GET'])
@login_required
def addproduct():
    form = Addproduct()
    brands = Brand.query.all()
    categories = Category.query.all()
    if not isinstance(current_user, Vendor):
        flash(f'This page is only accessible to vendors', 'danger')
        return redirect(url_for('dash.home'))
    if form.validate_on_submit():
        brand_id = request.form.get('brand')
        category_id = request.form.get('category')
        newProduct = Product(name=form.name.data, price=form.price.data, discount=form.discount.data,
                             stock=form.stock.data, description=form.description.data, brand_id=brand_id, category_id=category_id,  vendor_id=current_user.id,
                             )
        if form.image_1.data:
            image_name = save_image(form.image_1.data, 'products')
            newProduct.image_1 = image_name
        
        if form.image_2.data:
            image_name = save_image(form.image_2.data, 'products')
            newProduct.image_2 = image_name

        if form.image_3.data:
            image_name = save_image(form.image_3.data, 'products')
            newProduct.image_3 = image_name

        db.session.add(newProduct)
        new_activity = Activity(content='You added new product to the database', vendor_id=current_user.id)
        db.session.add(new_activity)
        db.session.commit()
        flash(f'Product successfully added', 'success')
        print('No')
        return redirect(url_for('dash.addproduct'))
    return render_template('dashboard/add_product.html', form=form, brands=brands, categories=categories)

@dash.route('/dash/<int:id>/updateproduct', methods=['POST', 'GET'])
@login_required
def updateproduct(id):
    product_to_edit = Product.query.get_or_404(id)
    form = Updateproduct()
    brands = Brand.query.all()
    categories = Category.query.all()

    if not isinstance(current_user, Vendor):
        flash(f'This page is only accessible to vendors', 'danger')
        return redirect(url_for('dash.home'))
    
    elif current_user.id != product_to_edit.vendor_id:
        flash(f'You cant access a product that dosent belong to you', 'danger')
        return redirect(url_for('dash.home'))
    
    if form.validate_on_submit():
        product_to_edit.name = form.name.data
        product_to_edit.price = form.price.data
        product_to_edit.stock = form.stock.data
        product_to_edit.discount = form.discount.data
        product_to_edit.description = form.description.data

        if form.image_1.data:
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/products'+ product_to_edit.image_1))
                product_to_edit.image_1 = save_image(form.image_1.data, 'products')
                print(product_to_edit.image_1)
            except:
                product_to_edit.image_1 = save_image(form.image_1.data, 'products')

        
        if form.image_2.data:
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/products'+ product_to_edit.image_2))
                product_to_edit.image_2 = save_image(form.image_2.data, 'products')
            except:
                product_to_edit.image_2 = save_image(form.image_2.data, 'products')

        if form.image_3.data:
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/products'+ product_to_edit.image_3))
                product_to_edit.image_3 = save_image(form.image_3.data, 'products')
            except:
                product_to_edit.image_3 = save_image(form.image_3.data, 'products')

        new_activity = Activity(content=f'You updated the product {product_to_edit.name}', vendor_id=current_user.id)
        db.session.add(new_activity)
        db.session.commit()

        flash('product successfully updated', 'success')
        return redirect(url_for('dash.home'))
    
    form.name.data = product_to_edit.name
    form.price.data = product_to_edit.price
    form.discount.data = product_to_edit.discount
    form.stock.data = product_to_edit.stock
    form.description.data = product_to_edit.description

    return render_template('dashboard/update_product.html', form=form, brands=brands, categories=categories)

@dash.route('/dash/<int:id>/deleteproduct', methods=['POST', 'GET'])
@login_required
def deleteproduct(id):
    product_to_delete = Product.query.get_or_404(id)

    if not isinstance(current_user, Vendor):
        flash(f'This page is only accessible to vendors', 'danger')
        return redirect(url_for('home'))
    
    elif current_user.id != product_to_delete.vendor_id:
        flash(f'You cant delete a product that dosent belong to you', 'danger')
        return redirect(url_for('home'))
    
    try:
        os.unlink(os.path.join(current_app.root_path, 'static/images/products'+ product_to_delete.image_1))
        os.unlink(os.path.join(current_app.root_path, 'static/images/products'+ product_to_delete.image_2))
        os.unlink(os.path.join(current_app.root_path, 'static/images/products'+ product_to_delete.image_3))
        db.session.delete(product_to_delete)
    except:
        db.session.delete(product_to_delete)

    new_activity = Activity(content=f'You deleted the product {product_to_delete.name}', vendor_id=current_user.id)
    db.session.add(new_activity)
    db.session.commit()

    return redirect(url_for('dash.home'))


@dash.route('/dash/<int:id>/profile', methods=['POST', 'GET'])
@login_required
def profile(id):
    if type(current_user) == 'Admin':
        user_profile = Admin.query.get_or_404(id)

    elif type(current_user) == 'Customer':
        user_profile = Customer.query.get_or_404(id)

    else:
        user_profile = Vendor.query.get_or_404(id)

    if request.method == 'POST':
        current_password = request.form.get('password')
        print(current_password)
        return request.referrer

    return render_template('dashboard/profile.html')

@dash.route('/dash/myproducts', methods=['POST', 'GET'])
@login_required
def vendor_products():
    products = current_user.products
    return render_template('dashboard/products.html', products=products)

@dash.route('/dash/addbrand', methods=['POST', 'GET'])
@login_required
def addbrand():
    if request.method == 'POST':
    #newBrand = Brand(name=form1.name.data)
        newBrand = request.method.get('name')
        db.session.add(newBrand)
        #db.session.commit()
        flash(f'Brand has been successfully added', 'success')
        return redirect(url_for('dash.addproduct'))

    return render_template('dashboard/home.html')
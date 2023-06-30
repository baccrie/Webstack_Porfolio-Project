from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.customers.forms import CustomerRegister, UpdateCustomerInfo, UpdateCustomerPassword
from ShopWE.vendors.forms import VendorRegister, UpdateVendorInfo, UpdateVendorPassword
from ShopWE.auth.forms import Login
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Activity, Post, Admin
from ShopWE.dashboard.forms import Addproduct, Addbrand, Addcategory, Updateproduct
from ShopWE.generic import save_image
from flask import current_app
import os

product = Blueprint('product', __name__)

@product.route('/product/<int:id>', methods=['POST', 'GET'])
def singleproduct(id):
    product = Product.query.get_or_404(id)
    return render_template('product/single_product.html', product=product, brands=brands(), categories=categories())


@product.route('/dash/addproduct', methods=['POST', 'GET'])
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
        return redirect(url_for('product.addproduct'))
    return render_template('product/add_product.html', form=form, brands=brands, categories=categories)

@product.route('/dash/<int:id>/updateproduct', methods=['POST', 'GET'])
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
                os.unlink(os.path.join(current_app.root_path, 'static/images/products/'+ product_to_edit.image_1))
                product_to_edit.image_1 = save_image(form.image_1.data, 'products')
            except:
                product_to_edit.image_1 = save_image(form.image_1.data, 'products')

        
        if form.image_2.data:
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/products/'+ product_to_edit.image_2))
                product_to_edit.image_2 = save_image(form.image_2.data, 'products')
            except:
                product_to_edit.image_2 = save_image(form.image_2.data, 'products')

        if form.image_3.data:
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/products/'+ product_to_edit.image_3))
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

    return render_template('product/update_product.html', form=form, brands=brands, categories=categories)

@product.route('/dash/<int:id>/deleteproduct', methods=['POST', 'GET'])
@login_required
def deleteproduct(id):
    product_to_delete = Product.query.get_or_404(id)

    if not isinstance(current_user, Vendor):
        flash(f'This page is only accessible to vendors', 'danger')
        return redirect(url_for('dash.home'))
    
    elif current_user.id != product_to_delete.vendor_id:
        flash(f'You cant delete a product that dosent belong to you', 'danger')
        return redirect(url_for('dash.home'))
    
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


@product.route('/dash/myproducts', methods=['POST', 'GET'])
@login_required
def vendor_products():
    if not isinstance(current_user, Vendor):
        flash('You re not authorized to access this page', 'danger')
        return redirect(url_for('dash.home'))
    
    if not current_user.products:
        flash('You dont have any product yet, visit the addproduct page to add new product', 'info')
        return redirect(url_for('dash.home'))
    
    products = current_user.products
    return render_template('product/products.html', products=products)

@product.route('/dash/products')
def allproducts():
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    products = Product.query.all()
    return render_template('product/all_products.html', products=products)
from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.customers.forms import CustomerRegister, UpdateCustomerInfo, UpdateCustomerPassword
from ShopWE.vendors.forms import VendorRegister, UpdateVendorInfo, UpdateVendorPassword
from ShopWE.auth.forms import Login
from ShopWE.models import Customer, Vendor, Product,  Brand, Category, Activity, Post, Admin
from ShopWE.dashboard.forms import Addproduct, Addbrand, Addcategory, Updateproduct
from ShopWE.generic import save_image, brands, categories
from flask import current_app
import os


product = Blueprint('product', __name__)

@product.route('/product/<int:id>', methods=['POST', 'GET'])
def singleproduct(id):
    product = Product.query.get_or_404(id)
    brand = Brand.query.filter_by(id=product.brand_id).first()
    related_product = brand.products
    return render_template('product/single_product.html', product=product, brands=brands(), categories=categories(), related_products=related_product, id=id)


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
        new_activity = Activity(content='You added new product to the database', category='success', vendor_id=current_user.id)
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

        new_activity = Activity(content=f'You updated the product {product_to_edit.name}', category='info', vendor_id=current_user.id)
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

    new_activity = Activity(content=f'You deleted the product {product_to_delete.name}', category='danger', vendor_id=current_user.id)
    db.session.add(new_activity)
    db.session.commit()

    flash(f'Product successfully deleted', 'info')
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

@product.route('/dash/addbrand', methods=['POST', 'GET'])
@login_required
def add_brand():
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    if request.method == 'POST':
        brand = request.form.get('brand')
        brands = Brand.query.filter_by(name=brand).first()
        if brands:
            flash('Brand already exixts pls choose a different brand', 'danger')
            return redirect(url_for('product.add_brand'))
        new_brand = Brand(name=request.form.get('brand'))
        db.session.add(new_brand)
        db.session.commit()
        flash('Brand has been added successfully', 'success')

    return render_template('product/addbrand.html')

@product.route('/dash/addcategory', methods=['POST', 'GET'])
@login_required
def add_category():
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    if request.method == 'POST':
        category = request.form.get('category')
        categories = Category.query.filter_by(name=category).first()
        if categories:
            flash('Category already exixts pls choose a different category', 'danger')
            return redirect(url_for('product.add_category'))
        new_category = Category(name=request.form.get('category'))
        db.session.add(new_category)
        db.session.commit()
        flash('Category has been added successfully', 'success')

    return render_template('product/addcategory.html')

@product.route('/dash/<int:id>/editbrand', methods=['POST', 'GET'])
@login_required
def edit_brand(id):
    brand_to_update = Brand.query.filter_by(id=id).first()
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    if request.method == 'POST':
        brand = request.form.get('brand')
        brands = Brand.query.filter_by(name=brand).first()

        if brands:
            flash('Brand already exixts pls choose a different brand', 'danger')
            return redirect(url_for('product.edit_brand', id=id))
        
        brand_to_update.name = brand
        db.session.commit()
        flash('Brand has been updated successfully', 'success')
    return render_template('product/edit_brand.html', brand_to_update=brand_to_update)


@product.route('/dash/<int:id>/editcategory', methods=['POST', 'GET'])
@login_required
def edit_category(id):
    category_to_update = Category.query.filter_by(id=id).first()
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    if request.method == 'POST':
        category = request.form.get('category')
        categories = Category.query.filter_by(name=category).first()

        if categories:
            flash('Categories already exixts pls choose a different category', 'danger')
            return redirect(url_for('product.edit_category', id=id))
        
        category_to_update.name = request.form.get('category')
        db.session.commit()
        flash('category has been updated successfully', 'success')
    return render_template('product/edit_category.html', category_to_update=category_to_update)


@product.route('/dash/brands')
@login_required
def brands():
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    brands = Brand.query.all()
    return render_template('product/brands.html', brands=brands)

@product.route('/dash/categories')
@login_required
def categories():
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    categories = Category.query.all()
    return render_template('product/categories.html', categories=categories)

@product.route('/dash/<int:id>/deletebrand')
@login_required
def delete_brand(id):
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    brand_to_delete = Brand.query.get_or_404(id)
    db.session.delete(brand_to_delete)
    db.session.commit()
    flash(f'Brand has been deleted successfully', 'info')
    return redirect(url_for('product.brands'))

@product.route('/dash/<int:id>/deletecategory')
@login_required
def delete_category(id):
    if not isinstance(current_user, Admin):
        flash('Oops! you were redirected from an admin only page', 'danger')
        return redirect(url_for('dash.home'))
    
    category_to_delete = Category.query.get_or_404(id)
    db.session.delete(category_to_delete)
    db.session.commit()
    flash(f'Category has been deleted successfully', 'info')
    return redirect(url_for('product.categories'))
from ShopWE import app, db, bcrypt, flash
from flask import Blueprint, render_template, url_for, session, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from ShopWE.customers.forms import CustomerRegister
from ShopWE.vendors.forms import VendorRegister
from ShopWE.auth.forms import Login
from ShopWE.models import Customer, Vendor, Product,  Brand, Category
from ShopWE.dashboard.forms import Addproduct, Addbrand, Addcategory, Updateproduct

dash = Blueprint('dash', __name__)

@dash.route('/dash/home')
@login_required
def home():
    form1 = Addbrand()
    return render_template('dashboard/home.html', form1=form1)


@dash.route('/dash/addproduct', methods=['POST', 'GET'])
@login_required
def addproduct():
    form = Addproduct()
    brands = Brand.query.all()
    categories = Category.query.all()
    if not isinstance(current_user, Vendor):
        flash(f'This page is only accessible to vendors', 'danger')
        return redirect(url_for('home'))
    if form.validate_on_submit():
        brand_id = request.form.get('brand')
        category_id = request.form.get('category')
        newProduct = Product(name=form.name.data, price=form.price.data, discount=form.discount.data,
                             stock=form.stock.data, description=form.description.data, brand_id=brand_id, category_id=category_id, vendor_id=current_user.id)
        db.session.add(newProduct)
        db.session.commit()
        flash(f'Product successfully added', 'success')
        return redirect(url_for('dash.addproduct'))
    return render_template('dashboard/add_product.html', form=form, brands=brands, categories=categories)

@dash.route('/dash/<int:id>/updateproduct', methods=['POST', 'GET'])
@login_required
def updateproduct(id):
    product_to_edit = Product.query.get_or_404(id)
    form = Updateproduct()

    if not isinstance(current_user, Vendor):
        flash(f'This page is only accessible to vendors', 'danger')
        return redirect(url_for('home'))
    
    elif current_user.id != product_to_edit.vendor_id:
        flash(f'You cant access a product that dosent belong to you', 'danger')
        return redirect(url_for('home'))
    
    if form.validate_on_submit():
        product_to_edit.name = form.name.data
        product_to_edit.price = form.price.data
        product_to_edit.stock = form.stock.data
        product_to_edit.discount = form.discount.data
        product_to_edit.description = form.description.data

        print('start')
        db.session.commit()
        print('stop')

        flash('product successfully updated', 'success')
        return redirect(url_for('dash.home'))
    
    form.name.data = product_to_edit.name
    form.price.data = product_to_edit.price
    form.discount.data = product_to_edit.discount
    form.stock.data = product_to_edit.stock
    form.description.data = product_to_edit.description

    return render_template('dashboard/update_product.html', form=form)

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
    
    db.session.delete(product_to_delete)
    db.session.commit()

    return redirect(url_for('dash.home'))


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
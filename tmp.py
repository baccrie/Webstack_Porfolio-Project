ry', methods=['POST', 'GET'])
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
        
        category_to_update.name = brand
        db.session.commit()
        flash('category has been updated successfully', 'success')
    return render_template('product/edit_category.html', category_to_update=category_to_update)

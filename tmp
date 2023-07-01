 if isinstance(current_user, Admin):
        user_profile = Admin.query.get_or_404(id)
        form = UpdateCustomerInfo()

    elif isinstance(current_user, Customer):
        print('Yes')
        form = UpdateCustomerInfo()
        form1 = UpdateCustomerPassword()
        user_profile = Customer.query.get_or_404(id)

        form.email.data = current_user.email
        form.username.data = current_user.username
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.country.data = current_user.country
        form.state.data = current_user.state
        form.address.data = current_user.address
        form.city.data = current_user.city
        form.number.data = current_user.phone
        form.about.data = current_user.about

    
    elif isinstance(current_user, Vendor):
        user_profile = Vendor.query.get_or_404(id)
        form = UpdateVendorInfo()
        form1 = UpdateVendorPassword()

        form.email.data = current_user.email
        form.name.data = current_user.name
        form.country.data = current_user.country
        form.state.data = current_user.state
        form.address.data = current_user.address
        form.city.data = current_user.city
        form.number.data = current_user.phone
        form.about.data = current_user.about

        
    
    print(form.errors)
    if request.method == 'POST':
        print('start')
        user_profile.email = form.email.data
        user_profile.username = form.username.data
        user_profile.first_name = form.first_name.data
        user_profile.last_name = form.last_name.data
        user_profile.country = form.country.data
        user_profile.state = form.state.data
        user_profile.city = form.city.data
        user_profile.address = form.address.data
        user_profile.number = form.number.data
        user_profile.about = form.about.data
        print('stop')

        db.session.commit()
        flash('success', 'success')
        return redirect(url_for('dash.home'))
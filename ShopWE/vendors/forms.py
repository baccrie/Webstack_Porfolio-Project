from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from ShopWE.models import Vendor, Customer, Admin
from ShopWE import bcrypt

"""
This Module handles flaskwtf for rendering and validating forms input for Vendors registraton
"""

class VendorRegister(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired()])
    number = TelField('Number', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    about = TextAreaField('About', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Sign Up')
   
        
    def validate_email(self, email):
        user_1 = Customer.query.filter_by(email=email.data).first()
        user_2 = Vendor.query.filter_by(email=email.data).first()
        user_3 = Admin.query.filter_by(email=email.data).first()

        if user_1 or user_2:
            raise ValidationError(f'User with email already exist! ')
        
    def validate_number(self, number):
        user_1 = Customer.query.filter_by(phone=number.data).first()
        user_2 = Vendor.query.filter_by(phone=number.data).first()
        user_3 = Admin.query.filter_by(phone=number.data).first()

        if user_1 or user_2 or user_3:
            raise ValidationError(f'Phone already exist! ')
        
class UpdateVendorInfo(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired()])
    number = TelField('Number', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    address = TextAreaField('Address')
    about = TextAreaField('About', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Save Changes')
   
        
    def validate_email(self, email):
        user_1 = Customer.query.filter_by(email=email.data).first()
        user_2 = Vendor.query.filter_by(email=email.data).first()
        user_3 = Admin.query.filter_by(email=email.data).first()

        if user_1 or user_2:
            raise ValidationError(f'User with email already exist! ')
        
    def validate_number(self, number):
        user_1 = Customer.query.filter_by(phone=number.data).first()
        user_2 = Vendor.query.filter_by(phone=number.data).first()
        user_3 = Admin.query.filter_by(phone=number.data).first()

        if user_1 or user_2 or user_3:
            raise ValidationError(f'Phone already exist! ')
        
class UpdateVendorPassword(FlaskForm):
    current_password = PasswordField('Current Password')
    new_password = PasswordField('Password', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Change Password')

    def validate_current_password(self, current_password):
        if not bcrypt.check_password_hash(current_user.password, current_password.data):
            raise ValidationError('Your Password is incorrect')
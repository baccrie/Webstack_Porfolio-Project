from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from ShopWE.models import Vendor, Customer


class VendorRegister(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    number = TelField('Number', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
   
    def validate_email(self, email):
        user_1 = Vendor.query.filter_by(email=email.data).first()
        user_2 = Customer.query.filter_by(email=email.data).first()
        if user_1 or user_2:
            raise ValidationError(f'Vendor with {user.email} already exist! ')
        
    def validate_number(self, number):
        user_1 = Vendor.query.filter_by(phone=number.data).first()
        user_2 = Customer.query.filter_by(phone_number=number.data).first()

        if user_1 or user_2:
            raise ValidationError(f'Phone already exist! ')
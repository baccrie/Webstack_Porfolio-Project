from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from ShopWE.models import Customer, Vendor


class CustomerRegister(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    number = TelField('Number', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_username(self, username):
        user = Customer.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'User with {user.username} already exist! ')
        
    def validate_email(self, email):
        user = Customer.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'User with {user.email} already exist! ')

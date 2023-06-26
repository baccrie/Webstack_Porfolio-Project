from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField, TextAreaField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class Addproduct(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    discount = IntegerField('Discount', validators=[DataRequired()])
    stock = IntegerField('Stock', default=0)
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Product')

    image_1 = FileField('image1', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    image_2 = FileField('image1', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    image_3 = FileField('image1', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])



class Updateproduct(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    discount = IntegerField('Discount', validators=[DataRequired()])
    stock = IntegerField('Stock', default=0)
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Update Product')

    image_1 = FileField('image1', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    image_2 = FileField('image1', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    image_3 = FileField('image1', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

class Addbrand(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField('image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Add')


class Addcategory(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField('image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Add')
    


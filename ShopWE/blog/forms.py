from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class Blogpost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Post Image', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'gif'])])
    submit = SubmitField('Post')

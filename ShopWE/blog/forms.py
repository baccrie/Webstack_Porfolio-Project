from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_ckeditor import CKEditorField
from wtforms.widgets import TextArea


class Blogpost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = CKEditorField('content', validators=[DataRequired()], widget=TextArea())
    image = FileField('Post Image', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'gif'])])
    submit = SubmitField('Post')

class UpdateBlogPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = CKEditorField('content', validators=[DataRequired()], widget=TextArea())
    image = FileField('Post Image', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'gif'])])
    submit = SubmitField('Update')
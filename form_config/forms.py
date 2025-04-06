from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    email = EmailField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=32)])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=20, message='Must be between 1-20 characters')])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=20, message='Must be between 1-20 characters')])
    email = EmailField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=32)])
    submit = SubmitField('Submit')

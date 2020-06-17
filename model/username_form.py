from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField

class UsernameForm(FlaskForm):
    username = StringField('Username')

#test
from flask_wtf import Form 
from wtforms import StringField, validators

class LoginForm(Form):
	username = StringField('Username', [validators.required()])
	password = StringField('Password', [validators.required()])
	
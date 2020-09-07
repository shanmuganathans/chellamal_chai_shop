import re
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from flask import flash
from flask_package.models import User

class RegisterationForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired(),Length(min =2, max=20)])
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confim password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('SignUp')

    def validate_username(self,username):
    	print('validate_username')
    	user = User.query.filter_by(username =  username.data).first()
    	if user:
    		print(user)
    		flash('UserName already exists')
    		raise ValidationError()

    def validate_email(self, email):
    	user = User.query.filter_by(email = email.data).first()
    	if user:
    		flash('Email already exists')
    		raise ValidationError()

    def validate_password(self, password):
    	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    	match_re = re.compile(reg)
    	res = re.search(match_re, password.data)
    	if not res:
    		flash(" The password must contain at least one uppercase,lowercase and digit")
    		raise ValidationError()





class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField("Password",validators = [DataRequired()])
    rember = BooleanField('Remeber me')
    login = SubmitField('Login')



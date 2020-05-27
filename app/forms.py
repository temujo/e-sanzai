from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    mobile_number = StringField('Дугаар', validators=[DataRequired(message='Энэ талбар шаардлагатай.')])
    password = PasswordField('Нууц үг', validators=[DataRequired(message='Энэ талбар шаардлагатай.')])
    remember_me = BooleanField('Сануулах')
    submit = SubmitField('Нэвтрэх')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from application.models import Account


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

    def validate_email(self, email):
        if Account.query.filter_by(email=email.data).first() is None:
            raise ValidationError('No user with this email found.')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm',
                                                                             message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if Account.query.filter_by(email=email.data).first():
            raise ValidationError('Your email has been already registered.')

    def validate_login(self, login):
        if Account.query.filter_by(login=login.data).first():
            raise ValidationError('Sorry, account with this username already exists.')


class UserInfoForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    voivodeship = SelectField(u'Voivodeship', choices=[('ds', 'dolnośląskie'),
                                                       ('kp', 'kujawsko-pomorskie'),
                                                       ('lb', 'lubelskie'),
                                                       ('ls', 'lubuskie'),
                                                       ('ld', 'łódzkie'),
                                                       ('mp', 'małopolskie'),
                                                       ('mz', 'mazowieckie'),
                                                       ('op', 'opolskie'),
                                                       ('pk', 'podkarpackie'),
                                                       ('pl', 'podlaskie'),
                                                       ('pm', 'pomorskie'),
                                                       ('sl', 'śląskie'),
                                                       ('sk', 'świętokrzyskie'),
                                                       ('wm', 'warmińsko-mazurskie'),
                                                       ('wp', 'wielkopolskie'),
                                                       ('zp', 'zachodnio-pomorskie')])
    is_infected = BooleanField('Are you infected person?')
    submit = SubmitField('Save your personal information')

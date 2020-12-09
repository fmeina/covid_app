#from sqlalchemy.orm import relationship

from application import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(user_id)


class Account(db.Model, UserMixin):
    __tablename__ = "accounts"
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(64))
    user_info = db.relationship('UserInfo', backref='account', lazy='dynamic')  # register relationship

    def __repr__(self):
        return "login" + " " + self.login

    def __init__(self, email, login, password):
        self.email = email
        self.login = login
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.account_id


class UserInfo(db.Model):
    __tablename__ = "userinfo"
    userinfo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'))
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    voivodeship = db.Column(db.String(25))
    is_infected = db.Column(db.BOOLEAN, unique=False)

    def __repr__(self):
        return "name" + " " + self.first_name + " " + self.last_name

    def __init__(self, first_name, last_name, voivodeship, is_infected):  # nie wiem czy nie trzeba dodac account_id
        self.first_name = first_name
        self.last_name = last_name
        self.voivodeship = voivodeship
        self.is_infected = is_infected

    def get_id(self):
        return self.account_id

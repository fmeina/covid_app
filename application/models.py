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

from application import db


class Accounts(db.Model):
    __tablename__ = "accounts"
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(64))


    def __repr__(self):
        return "login" + " " + self.login

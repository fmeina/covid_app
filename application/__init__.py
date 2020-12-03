from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from application.core.views import core
app.register_blueprint(core)

from application.users.views import users
app.register_blueprint(users)
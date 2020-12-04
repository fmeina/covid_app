from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.static_folder = 'static'

db = SQLAlchemy(app)



from application.core.views import core
app.register_blueprint(core)

from application.users.views import users
app.register_blueprint(users)

login_manager.init_app(app)
login_manager.login_view = 'users.login'

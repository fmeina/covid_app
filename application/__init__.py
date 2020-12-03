from flask import Flask

app = Flask(__name__)

from application.core.views import core
app.register_blueprint(core)

from application.users.views import users
app.register_blueprint(users)
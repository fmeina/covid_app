from flask import render_template, request, Blueprint

users = Blueprint('users', __name__)


@users.route('/register')
def index():
    return render_template('register.html')

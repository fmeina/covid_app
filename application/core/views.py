from flask import render_template, request, Blueprint
from flask_login import login_required, current_user

core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@login_required
@core.route('/stats')
def stats():
    return render_template('stats.html')

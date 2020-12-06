from flask import render_template, request, Blueprint
from flask_login import login_required, current_user
from application.core.article_scraper import text1

core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', current_user=current_user, text1=text1)


@core.route('/stats')
@login_required
def stats():
    return render_template('stats.html', current_user=current_user)


@core.route('/report')
@login_required
def report():
    return render_template('report.html', current_user=current_user)

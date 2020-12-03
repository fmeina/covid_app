from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

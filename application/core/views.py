from flask import render_template, Blueprint
from flask_login import login_required, current_user
from application.utils.article_scraper import text1
from werkzeug.utils import secure_filename
from flask import flash, request, redirect, url_for
from application.utils.file_uploader import allowed_file
from application import app
import os


core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', current_user=current_user, text1=text1)


@core.route('/stats')
@login_required
def stats():
    return render_template('stats.html', current_user=current_user)


@core.route('/report', methods=['GET', 'POST'])
@login_required
def report():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        elif not allowed_file(file.filename):
            flash('Incorrect file extension, you should use .pdf, .doc or .docx')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File updated successfully')
    return render_template('report.html', current_user=current_user)

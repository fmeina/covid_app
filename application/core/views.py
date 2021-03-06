from flask import render_template, Blueprint, request, make_response, jsonify
from flask_login import login_required, current_user
from application.utils.article_scraper import text1
from werkzeug.utils import secure_filename
from flask import flash, request, redirect, url_for
from application.utils.file_uploader import allowed_file
from application import app, db
from application.utils.infections_sql import *
import pdfkit
import os

core = Blueprint('core', __name__)
config = pdfkit.configuration(wkhtmltopdf="D:\\pytek\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")


@core.route('/', methods=['GET', 'POST'])
def index():
    count = int(request.cookies.get('visit-count', 0))
    count += 1
    count_number = 'You have visited this page ' + str(count) + ' times'

    resp = make_response(render_template('index.html', current_user=current_user, count_number=count_number))
    resp.set_cookie('visit-count', str(count))
    return resp


@core.route('/stats')
@login_required
def stats():
    return render_template('stats.html', current_user=current_user, number_result=number_result,
                           number_result1=number_result1,
                           number_result2=number_result2,
                           number_result3=number_result3,
                           number_result4=number_result4,
                           number_result5=number_result5,
                           number_result6=number_result6,
                           number_result7=number_result7,
                           number_result8=number_result8,
                           number_result9=number_result9,
                           number_result10=number_result10,
                           number_result11=number_result11,
                           number_result12=number_result12,
                           number_result13=number_result13,
                           number_result14=number_result14,
                           number_result15=number_result15,
                           number_result16=number_result16)


@core.route('/stats_file')
@login_required
def stats_file():
    return render_template('stats_file.html', current_user=current_user, number_result=number_result,
                           number_result1=number_result1,
                           number_result2=number_result2,
                           number_result3=number_result3,
                           number_result4=number_result4,
                           number_result5=number_result5,
                           number_result6=number_result6,
                           number_result7=number_result7,
                           number_result8=number_result8,
                           number_result9=number_result9,
                           number_result10=number_result10,
                           number_result11=number_result11,
                           number_result12=number_result12,
                           number_result13=number_result13,
                           number_result14=number_result14,
                           number_result15=number_result15,
                           number_result16=number_result16)


@core.route('/stats_file_pdf')
def stats_pdf():
    rendered = render_template('stats_file.html', current_user=current_user, number_result=number_result,
                               number_result1=number_result1,
                               number_result2=number_result2,
                               number_result3=number_result3,
                               number_result4=number_result4,
                               number_result5=number_result5,
                               number_result6=number_result6,
                               number_result7=number_result7,
                               number_result8=number_result8,
                               number_result9=number_result9,
                               number_result10=number_result10,
                               number_result11=number_result11,
                               number_result12=number_result12,
                               number_result13=number_result13,
                               number_result14=number_result14,
                               number_result15=number_result15,
                               number_result16=number_result16)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=stats.pdf'

    return response


@core.route('/stats_json')
def stats_json():
    return jsonify(all=number_result,
                   ds=number_result1,
                   kp=number_result2,
                   lb=number_result3,
                   ls=number_result4,
                   ld=number_result5,
                   mp=number_result6,
                   mz=number_result7,
                   op=number_result8,
                   pk=number_result9,
                   pl=number_result10,
                   pm=number_result11,
                   sl=number_result12,
                   sk=number_result13,
                   wm=number_result14,
                   wp=number_result15,
                   zp=number_result16)


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
            extension = filename.split()[-1]
            new_filename = "upload-{}_{}".format(current_user.account_id, extension)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            flash('File updated successfully')
    return render_template('report.html', current_user=current_user)


@core.route('/actual_restrictions')
def actual_restrictions():
    return render_template('actual_restrictions.html', current_user=current_user, text1=text1)


@core.route('/ajax', methods=['POST'])
def ajax_request():
    username = request.form['username']
    return jsonify(username=username)

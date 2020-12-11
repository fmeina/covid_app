from flask import render_template, request, redirect, request, url_for, flash, abort, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from application.users.forms import LoginForm, RegistrationForm, UserInfoForm
from application.models import Account, UserInfo
from application import db

users = Blueprint('users', __name__)


@users.route('/personal-info', methods=['GET', 'POST'])
@login_required
def personal_info():
    form = UserInfoForm()
    if form.validate_on_submit():
        user_info = UserInfo(account_id=current_user.account_id,
                             first_name=form.first_name.data,
                             last_name=form.last_name.data,
                             voivodeship=form.voivodeship.data,
                             is_infected=form.is_infected.data)
        data_account_id = user_info.account_id
        data_first_name = user_info.first_name
        data_last_name = user_info.last_name
        data_voivodeship = user_info.voivodeship
        data_is_infected = user_info.is_infected
        if UserInfo.query.filter(UserInfo.account_id == current_user.account_id).first() is not None:
            db.engine.execute("DELETE FROM userinfo WHERE account_id = %s", data_account_id)
            db.engine.execute(
                "INSERT INTO userinfo(account_id, first_name, last_name, voivodeship, is_infected) VALUES(%s, %s, %s, %s, %s)",
                data_account_id, data_first_name, data_last_name, data_voivodeship, data_is_infected)
            db.session.commit()
            flash('Your personal information is updated now')
        else:
            db.engine.execute(
                "INSERT INTO userinfo(account_id, first_name, last_name, voivodeship, is_infected) VALUES(%s, %s, %s, %s, %s)",
                data_account_id, data_first_name, data_last_name, data_voivodeship, data_is_infected)
            db.session.commit()
            flash('Your personal information is saved now')
    return render_template('user_info.html', form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Account(email=form.email.data,
                       login=form.login.data,
                       password=form.password.data)
        data_login = user.login
        data_email = user.email
        data_password = user.password
        db.engine.execute("INSERT INTO accounts(login, email, password) VALUES(%s, %s, %s)", data_login, data_email,
                          data_password)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Account.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.')
            next = request.args.get('next')
            if next is None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
        else:
            flash("Wrong password.")
    return render_template('login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out.")
    return redirect(url_for('core.index'))

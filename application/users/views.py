from flask import render_template, request, redirect, request, url_for, flash, abort, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from application.users.forms import LoginForm, RegistrationForm
from application.models import Account
from application import db

users = Blueprint('users', __name__)

""" TODO: 
    - naprawic flash() bo nie wyswietla napisu
    - wyrzucic welcome_user() i zamiast tego przekierowac do core
"""



@login_required
@users.route('/logout')
def logout():
    logout_user()
    flash("You logged out.")
    return redirect(url_for('core.index'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Account.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')
            next = request.args.get('next')
            if next is None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Account(email=form.email.data,
                       login=form.login.data,
                       password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

from flask import render_template, url_for, redirect, request, flash, Blueprint
from app.forms import SignUpForm, LoginForm
from app import app, db, bcrypt
from app.models import User, Post
from flask_login import login_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def helpcenter():
    if request.method == 'POST':
        return redirect(url_for('helpcenter'))
    return render_template('TradeQHelpcenter.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account successfully created for {form.username.data}", "success")
        return redirect(url_for('login'))
    return render_template('sign_up.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash("Login failed. Please enter the correct details", "danger")
    return render_template("login.html", form=form)

from flask_login import login_user, logout_user, login_required

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

import os
import secrets
from PIL import Image
from flask import render_template, url_for, redirect, request, flash, Blueprint
from app.forms import SignUpForm, LoginForm, UpdateAccountForm
from app import app, db, bcrypt
from app.models import User, Post
from flask_login import login_user, current_user, logout_user

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/help')
def helpcenter():
    if request.method == 'POST':
        return redirect(url_for('helpcenter'))
    return render_template('TradeQHelpcenter.html', title='Support')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Successfully logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash("Login failed. Please enter the correct details", "danger")
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('index'))
    
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail = output_size
    i.save(picture_path)

    return picture_fn

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Successfully updated account!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data =  current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='My Profile', image_file=image_file, form=form)
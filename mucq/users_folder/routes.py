from flask import render_template, url_for, redirect, request, flash, Blueprint
from mucq.users_folder.forms import (SignUpForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm)
from flask_login import login_required, login_user, current_user, logout_user
from mucq.users_folder.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route('/signup', methods=['GET', 'POST'])
def signup():
    from mucq.__init__ import db, bcrypt
    import mucq.models
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = mucq.models.User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f"Account successfully created for {form.username.data}", "success")
        return redirect(url_for('users.login'))
    return render_template('sign_up.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    import mucq.models
    from mucq.__init__ import bcrypt
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = mucq.models.User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Successfully logged in!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash("Login failed. Please enter the correct details", 'danger')
    return render_template("login.html", form=form)


@users.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('main.index'))

@login_required
@users.route('/profile', methods=['GET', 'POST'])
def profile():
    from mucq.__init__ import db
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Successfully updated account!', 'success')
        return redirect(url_for('users.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='My Profile', image_file=image_file, form=form)

@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    import mucq.models
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = mucq.models.User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions on how to reset your password to your email', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    import mucq.models
    from mucq.__init__ import db, bcrypt
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = mucq.models.User.verify_reset_token(token)
    if user is None:
        flash('error: invalid or expired token', 'danger')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(
            f"Account password has been successfully updated!", "success")
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

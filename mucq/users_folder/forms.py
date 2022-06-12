from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField

class SignUpForm(FlaskForm):
    username = StringField('Username:', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up!')

    def validate_username(self, username):
        import mucq.models
        user = mucq.models.User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is used, please choose another username')

    def validate_email(self, email):
        import mucq.models
        user = mucq.models.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'There is already an account using this email')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username:', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    #about me (working)
    about_me = StringField('About Me', validators=[Length(min=2, max=2000)])
    #about me (working)
    picture = FileField('Update Profile Picture: ', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        import mucq.models
        if username.data != current_user.username:
            user = mucq.models.User.query.filter_by(
                username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is used, please choose another username')

    def validate_email(self, email):
        import mucq.models
        if email.data != current_user.email:
            user = mucq.models.User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'There is already an account using this email')


class RequestResetForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        import mucq.models
        user = mucq.models.User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'The email that you typed is not a MucQ account. Sign Up to create an account')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password:', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

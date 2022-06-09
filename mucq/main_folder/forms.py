from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    email = EmailField('Email', validators=[validators.DataRequired(), validators.Length(1, 100), validators.Email()])
    feedback = TextAreaField('Feedback', validators=[validators.DataRequired()])
    submit = SubmitField('Submit feedback')


class TagsForm(FlaskForm):
    title = StringField('Title', validators=[validators.DataRequired()])
    text = TextAreaField('Description', validators=[validators.DataRequired()])
    submit = SubmitField('Post')


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')

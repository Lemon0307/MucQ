from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class ProductsForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_like = BooleanField('Like')
    description = StringField('Description', validators=[DataRequired()])
    product_price = StringField('Price', validators=[DataRequired()])
    picture = FileField('Product Image: ', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg']), DataRequired()])
    submit = SubmitField('Create Product')
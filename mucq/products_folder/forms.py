from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class ProductsForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    #product_image = FileField('Product Photo', validators=[])
    description = StringField('Description', validators=[DataRequired()])
    product_price = StringField('Price', validators=[DataRequired()])
    picture = FileField('Product Image: ', validators=[
                        FileAllowed(['jpg', 'png']), DataRequired()])
    submit = SubmitField('Create Product')
import re
from flask import render_template, url_for, redirect, request, flash, abort, Blueprint
from flask_login.utils import login_required
from flask_login import current_user

from mucq.models import Products

products = Blueprint('products', __name__)


@products.route('/products')
def product():
    products = Products.query.all()
    return render_template('products/products.html', products=products)


@products.route('/products/<int:product_id>', methods=['GET', 'POST'])
def product_view(product_id):
    import mucq.models
    product = mucq.models.Products.query.get_or_404(product_id)
    return render_template('/products/product_view.html', product=product)


@products.route('/create_product', methods=['GET', 'POST'])
def create_product():
    from mucq.models import Products
    import mucq.products_folder.forms
    from mucq.__init__ import db
    form = mucq.products_folder.forms.ProductsForm()
    if form.validate_on_submit():
        product = Products(product_name=form.product_name.data, description=form.description.data, author=current_user)
        db.session.add(product)
        db.session.commit()
        flash('Your product has been created!', 'success')
        return redirect(url_for('products.product'))
        
    return render_template('/products/create_products.html', form=form)
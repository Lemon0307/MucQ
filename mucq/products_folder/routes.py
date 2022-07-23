from fileinput import filename
from click import format_filename
from flask import render_template, url_for, redirect, request, flash, abort, Blueprint
from flask_login.utils import login_required
from flask_login import current_user
from mucq.main_folder.forms import SearchForm
from flask_wtf.csrf import CSRFProtect
from mucq.products_folder.utils import save_picture
from json import *

from mucq.models import Products

csrf = CSRFProtect()
products = Blueprint('products', __name__)


@products.route('/products')
def product():
    from mucq.products_folder.forms import ProductsForm
    from mucq.models import Products
    products = Products.query.order_by(Products.date_posted.desc())
    form = ProductsForm()
    return render_template('products/products.html', products=products, form=form)


@products.route('/products/<int:product_id>', methods=['GET', 'POST'])
def product_view(product_id):
    import mucq.models
    product = mucq.models.Products.query.get_or_404(product_id)
    return render_template('/products/product_view.html', product=product)


@login_required
@products.route('/create_product', methods=['GET', 'POST'])
def create_product():
    from mucq.models import Products
    import mucq.products_folder.forms
    from mucq.__init__ import db
    form = mucq.products_folder.forms.ProductsForm()
    if form.picture.data:
        picture_file = save_picture(form.picture.data)
    if form.validate_on_submit():
        product = Products(product_name=form.product_name.data, description=form.description.data, product_price=form.product_price.data,
                           image_file=picture_file, author=current_user)
        db.session.add(product)
        db.session.commit()
        flash('Your product has been created!', 'success')
        return redirect(url_for('products.product'))
    return render_template('/products/create_products.html', form=form)


@products.route('/search_product', methods=['POST'])
@csrf.exempt
def search_product():
    from mucq.models import Products
    form = SearchForm()
    posts = Products.query
    if form.validate_on_submit():
        SearchForm.searched = form.searched.data
        posts = posts.filter(Products.product_name.like(
            '%' + SearchForm.searched + '%'))
        posts = posts.order_by(Products.product_name).all()
        return render_template('/products/search_product.html', form=form, searched=SearchForm.searched, posts=posts)
    return render_template('/products/search_product.html', form=form, searched=SearchForm.searched, posts=posts)


@products.route('/post/<int:product_id>/delete', methods=['POST'])
@login_required
def delete_product(product_id):
    import mucq.models
    from mucq.__init__ import db
    product = mucq.models.Products.query.get_or_404(product_id)
    if product.author != current_user:
        abort(403)
    db.session.delete(product)
    db.session.commit()
    flash('Product successfully deleted!', 'success')
    return redirect(url_for('products.product'))
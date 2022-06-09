import re
from flask import render_template, url_for, redirect, request, flash, abort, Blueprint
from flask_login.utils import login_required
from flask_login import current_user

products = Blueprint('products', __name__)

@products.route('/products', methods=['GET', 'POST'])

def product():
    return render_template('products/products.html')
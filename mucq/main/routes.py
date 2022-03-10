from flask import render_template, url_for, redirect, request
from mucq.__init__ import app
from mucq.models import Post
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/help')
def helpcenter():
    if request.method == 'POST':
        return redirect(url_for('helpcenter'))
    return render_template('TradeQHelpcenter.html', title='Support')

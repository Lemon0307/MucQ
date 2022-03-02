from flask import render_template, url_for, redirect, request
from app.__init__ import app
from app.models import Post
from flask import Blueprint

main = Blueprint('main', __name__)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/help')
def helpcenter():
    if request.method == 'POST':
        return redirect(url_for('helpcenter'))
    return render_template('TradeQHelpcenter.html', title='Support')

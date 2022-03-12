from flask import render_template, url_for, redirect, request, Blueprint, flash
from flask_login import current_user, login_required

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    from mucq.models import Post
    import mucq.posts_folder.forms
    posts = Post.query.order_by(Post.date_posted.desc())
    from mucq.__init__ import db
    import mucq.models
    form = mucq.posts_folder.forms.PostForm()
    if form.validate_on_submit():
        
        post = mucq.models.Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')

    return render_template('index.html', posts=posts, form=form)
    

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/help')
def helpcenter():
    if request.method == 'POST':
        return redirect(url_for('helpcenter'))
    return render_template('TradeQHelpcenter.html', title='Support')

@main.route('/terms-of-service')
def tos():
    return render_template('tos.html', title='Terms of Service')
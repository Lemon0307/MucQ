from flask import render_template, url_for, redirect, request, flash, abort, Blueprint
from flask_login.utils import login_required
import mucq.posts_folder.forms
from mucq.__init__ import db
import mucq.models
from flask_login import current_user

posts = Blueprint('posts', __name__)

@posts.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = mucq.posts_folder.forms.PostForm()
    if form.validate_on_submit():
        post = mucq.models.Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title='Create Post', form=form, legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = mucq.models.Post.query.get_or_404(post_id)
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template('post.html', post=post, image_file=image_file)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = mucq.models.Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = mucq.posts_folder.forms.PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = mucq.models.Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post successfully deleted!', 'success')
    return redirect(url_for('main.index'))


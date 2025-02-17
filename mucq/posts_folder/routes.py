import re
from flask import render_template, url_for, redirect, request, flash, abort, Blueprint
from flask_login.utils import login_required
from flask_login import current_user

posts = Blueprint('posts', __name__)

@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    import mucq.models
    from mucq.__init__ import db
    import mucq.posts_folder.forms
    post = mucq.models.Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = mucq.posts_folder.forms.PostForm()
    if form.validate_on_submit():
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.index', post_id=post.id))
    elif request.method == 'GET':
        form.content.data = post.content
    return render_template('/posts/create_post.html', title='Update Post', form=form, legend='Update Post')

@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    import mucq.models
    from mucq.__init__ import db
    post = mucq.models.Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post successfully deleted!', 'success')
    return redirect(url_for('main.index'))
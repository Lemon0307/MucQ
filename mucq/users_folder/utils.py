import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail = output_size
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    from mucq.__init__ import mail
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='mucq.contact@gmail.com', recipients=[user.email])
    msg.body = f'''Hello! If you want to reset your password, please click on the following link:
    {url_for('users.reset_token', token=token, _external=True)}
    
    This is an automated message. If you did not make this request and the email is sent to you by accident, please delete this email immedietely and no changes will apply to the person requesting this email.
    '''
    mail.send(msg)

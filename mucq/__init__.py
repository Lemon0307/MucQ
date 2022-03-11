import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from mucq.config import Config

mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    import mucq.main_folder.routes as main
    import mucq.posts_folder.routes as posts
    import mucq.users_folder.routes as users

    app.register_blueprint(users.users)
    app.register_blueprint(posts.posts)
    app.register_blueprint(main.main)

    return app
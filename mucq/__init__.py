import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from mucq.config import Config
from flask_wtf.csrf import CsrfProtect
from flask_migrate import Migrate
mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
file_path = os.path.abspath(os.path.dirname(__file__))


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    migrate = Migrate(app, db)
    CsrfProtect(app)
    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    import mucq.main_folder.routes as main
    import mucq.posts_folder.routes as posts
    import mucq.users_folder.routes as users
    import mucq.errors.handlers as errors
    import mucq.products_folder.routes as products
    import mucq.dev_folder.routes as dev

    app.register_blueprint(users.users)
    app.register_blueprint(posts.posts)
    app.register_blueprint(main.main)
    app.register_blueprint(errors.errors)
    app.register_blueprint(products.products)
    app.register_blueprint(dev.dev)

    return app

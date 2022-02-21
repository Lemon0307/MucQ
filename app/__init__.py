import os
from app import routes
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '188db0c1a734f4d4d31f26f6c0ef5562d7aa4910caeb09b2bd402a25edba2d51b4000e2245f818c9e1216cb62e3e98761ebbaac40510ce4608213ef327e32e12322f02e423'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'mucq.contact@gmail.com'
app.config['MAIL_PASSWORD'] = 'sussyimposter'
mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

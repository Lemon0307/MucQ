from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mucq.__init__ import login_manager, db, create_app
from flask import current_app
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    about_me = db.Column(db.Text, nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    products = db.relationship('Products', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=300):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.about_me}', '{self.image_file}')"

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):

        return f"Post('{self.date_posted}')"


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"{self.name} , {self.email} , {self.feedback}, {self.date}"


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"{self.title} , {self.text} , {self.date}"


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    product_name = db.Column(db.String(40), nullable=False)
    product_price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text, nullable=False)
    #likes = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"POST('{self.product_name}', '{self.description}', '{self.product_price}')"

def init_db():
    db.drop_all()
    db.create_all()
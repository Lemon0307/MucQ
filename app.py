from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from forms import SignUpForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '188db0c1a734f4d4d31f26f6c0ef5562d7aa4910caeb09b2bd402a25edba2d51b4000e2245f818c9e1216cb62e3e98761ebbaac40510ce4608213ef327e32e12322f02e423'
db = SQLAlchemy(app)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactus')
def contactus():
    if request.method == 'POST':
        return redirect(url_for('contactus'))
    return render_template('contactus.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f"Account successfully created for {form.username.data}", "success")
        return redirect(url_for('index'))
    return render_template('sign_up.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"Successfully logged in", "success")
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please try again', 'danger')
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
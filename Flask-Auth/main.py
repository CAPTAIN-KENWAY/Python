from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'AH3_ZQIbDa9cqFolkk62-g'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager.init_app(app=app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if db.session.query(User).filter_by(email = request.form['email']).first():
            flash('Email already exist in the database. Please Login instead.')
            return redirect(url_for('login'))
            
        password = request.form['password']

        hash_password = generate_password_hash(
            password=password, method='pbkdf2:sha256', salt_length=8)

        new_user = User(
            email=request.form['email'],
            password=hash_password,
            name=request.form['name']
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = db.session.query(User).filter_by(email = request.form['email']).first()
        if user==None:
            flash("Email doesn't exist in the Database")
        elif check_password_hash(user.password,request.form['password']):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash("Incorrect Password")
    return render_template("login.html")


@app.route('/secrets', methods=['POST', 'GET'])
@login_required
def secrets():
    # name = db.session.query(User.name).filter(User.email == email).one()
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    if logout_user():
        return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory='./static/files/', path='cheat_sheet.pdf', as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)

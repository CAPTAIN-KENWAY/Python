from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_URL = "https://api.themoviedb.org/3/movie/"
API_KEY = "bd68532447e6f3d03e92a058c1e6403e"
IMAGE_URL = 'https://image.tmdb.org/t/p/original'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app=app)


class Movie(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, db.CheckConstraint('ranking<=10 and ranking>0'), nullable=False)
    ranking = db.Column(db.Integer, db.CheckConstraint(
        'ranking<=10 and ranking>0'), nullable=False, unique=True)
    review = db.Column(db.String(500))
    img_url = db.Column(db.String(1000), nullable=False)


class Add_Form(FlaskForm):
    movie_title = StringField('Movie Title', validators=[InputRequired()])
    submit = SubmitField('Add Movie')


class Edit_Form(FlaskForm):
    new_rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[InputRequired()])
    new_review = StringField('Your Review')
    submit = SubmitField('Done')


def select():
    pass

# new_movie=Movie(
#     title="Drive",
#     year=2011,
#     description="Driver is a skilled Hollywood stuntman who moonlights as a getaway driver for criminals. Though he projects an icy exterior, lately he's been warming up to a pretty neighbor named Irene and her young son, Benicio. When Irene's husband gets out of jail, he enlists Driver's help in a million-dollar heist. The job goes horribly wrong, and Driver must risk his life to protect Irene and Benicio from the vengeful masterminds behind the robbery.",
#     rating=7.8,
#     ranking=10,
#     review="My favourite character was the driver.",
#     img_url="https://www.themoviedb.org/t/p/w300_and_h450_bestv2/602vevIURmpDfzbnv5Ubi6wIkQm.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    return render_template("index.html", movies=Movie.query.all())


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = Add_Form()
    if form.validate_on_submit() and request.method == 'POST':
        search = request.form['movie_title']
        parameters = {
            'language': 'en-US',
            'api_key': API_KEY,
            'query': search,
            'page': 1
        }
        movies = requests.get(url=SEARCH_URL, params=parameters).json()
        return render_template('select.html', movies=movies['results'])

    return render_template('add.html', form=form)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    movie_id = request.args.get('id', type=int)
    movie = Movie.query.get(movie_id)
    form = Edit_Form()
    if form.validate_on_submit() and request.method == 'POST':
        movie_id = request.form['id']
        movie = Movie.query.get(movie_id)
        movie.rating = request.form['new_rating']
        if len(request.form['new_review']) > 0:
            movie.review = request.form['new_review']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id', type=int)
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Importing libraries, classes and functions

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import requests

# API key and urls. Using website themoviedb.org

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_URL = "https://api.themoviedb.org/3/movie/"
API_KEY = "bd68532447e6f3d03e92a058c1e6403e"
IMAGE_URL = 'https://image.tmdb.org/t/p/original'

# Creating flask app and adding bootstrap to it. Configuring app to use the movies-collection database
# and creating secret key for wtforms.

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app=app)

# Creating the Movie model, which will eventually create movie table in the database along with the given
# columns with their datatypes and constraints.


class Movie(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, db.CheckConstraint('ranking<=10 and ranking>0'))
    ranking = db.Column(db.Integer, db.CheckConstraint(
        'ranking<=10 and ranking>0'))
    review = db.Column(db.String(500))
    img_url = db.Column(db.String(1000), nullable=False)


# Creating the forms for adding and editing the movies.

class Add_Form(FlaskForm):
    movie_title = StringField('Movie Title', validators=[InputRequired()])
    submit = SubmitField('Add Movie')


class Edit_Form(FlaskForm):
    new_rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[InputRequired()])
    new_review = StringField('Your Review')
    submit = SubmitField('Done')


# Routing root or '/' to our index.html and passing movies by quering the database using SQLAlchemy

@app.route("/")
def home():

    # Sorting the movies according to their rating and updating the ranking column.
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i, movie in enumerate(movies, 1):
        movie.ranking = i
    db.session.commit()

    return render_template("index.html", movies=Movie.query.order_by(Movie.ranking.desc()).all())

# Routing '/add' to add.html and passing our add_form.


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = Add_Form()  
    if form.validate_on_submit() and request.method == 'POST':

        # searching the movie name using the tmdb api.
        search = request.form['movie_title']
        parameters = {
            'language': 'en-US',
            'api_key': API_KEY,
            'query': search,
            'page': 1
        }
        movies = requests.get(url=SEARCH_URL, params=parameters).json()

        # After search going to select.html to select the movie from list of movies
        return render_template('select.html', movies=movies['results'])

    return render_template('add.html', form=form)


# Routing the '/find' to find.html and adding the selected movie to database.


@app.route("/find", methods=['GET', 'POST'])
def find():
    id = request.args.get('id', type=str)  # getting the id of movie from tmdb
    parameters = {
        'language': 'en-US',
        'api_key': API_KEY,
    }

    # get details of movie selected using the tmdb api with movie id.
    movie = requests.get(url=f'{MOVIE_URL}{id}', params=parameters).json()

    # Checking if movie already present in the database.
    try:
        mv = db.session.query(Movie.id).filter(Movie.title == movie['title']).one()
        flash('Movie already present.', 'error')
        return redirect(url_for('home'))

    # adding the new movie to database.
    except NoResultFound:
        new_movie = Movie(
            title=movie['title'],
            year=movie['release_date'].split('-')[0],
            description=movie['overview'],
            img_url=f"{IMAGE_URL}{movie['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        mv = db.session.query(Movie.id).filter(Movie.title == movie['title']).one()
        flash('Movie Added Successfully!', 'info')

        # Redirecting to edit for adding rating and review.
        # Passing the movie id of the movie added to edit.
        return redirect(url_for('edit', id=mv.id))


# Routing the '/edit' to edit.html for editing the rating and review of a movie.


@app.route("/edit", methods=['GET', 'POST'])
def edit():

    # Getting the movie id from post request
    movie_id = request.args.get('id', type=int)
    movie = Movie.query.get(movie_id)
    form = Edit_Form()
    if form.validate_on_submit() and request.method == 'POST':
        movie_id = request.form['id']
        movie = Movie.query.get(movie_id)
        movie.rating = request.form['new_rating']

        if len(request.form['new_review']) > 0: # Checking if new review is given.
            movie.review = request.form['new_review']
        db.session.commit()
        flash('Movie Edited Successfully!', 'info')
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


# Routing the '/delete' to delete.html for deleting the existing movies.


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id', type=int)
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


# Running the app in main


if __name__ == '__main__':
    with app.app_context():
        db.create_all() # creating all database objects
    app.run(debug=True)

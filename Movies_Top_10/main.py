from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import InputRequired
import requests

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


class Edit_Form(FlaskForm):
    new_rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[InputRequired()])
    new_review = StringField('Your Review')
    submit = SubmitField('Done')


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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

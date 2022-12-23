from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        self = self.__dict__
        del self['_sa_instance_state']
        return self


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record

@app.route('/random', methods=['GET'])
def get_random():
    ids = Cafe.query.count()
    random_id = randint(1, ids)
    cafe = Cafe.query.get(random_id)
    return jsonify(cafe.to_dict())

@app.route('/all')
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route('/search')
def search():
    loc = request.args['loc']
    cafes_count = Cafe.query.filter_by(location=loc).count()
    if cafes_count == 0:
        return jsonify(error={
            'Not Found': 'Sorry we don\'t have cafe at that location.'
        })
    cafes = Cafe.query.filter_by(location=loc)    
    return jsonify(cafe = [cafe.to_dict() for cafe in cafes])

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

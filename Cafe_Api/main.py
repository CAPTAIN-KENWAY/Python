from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import randint

API_KEY = 'TopSecretAPIKey'

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
    return jsonify(cafe.to_dict()), 200

@app.route('/all')
def all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200

@app.route('/search')
def search():
    loc = request.args['loc']
    cafes_count = Cafe.query.filter_by(location=loc).count()
    if cafes_count == 0:
        return jsonify(error={
            'Not Found': 'Sorry we don\'t have cafe at that location.'
        }), 404

    cafes = Cafe.query.filter_by(location=loc)    
    return jsonify(cafe = [cafe.to_dict() for cafe in cafes]), 200

# HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add():
    if API_KEY != request.args['api_key']:
        return jsonify(
            error='Sorry, that\'s not allowed. Make sure you have correct api_key.'
        ), 403
    new_cafe = Cafe(
    name = request.form.get('name'),
    map_url = request.form.get('map_url'),
    img_url = request.form.get('img_url'),
    location = request.form.get('location'),
    seats = request.form.get('seats'),
    has_toilet = bool(request.form.get('has_toilet')),
    has_wifi = bool(request.form.get('has_wifi')),
    has_sockets = bool(request.form.get('has_sockets')),
    can_take_calls = bool(request.form.get('can_take_calls')),
    coffee_price = request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        response={
            'success':'Successfully added the new cafe.'
        }
    ), 200


# HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:id>', methods=['PATCH'])
def update(id):
    cafe = Cafe.query.get(id)
    if cafe is None:
        return jsonify(
            error={
            'Not Found': 'Sorry a cafe with that id was not found in the database.'
            }
        ), 404

    cafe.coffee_price = request.args['price']
    db.session.commit()
    return jsonify(
        response={
            'success':'Successfully updated the price.'
        }
    ), 200


# HTTP DELETE - Delete Record

@app.route('/report-closed/<int:id>', methods=['DELETE'])
def delete(id):
    cafe = Cafe.query.get(id)
    if API_KEY != request.args['api_key']:
        return jsonify(
            error='Sorry, that\'s not allowed. Make sure you have correct api_key.'
        ), 403
    if cafe is None:
        return jsonify(
            error={
            'Not Found': 'Sorry a cafe with that id was not found in the database.'
            }
        ), 404    

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(
        response={
            'success':'Successfully deleted the cafe.'
        }
    ), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

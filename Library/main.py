from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class books(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    return render_template('index.html', books=books.query.all())


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    id = request.args.get('id', type=int)
    if request.method == 'POST':
        new_rating = request.form['new_rating']
        id = request.form['id']
        book = books.query.get(id)
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', id=id, books=books.query.all())

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    id = request.args.get('id', type=int)
    book = books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

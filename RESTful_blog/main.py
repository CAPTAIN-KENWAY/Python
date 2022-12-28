from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt


# Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/f4a3a509a8a42cefa926").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
bootstrap = Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['CKEDITOR_PKG_TYPE'] = 'full-all'
app.config['CKEDITOR_HEIGHT'] = '500'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CONFIGURE TABLE


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    author = StringField("Your Name", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")

# WEBSUTE


@app.route('/')
def home():
    return render_template("index.html", all_posts=BlogPost.query.all())


@app.route("/post/<int:index>")
def show_post(index):
    post = BlogPost.query.get(index)
    return render_template("post.html", post=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/new-post', methods=['GET', 'POST'])
def add():
    new_post_form = CreatePostForm()
    if new_post_form.validate_on_submit() and request.method == 'POST':
        now = dt.datetime.now()
        # date = now.strftime('%B %d, %Y')
        new_post = BlogPost(
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            date=now.strftime('%B %d, %Y'),
            author=request.form.get('author'),
            img_url=request.form.get('img_url'),
            body=request.form.get('body')
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('make-post.html', form=new_post_form)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = db.session.query(BlogPost).get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        author=post.author,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = request.form['title']
        post.subtitle = request.form['subtitle']
        post.author = request.form['author']
        post.img_url = request.form['img_url']
        post.body = request.form['body']
        db.session.commit()
        return redirect(url_for('show_post', index=post.id))

    return render_template('make-post.html', form=edit_form, id=post_id)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id = request.args.get('id', type=int)
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

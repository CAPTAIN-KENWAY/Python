from flask import Flask, render_template
from post import Post

app = Flask(__name__)
p = Post()


@app.route('/')
def home():
    all_posts = p.get_all_posts()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def view_post(id):
    post = p.get_post(id=id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)



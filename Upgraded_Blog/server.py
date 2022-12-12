from flask import Flask, render_template, request
import requests
import smtplib


NPOINT_URL = "https://api.npoint.io/f4a3a509a8a42cefa926"
EMAIL = "pythontesting810@gmail.com"
PASSWORD = "jflzmvkrbbuhavxz"


def get_all_posts():
    response = requests.get(url=NPOINT_URL)
    data = response.json()
    return data


def get_post(id):
    response = requests.get(url=NPOINT_URL)
    data = response.json()
    return data[id-1]

def send_mail(name, email, phone, message):
    msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="guptakaran094@gmail.com",
            msg=msg.encode('utf-8')
        )


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=get_all_posts())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", msg_sent=False)
    else:
        data = request.form
        send_mail(data['name'], data['email'], data["phone"], data["message"])        
        return render_template("contact.html", msg_sent=True)


@app.route('/post/<int:id>')
def view_post(id):
    return render_template("post.html", post=get_post(id))


if __name__ == "__main__":
    app.run(debug=True)

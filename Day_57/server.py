from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    return render_template('index.html', year=year)
    

@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    parameters = {
        'name': name
    }
    response =  requests.get(url="https://api.agify.io/", params=parameters)
    data = response.json()
    age = int(data['age'])
    response =  requests.get(url="https://api.genderize.io/", params=parameters)
    data = response.json()
    gender = data['gender']
    return render_template('guess.html', name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)

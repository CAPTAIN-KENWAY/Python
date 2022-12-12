import random
from flask import Flask

app = Flask(__name__)
@app.route('/')
def root():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src=https://media.giphy.com/media/IsfrRWvbUdRny/giphy.gif>'

number = random.randint(0,10)

@app.route('/<guess_number>')
def guess(guess_number):
    if int(guess_number)>number:
        return "<h1 style='color:purple'>Too high, try again!</h1>"\
            "<img src=https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy-downsized-large.gif>"
    elif int(guess_number)<number:
        return "<h1 style='color:red'>Too low, try again!</h1>"\
            "<img src=https://media.giphy.com/media/3oEduPoyJdFYgHx7YQ/giphy.gif>"
    else:
        return "<h1 style='color:green'>You found me!</h1>"\
            "<img src=https://media.giphy.com/media/QyK8gRzGW2fV6qo8Hm/giphy.gif>"



if __name__ == "__main__":
    app.run(debug=True)
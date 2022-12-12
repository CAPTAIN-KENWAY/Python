from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import InputRequired, URL
import csv

COFFEE_RATING = ('☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕')
WIFI_RATING = ('✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪')
POWER_RATING = ('✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')

app = Flask(__name__)
app.secret_key = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[InputRequired()])
    location = StringField('Cafe location on Google Maps (URL)',
                           validators=[InputRequired(), URL()])
    opentime = TimeField(
        'Opening time e.g. 8AM', validators=[InputRequired()],
        render_kw={'style': 'width: 48.5rem; height: 2rem'})
    closetime = TimeField(
        'Closing time e.g. 5:30PM', validators=[InputRequired()],
        render_kw={'style': 'width: 48.5rem; height: 2rem'})
    coffee_rating = SelectField('Coffee Rating', choices=COFFEE_RATING, validators=[
        InputRequired()],
        render_kw={'style': 'width: 48.5rem; height: 2rem'})
    wifi_rating = SelectField('Wifi Strength Rating', choices=WIFI_RATING, validators=[
                              InputRequired()], render_kw={'style': 'width: 48.5rem; height: 2rem'})
    power_rating = SelectField('Power Socket Availablity', choices=POWER_RATING, validators=[
                               InputRequired()], render_kw={'style': 'width: 48.5rem; height: 2rem'})
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a+', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            row = [form.cafe.data, form.location.data, form.opentime.data, form.closetime.data,
                   form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
            writer.writerow(row)
            return redirect(url_for("cafes"))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run()

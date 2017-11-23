from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

form =  """
        <br>
        <form action="/testform">
          <input type="text" name="day">
          <input type="text" name="month">
          <input type="text" name="year">
          <br><br>
          <input type="submit">
        </form>
        <hr>
        """

@app.route("/")
def hello():
    return form

@app.route("/testform", methods=['GET', 'POST'])
def testroute():
    day = validate_day(request.args.get('day'))
    month = validate_month(request.args.get('month'))
    year = validate_year(request.args.get('year'))

    if day and month and year:
        return "Thanks for submitting everything" + form
    else:
        return form


def validate_day(day):
    if day.isdigit() and int(day) > 0 and int(day) < 31:
        return int(day)

def validate_month(month):
    months = [
        "January",
        "February"
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if month.capitalize() in months:
        return month.capitalize()

def validate_year(year):
    if year.isdigit() and int(year) > 1900 and int(year) < 2020:
        return int(year)

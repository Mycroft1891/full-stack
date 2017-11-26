from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import url_for
import cgi

app = Flask(__name__)


#########################
# Create Routes         #
#########################

@app.route("/")
def hello():
    return generate_form()


@app.route("/testform", methods=['GET', 'POST'])
def testroute():
    day = validate_day(request.args.get('day'))
    month = validate_month(request.args.get('month'))
    year = validate_year(request.args.get('year'))

    if day and month and year:
        return redirect(url_for('thanks'))
    else:
        return generate_form("Please give valid dates", day, month, year)


@app.route("/thanks")
def thanks():
    return  """
            <h1 style="padding:5px; color:white; background-color:green;">
                Thank you for submitting the form
            </h1>
            """


#########################
# Create Form           #
#########################

form =  """
        <form action="/testform">
            What is your birthday ?<br><br>
            <label>Day<input type="text" name="day" value="{day}" placeholder="16"></label>
            <label>Month <input type="text" name="month" value="{month}" placeholder="Aug" ></label>
            <label>Year <input type="text" name="year" value="{year}" placeholder="1991"></label>
            <br><br>
            <input type="submit">
        </form><hr>
        <h3 style="color:white; background-color:red;">{message}</h3>
        """


#########################
# Helper functions      #
#########################

def generate_form(message="", d="", m="", y=""):
    return form.format(message=message, day=d, month=m, year=y)


def escape_html(tag):
    for (i,o) in (("&", "&amp;"), (">", "&gt;"), ("<", "&lt;"), ('"', "&quot;")):
        tag = tag.replace(i, o)
    # return cgi.escape(tag, quote = True)


def validate_day(day):
    if day.isdigit() and int(day) > 0 and int(day) < 31:
        return int(day)


def validate_month(month):
    months = (
        ("Jan", "January"),
        ("Feb", "February"),
        ("Mar", "March"),
        ("Apr", "April"),
        ("May", "May"),
        ("Jun", "June"),
        ("Jul", "July"),
        ("Aug", "August"),
        ("Sep", "September"),
        ("Oct", "October"),
        ("Nov", "November"),
        ("Dec", "December")
    )

    month = month.capitalize()

    for (abbr, full) in months:
        if month == abbr or month == full:
            return month


def validate_year(year):
    if year.isdigit() and int(year) > 1900 and int(year) < 2020:
        return int(year)


#########################
# App Init              #
#########################

if __name__ == "__main__":
    app.run(debug=True)

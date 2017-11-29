# Forms and Inputs

[__<= GO BACK__](../README.md)

1. [Getting Started](#start)
2. [Install Flask and Setup](#setup)
3. [Python Programming](#python)
4. [Flask App: Simple Backend](main.py)


## <a name="start">Getting Started</a>

- [Working File](index.html)

Create a form
```
<form>
  <input name="q">
</form>
```

> Due personal reasons, I decided to use Flask instead of WebApp2 and Google App Engine.


## <a name="setup">Install Flask and setup</a>

```bash
brew install python3
pip3 install Flask
```

Now that we installed flask we create a basic app like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
```

To run our flask app we execute this command (main.py is our app):

```bash
FLASK_APP=main.py flask run
```

To create a route in Flaks we can use the `@app.route` decorator and specify a route as well as well as the methods we want to support:

```python
@app.route("/testform", methods=['GET', 'POST'])
def testroute():
    if valid_form:
        return form_is_valid
    else:
        return form_is_invalid
```

To redirect from one route to another we can use the `redirect` and `url_for`. We have to import both before we can use them:

```
from flask import redirect
from flask import url_for

@app.route(/hello)
def hello():
  return redirect(url_for('bye'))

@app.route(/bye)
def bye():
  return "Bye"
```

## <a name="python">Python Programming</a>

```python
######################################
# PART 1: Check if string is digit   #
######################################
my_string = '10'
my_string.isdigit() # True

my_other_string = 'hello'
my_other_string.isdigit() # False


######################################
# PART 2: Substitute String          #
######################################
sentence = "My name is %s"
print(sentence %"Alexander") # My name is Alexander

name = "Alexander"
print(sentence %name) # My name is Alexander

sentence = "My name is {name}"
print(sentence.format(name=name)) # My name is Alexander


######################################
# PART 3: Escape HTML                #
######################################
for (i,o) in (#tuples of html tags and escaped versions):
    tag = tag.replace(i, o)

import cgi
cgi.escape(tag, quote = True)

```

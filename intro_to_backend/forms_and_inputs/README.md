# Forms and Inputs

- [Working File](index.html)

Create a form
```
<form>
  <input name="q">
</form>
```

> Due personal reasons, I decided to use Flask instead of WebApp2 and Google App Engine.

## Install Flask and setup

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

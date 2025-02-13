# Table of contents 
- [Table of contents](#table-of-contents)
- [Creating a Flask Application](#creating-a-flask-application)
- [Returning JSON](#returning-json)
  - [Using jsonify()](#using-jsonify)
- [Application Configuration](#application-configuration)
  - [Loading application configuration](#loading-application-configuration)
  - [Application Structure](#application-structure)

# Creating a Flask Application
- Install Flask: `pip install flask`
- Create the main server file (app.py)

```python 
from flask import Flask 
app = Flask(__name__)
```

- Add routes 
  - Use the @app decorator to define the method 
  - Pass in the URL path 
  - Return HTML in the method

```python 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"
```

- Running Flask 
  - Export settings 
    - FLASK_APP
    - FLASK_ENV

```txt
export FLASK_APP=app.py
export FLASK_ENV=development
```
  - We can avoid using them by running the command `flask --app app --debug run`

- Run the application 
  - `flask run`


# Returning JSON
We can return a serializable type by just returning the json component identified by { }

```python 
@app.route('/')
def home():
    return {"message": "Hello World!"}
```

## Using jsonify()
We can use the jsonify method passing key-value pairs returning a JSON to the client. 

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello world!")
    # This will return {"message": "Hello world!"}
```

# Application Configuration 
Other configurations are ENV, DEBUG, TESTING, SECRET_KEY, SESSION_COOKIE_NAME, SERVER_NAME, JSONIFY_MIMETYPE

## Loading application configuration 
Flask provides a config object that acts like a dictionary `app.config['SECRET_KEY'] = "random-secret-key"`

Configure from an environment variable 
`app.config["VARIABLE_NAME"]`
`app.config.from_prefixed_env()`

configure from a python file 
`app.config.from_file("pathtoconfigfile")


## Application Structure 
|--config.json
|--requirements.txt  
|--setup.py
|--src/
|---- __init__.py
|------static/
|------css/
|--------main.css
|------img/
|--------header.png
|------js/
|--------site.js
|------templates
|--------about.html
|--------index.html
|--tests/
|----test_auth.py
|----test_site.py
|--venv
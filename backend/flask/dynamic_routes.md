# Table of contents
- [Table of contents](#table-of-contents)
- [Calling external APIs](#calling-external-apis)
- [Dynamic route parameters](#dynamic-route-parameters)

# Calling external APIs
Can call external APIs using requests. Return JSON as a dictionary. 

```python 
from flask import Flask, escape 
import requests 

app = Flask(__name__)

@app.route("/")
def get_author():
    res = requests.get("https://some_url")
    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message": "Something went wrong!"}, 404
    else:
        return {"message": "Server Error"}, 500
```


# Dynamic route parameters 
RESTful API requires resource ID in the URL
- Provide an API that looks up a book by its ISBN
- Example GET URL: http://localhost/book/1449355830

Dynamic routing would do the following 
```python 
@app.route("/book/<isbn>")
def get_author(isbn):
    res = requests.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON")

    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 400:
        return {"message": "Something went wrong"},404
```


Paramether types that go in a route like the following `@app.route("/path/<type:variable>")`

- string `<str:variable>`
- int `<int:variable>`
- float `float:variable>`
- path `sub[slashes are accepted]`
- uuid `<uuid:uuid>`
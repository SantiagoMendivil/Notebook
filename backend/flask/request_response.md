# Table of contents 
- [Table of contents](#table-of-contents)
- [Custom Routes](#custom-routes)
- [Request Object: Access values](#request-object-access-values)
- [Response Object: Attributes](#response-object-attributes)
- [Response Object: Usage](#response-object-usage)

# Custom Routes 
The `@app.route("/path")` decorator defaults to the GET method. We can use **methods** argument to only allow specific HTTP methods

In this example the GET method is implicit
```python 
@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200
```

In this example the GET method is explicit
```python 
@app.route("/health", methods=["GET"])
def health():
    return jsonify(dict(status="OK")), 200
```

We can **combine request methods** by specifying them in the methods argument, like the following: 

```python 
@app.route("/health", methods=["GET", "POST"])
def health():
    if request.method == "GET":
        return jsonify(status="OK", method="GET"), 200

    if request.method == "POST":
        return jsonify(status="OK", method="POST"), 200
```

Some common request attributes are: 
- server
- headers
- URL
- access_route
- full_path
- is_secure
- is_JSON
- cookies

The header contains the following data: 
- Cache-control 
- Accept
- Accept-encoding
- User-agent
- Accept-language
- Host 


# Request Object: Access values 
You can access the elements returned by the response as a dictionary using the following syntax 

```python 
from flask import Flask, request 
app = Flask(__name__)

@app.route("/home")
def home():
    course = request.args["course"]
    rating = request.args.get("rating")
    return {"message": f"{course} with rating {rating}"}
```

# Response Object: Attributes 
Some of the common response attributes are: 
- status_code
- headers
- content_type
- content_length
- content_encodign
- mimetype
- expires


Some of the common methods 
- set_cookie
- delete_cookie


# Response Object: Usage 
- Success response from @app.route method 
- JSONify method 
- make_response
- redirect response
- abort method 
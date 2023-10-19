#!/usr/bin/python3
"""web flask module"""
from flask import Flask

app = Flask(__name__)


# Define a route to display "Hello HBNB!" with strict_slashes=False
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Define a route to display "HBNB" with strict_slashes=False
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


# Define a route to display "C " followed by the value of the text variable
# Replace underscore _ symbols with a space
@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

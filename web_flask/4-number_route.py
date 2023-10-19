#!/usr/bin/python3
"""web flask module"""
from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)


# Define a route to display "Hello HBNB!" with strict_slashes=False
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """hello hbnb route"""
    return "Hello HBNB!"


# Define a route to display "HBNB" with strict_slashes=False
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb route"""
    return "HBNB"


# Define a route to display "C " followed by the value of the text variable
# Replace underscore _ symbols with a space
@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """c route"""
    text = text.replace("_", " ")
    return "C {}".format(text)


# Define a route to display "Python "
# followed by the value of the text variable
# Replace underscore _ symbols with a space
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """python route"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


# Define a route to display "n is a number" only if n is an integer
@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """number route"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

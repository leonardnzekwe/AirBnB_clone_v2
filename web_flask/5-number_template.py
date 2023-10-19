#!/usr/bin/python3
"""web flask module"""
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


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


# Define a route to display "C "
# followed by the value of the text variable
# Replace underscore _ symbols with a space
@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """c route"""
    text = text.replace("_", " ")
    return "C {}".format(text)


# Define a route to display "Python "
# ollowed by the value of the text variable
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


# Define a route to display an HTML page only if n is an integer
# The page includes an H1 tag with "Number: n"
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number template route"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

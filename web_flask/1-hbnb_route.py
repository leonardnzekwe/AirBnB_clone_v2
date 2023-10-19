#!/usr/bin/python3
"""web flask module"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

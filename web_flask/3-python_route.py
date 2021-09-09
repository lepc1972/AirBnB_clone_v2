#!/usr/bin/python3
"""flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB!'


@app.route('/c/<text>')
def c_route(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def py_route(text="is cool"):
    return "Python {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

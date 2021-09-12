#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_one(id=None):
    states = storage.all(State)
    if id:
        key = 'State.{}'.format(id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

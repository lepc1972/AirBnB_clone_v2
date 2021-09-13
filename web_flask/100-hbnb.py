#!/usr/bin/python3
"""Starting flask server"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask
from flask import render_template
from models.place import Place
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_html():
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', **locals())


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

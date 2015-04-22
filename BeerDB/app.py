from flask import Flask
from flask import render_template
from pymongo import Connection
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'beerDB'
COLLECTION_NAME = 'beers'
FIELDS = {
    '_id': True,
    'name': True,
    'brewer': True,
    'abv': True,
    'malt': True,
    'hops': True,
    'note': True
}


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

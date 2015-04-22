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

# connection
# collection
# Helper function to establish connection to the database.
# def connect():
#     connection = Connection(MONGODB_HOST, MONGODB_PORT)
#     collection = connection[DBS_NAME][COLLECTION_NAME]

# Helper function to disconnect from the database.
# def disconnect():
#     connection.disconnect()

# Define route for home page.
@app.route("/")
def index():
    return render_template("index.html")


# Get all beers from database.
@app.route("/beers/all")
def beers_all():
    connection = Connection(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    beers = collection.find(fields=FIELDS, limit=50000)
    json_beers = []
    for beer in beers:
        json_beers.append(beer)
    json_beers = json.dumps(json_beers, default=json_util.default)
    connection.disconnect()
    return json_beers


# Add new beer to database.
# ...


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

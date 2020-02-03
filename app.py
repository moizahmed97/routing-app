from flask import Flask,url_for, render_template, request,redirect,session,jsonify
from connect import client
from sampledata import firstCoordinate,secondCoordinate
from bson.json_util import dumps
import json


db = client.routes # Database is called routes

coordinates = db.coordinates # collection (table) called coordinates 

# Insert the sample data (Only for the first time, get it from the sampledata file)
# coordinates.insert_many([firstCoordinate, secondCoordinate]) # Insert document (row) into collection (table) people

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        allCoordinates = dumps(coordinates.find())  # get all the coordinates as objects from the Database
        allCoordinates = json.loads(allCoordinates)
        return render_template("index.html", data = allCoordinates)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask,url_for, render_template, request,redirect,session,jsonify
from connect import client
from bson.json_util import dumps
import json
from connect import API_KEY


db = client.routes # Database is called routes

coordinates = db.coordinates # collection (table) called coordinates 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    # when the user has not selected which route they need
    if request.method == 'GET':
        allCoordinates = dumps(coordinates.find())  # get all the coordinates as objects from the Database
        allCoordinates = json.loads(allCoordinates)
        return render_template("index.html", data = allCoordinates, API_KEY=API_KEY)
    # When the user has clicked on one of the routes to display it    
    elif request.method == 'POST':
        # get the ID 
        coordinateClickedID = request.get_json()
        # the JSON object has id in string so convert it to Integer
        intID = int(coordinateClickedID["id"])
        # Get the coordinates for the ID clicked using a query to MongoDB
        query = db.coordinates.find_one({'id': intID })
        # send it back in JSON Format 
        dict = {
            "fromCoordinates" : query["fromCoordinates"],
            "toCoordinates" : query["toCoordinates"]
             } 
        return jsonify(dict)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)


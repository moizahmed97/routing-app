from flask import Flask,url_for, render_template, request,redirect,session
from connect import client

db = client.routes # create new database called routes

coordinates = db.coordinates # create new collection (table) called coordinates 

firstCoordinate = {             # Sample Data 
    "id" : 1,
    "From" : "Big Ben Tower",
    "To" : "Millenium Dome",
    "fromCoordinates" : "51.500729, -0.124625",
    "toCoordinates" : "44.837730, -0.687530",
    "Description" : "Coordinates for the two iconic locations in London: The Millenium Dome and the Big Ben Clock tower", 
}
secondCoordinate = {
    "id" : 2,
    "From" : "The Great Pyramid of Khufu",
    "To" : "The Pyramid of Sneferu",
    "fromCoordinates" :"29.979235, 31.134201",
    "toCoordinates" : "29.808333, 31.205833",
    "Description" : "Coordinates for the Great Pyramid of Giza (Khufu) and the The Red Pyramid of Dahshur",
}

# Insert the sample data (Only for the first time)
# coordinates.insert_many([firstCoordinate, secondCoordinate]) # Insert document (row) into collection (table) people

app = Flask(__name__)
# required for session management
app.secret_key = "skdlfj235647fhf"

@app.route("/")
def home():
    allCoordinates = coordinates.find()  # get all the coordinates as objects from the Database
    return render_template("index.html", data=allCoordinates)

@app.route("/display")
def display():
    return render_template("display.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)


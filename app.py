from flask import Flask,url_for, render_template, request,redirect,session,jsonify
from connect import client
from sampledata import firstCoordinate,secondCoordinate

db = client.routes # Database is called routes

coordinates = db.coordinates # collection (table) called coordinates 

# Insert the sample data (Only for the first time, get it from the sampledata file)
# coordinates.insert_many([firstCoordinate, secondCoordinate]) # Insert document (row) into collection (table) people

app = Flask(__name__)
# required for session management
app.secret_key = "skdlfj235647fhf"

sampleList = []

sampleList.append(firstCoordinate)
sampleList.append(secondCoordinate)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        allCoordinates = coordinates.find()  # get all the coordinates as objects from the Database
        return render_template("index.html", data = allCoordinates)
    elif request.method == 'POST':
        # get the data sent by AJAX from index.html
        test = request.form["check"]
        print(test)
        return redirect(url_for('display'))


@app.route("/display")
def display():
    return render_template("display.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)



"""  @app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
"""
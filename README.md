# routing-app
Flask Web App CHanged to Atlas Mongo Database that calculates the directions from one point to another using the HERE Maps Routing API 

# Important Note on Implementing
To communicate with Atlas the mongoDB database and the HERE routing API we need to store the environment variables in a env file which has been ignored here 
So create a .env file in the main directory with the following fields:

```
USERNAME = ''
PASSWORD = ''
API_KEY = ''
```
Enter ther username and password for the Atlas database as well as the API_KEY from the HERE developer dashboard between the quotes



## Features 
- Connected to Cloud NoSQL Database (MongoDB Atlas)
- Uses Flask (Python) as the server side language for querying with Atlas
- The Here Maps JavaScript API is used to get the coordinates and then display the route in a Modal
- Mobile first app

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


# Insert the sample data (Only for the first time, get it from the sampledata file)
# coordinates.insert_many([firstCoordinate, secondCoordinate]) # Insert document (row) into collection (table) people
"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb destinations')
os.system('createdb destinations')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/destinations.json') as f:
    destinations_data = json.loads(f.read())

# Create destinations, store them in list so we can use them
# to favorite them later
destinations_in_db = []
for destination in destinations_data:

    destination_type, average_overall_rating, name, population, latitude, longitude, url = (destination["destination_type"], destination["average_overall_rating"], destination["name"], destination["population"], destination["latitude"], destination["longitude"], destination["url"])

    db_destination = crud.create_destination(destination_type, 
                                            average_overall_rating, 
                                            name, 
                                            population, 
                                            latitude, 
                                            longitude,
                                            url)

    #Created a destination object here and appended it to destinations_in_db list
    destinations_in_db.append(db_destination)   

with open('data/users.json') as f:
    users_data = json.loads(f.read())

# Create users, store them in list so we can use them
users_in_db = []
for user in users_data:

    email, password, first_name, last_name = (user['email'], user['password'], user['first_name'], user['last_name'])

    db_user = crud.create_user(email, 
                            password, 
                            first_name, 
                            last_name)

    users_in_db.append(db_user)
    
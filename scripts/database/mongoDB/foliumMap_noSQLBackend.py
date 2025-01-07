
# This script creates a map with the location of clubs, bars and restaurants in Zurich. The data is stored in a MongoDB database. The script connects to the database, retrieves the data and creates a map with the location of the clubs, bars and restaurants. The map is saved as an HTML file.
# Data source for open data api: https://data.stadt-zuerich.ch/dataset/zt_nachtleben
# 2025-01-07 Modul 122 
# BFSU-Informatik, Dominik Reuss

import folium
from pymongo import MongoClient

# Uses public atlas cluster for demonstration purposes from MongoDB
# user is readonly on a single instance of the cluster
uri = "mongodb+srv://bfsu_student:wOI4JY5AZLY82v5u@myatlasclusteredu.jxymz.mongodb.net/?retryWrites=true&w=majority&appName=myAtlasClusterEDU"

client = MongoClient(uri)

db = client['clubs_ZH']
collection = db['Lokale']

map = folium.Map(location=[46.8182, 8.2275], zoom_start=8)

numberofdocuments = collection.estimated_document_count()
map_title = f"Raum Zürich: {numberofdocuments} Clubs, Bars und Restaurants"
title_html = f'<h1 style="position:absolute;z-index:100000;left:40vw" >{map_title}</h1>'
map.get_root().html.add_child(folium.Element(title_html))

for lokal in collection.find():
    folium.Marker(
        location=[lokal['geoCoordinates']['latitude'],lokal['geoCoordinates']['longitude']],
        popup=f"{lokal['name']['de']}<br>Adresse: {lokal['address']['streetAddress']}<br>Telefon: {lokal['address']['telephone']} <br>URL: <a href='{lokal['address']['url']}' target='_blank'>{lokal['address']['url']}</a>",
    ).add_to(map)

map.save('index.html')

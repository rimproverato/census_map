# Importing required libraries
import folium
import pandas

# Getting the longitude and latitude of all the countries
countries_locations = pandas.read_csv("countries.csv")
lat = list(countries_locations["latitude"])
lon = list(countries_locations["longitude"])

# Looping through the countries 
geo_map = folium.Map(location=[8.7832, 34.5085], zoom_start=3.8)
geo_map.save("map.html")


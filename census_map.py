# Importing required libraries
import folium
import pandas

# Getting the longitude and latitude of all the countries
countries_locations = pandas.read_csv("countries.csv")
lat = list(countries_locations["latitude"])
lon = list(countries_locations["longitude"])

# trying to convert to numeric so that i do not have any 'Naans'
lt = pandas.to_numeric(lat)
lg = pandas.to_numeric(lon)

# Looping through the countries 
geo_map = folium.Map(location=[8.7832, 34.5085], zoom_start=3.8)
background = folium.FeatureGroup(name= "Population map")
for lt, lg in zip(lat, lon):
    background.add_child(folium.Marker(location= [lt , lg], popup= "population: ", icon=folium.Icon(color="blue")))

# Rendering, displaying to the web
geo_map.add_child(background)
geo_map.save("map.html")


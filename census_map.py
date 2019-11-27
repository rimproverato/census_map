# Importing required libraries
import folium
import pandas

# Getting the longitude and latitude of all the countries
countries_locations = pandas.read_csv("countries.csv")
population = pandas.read_csv("pop_total_ds2_en_v2.csv")
lat = list(countries_locations["latitude"])
lon = list(countries_locations["longitude"])
pupltn = list(population["column_b"])

# trying to convert to numeric so that i do not have any 'Naans'
lt = pandas.to_numeric(lat)
lg = pandas.to_numeric(lon)

# change popup color depending on population
def icon_color (country_population):
    if countries_locations < 100:
        return "green"
    elif countries_locations <= 1000:
        return "blue"
    elif countries_locations <= 10000:
        return "purple"
    elif countries_locations <= 100000:
        return "darkpurple"
    elif countries_locations <= 1000000:
        return "orange"
    elif countries_locations <= 10000000:
        return "lightred"
    elif countries_locations <= 100000000:
        return "cadetblue"
    else:
        return "beige"

# Looping through the countries 
geo_map = folium.Map(location=[8.7832, 34.5085], zoom_start=3.8)
background = folium.FeatureGroup(name= "Population map")
for lt, lg, ppl in zip(lat, lon, pupltn):
    background.add_child(folium.Marker(location= [lt , lg], popup= f"population: {ppl}", icon=folium.Icon(color=icon_color(ppl))))

# Rendering, displaying to the web
geo_map.add_child(background)
geo_map.save("map.html")


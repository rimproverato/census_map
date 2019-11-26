import folium
import pandas

geo_map = folium.Map(location=[8.7832, 34.5085], zoom_start=3.8)
geo_map.save("map.html")

data = pandas.read_csv("countries.csv")
print(data)
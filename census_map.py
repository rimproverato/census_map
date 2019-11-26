import folium

geo_map = folium.Map(location=[0.0236, 37.9062] zoom_start=9)
geo_map.save("map.html")
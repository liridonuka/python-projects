import folium
list = [1,2,4,6,7,8,14]
a = list[-3:-1]

result = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright", max_zoom = 4)
print(type(result))

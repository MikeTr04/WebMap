"""LAB MAP"""

import argparse
import haversine
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

parser = argparse.ArgumentParser(description="Task Map")
parser.add_argument("year", help="year of movie")
parser.add_argument("lat", help="latitude")
parser.add_argument("lon", help="longitude")
parser.add_argument("path", help="path to dataset")
args = parser.parse_args()
year = int(args.year)
lat = float(args.lat)
lon = float(args.lon)
path = args.path

geolocator = Nominatim(user_agent="myGeocoder")
map1 = folium.Map(zoom_start=10)
try:
    LOCATION = geolocator.reverse([lat, lon])
except GeocoderUnavailable:
    LOCATION = "Some location"
main_group = folium.FeatureGroup()
main_group.add_child(folium.CircleMarker(location=[lat, lon],
                                         popup=LOCATION,
                                         radius=7,
                                         fill_color="green"))
map1.add_child(main_group)

film_locations = folium.FeatureGroup()
with open(path, "r", encoding="cp1252") as file1:
    lines = file1.readlines()
for i, x in enumerate(lines):
    if "LOCATIONS LIST\n" == x:
        lines = lines[i + 2:]
        break
films = []
for i in lines[:60]:
    film = i.split("\t")
    while '' in film:
        film.remove('')
    film = film[:2]
    film[1] = film[1].strip("\n")
    loc = geolocator.geocode(film[1])
    while loc is None:
        film[1] = ", ".join(film[1].split(", ")[1:])
        loc = geolocator.geocode(film[1])
    loc = loc.latitude, loc.longitude
    distance = haversine.haversine_vector(loc, (lat, lon))
    year1 = int(film[0][film[0].index('(') + 1:film[0].index(')')])
    films.append((film[0], distance[0], year1, loc))
films.sort(key=lambda x: x[1])
COUNTER = 0
for i in films:
    if year == i[2]:
        film_locations.add_child(folium.Marker(location=list(i[3]),
                                               popup=i[0],
                                               icon=folium.Icon(color="red")))
        COUNTER += 1
        if COUNTER == 10:
            break
map1.add_child(film_locations)

cities = folium.FeatureGroup()
kyiv = geolocator.geocode("Kyiv, Ukraine")
kyiv = kyiv.latitude, kyiv.longitude
lviv = geolocator.geocode("Lviv, Ukraine")
lviv = lviv.latitude, lviv.longitude
dnipro = geolocator.geocode("Dnipro, Ukraine")
dnipro = dnipro.latitude, dnipro.longitude
cities.add_child(folium.Marker(location=kyiv, popup="Kyiv, Ukraine", icon=folium.Icon()))
cities.add_child(folium.Marker(location=dnipro, popup="Dnipro, Ukraine", icon=folium.Icon()))
cities.add_child(folium.Marker(location=lviv, popup="Lviv, Ukraine", icon=folium.Icon()))
map1.add_child(cities)

map1.fit_bounds(map1.get_bounds())
map1.save("map.html")

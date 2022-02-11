# WebMap

WebMap is a python program that was made to solve the second task in lab 1.

## Purpose

The task was to create a map with the films that were made the closest to the given location and in a specified year. The locations needed to be marked on a Folium map, and saved in an HTML file. In addition, there needed to be overall 3 feature groups: main group, film locations, and another one with no specific task. In my third group, I put markers on some of Ukraine's biggest cities.

The main group consists of 1 circle marker, which is on the location location given by the user.

The film location group consists of locations where movies where made and are marked in red icons.

The cities group consists of 3 Ukrainian cities and their locations: Kyiv, Lviv, and Dnipro. They are marked in blue icons.

The map is saved in the directory of the program in the file with the title "map.html".

The amount of entries in the dataset that are being used is limited to 60 to ensure that map generation does not take too much time.

In this task, the modules argparse, haversine, folium, and geopy were used.

## Usage

The program uses argparse to get the argument values: year, latitude, longitude, and path to dataset.

```python
>>> python main.py 2015 49.83826 24.02324 locations.list
```
Here is the map generated after executing the code above:

![Map example](example.jpg?raw=true)


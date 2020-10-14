
# Exercise 16_7
# date: 13/10/2020

# Data visualisation of the most recent earthquake activities.

import json
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

# Exploring the structure of the data
filename = "C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/json_formated_data/all_hour_earthquake.geojson"
with open(filename) as f:
    recent_eq_data = json.load(f)

readable_file = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/json_formated_data/readable_all_hour_earthquake.geojson'
with open(readable_file, 'w') as f:
    json.dump(recent_eq_data, f, indent=4)

# Making the list of all earthquakes of past hour
recent_eq_dicts = recent_eq_data["features"]
recent_type_dicts = recent_eq_data["metadata"]

# Extracting Magnitudes and location data
mags = [eq_dict['properties']['mag'] for eq_dict in recent_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in recent_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in recent_eq_dicts]
hover_texts = [eq_dict['properties']['title'] for eq_dict in recent_eq_dicts]
title = recent_type_dicts['title']
print(title)


# Map the earthquakes.
# Customized Marker Size
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Electric',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
        },
    }]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/self Work/global-past_hour_earthquakess.html')

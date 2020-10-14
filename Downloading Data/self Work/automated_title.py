
# Exercise 16_7
# date: 13/10/2020
#Refactoring the all_eq_dicts by removing temporary variable

# Building a World Map

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Exploring the structure of the data
filename = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/json_formated_data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/json_formated_data/readable_eq_data.json'
with open(readable_file, 'w' ) as f:
    json.dump(all_eq_data, f, indent=4)

# Making the list of all earthquakes
all_eq_dicts = all_eq_data['features']
eq_type_dicts = all_eq_data['metadata']

# Extracting Magnitudes and location data
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]
title = eq_type_dicts['title']
print(title)

print(mags)

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
offline.plot(fig, filename='C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/self Work/global_earthquakess.html')
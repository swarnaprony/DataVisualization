# Exercise_16_9
# date: 14/10/2020
# Making world map shows the affected places by fire

import csv
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

filename = 'C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/csv_formated_data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Making the list of all places affected by fire
    lons, lats, brights= [], [], []
    for row in reader:
        lon = row[header_row.index('longitude')]
        lat = row[header_row.index('latitude')]
        bright = float(row[header_row.index('brightness')])
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)
#print(brights)
#print(lats)


# Map the earthquakes.
# Customized Marker Size
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [1/50*bright for bright in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
        },
    }]
my_layout = Layout(title="World Fire Map")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='C:/Users/asifhossain/Documents/python_projects/Data Visualization/Downloading Data/self Work/world_fire_map.html')

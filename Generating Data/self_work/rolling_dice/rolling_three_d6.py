#exercise_15_7
#date: 19/8/2020

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die8 import Die

#Creating three blueprint of Die class
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

#Rolling the dices for sometimes and store the results
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
print(results)

# Find the frequency of apearing of every possible values
values = []
frequencies = []
frequency_tuples = []

for value in range(3, die_1.num_sides + die_2.num_sides+ die_3.num_sides +1):
    values.append(value)
    frequency = results.count(value)
    frequencies.append(frequency)
    frequency_tuple = [(value, frequency)]
    frequency_tuples.append(frequency_tuple)
print(frequency_tuples)

# Visualization of frequency of apearing of every possible values

data = [Bar(x=values, y=frequencies)]
x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

my_layout = Layout(title='Result of rolling three d8 1000 time in a row', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data,'layout': my_layout}, filename='d8_d8_d8.html')
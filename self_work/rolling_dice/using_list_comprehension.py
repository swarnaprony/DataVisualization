#exercise_15_9
#date: 19/08/2020

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die8 import Die

#Creating three blueprint of Die class
die_1 = Die(6)
die_2 = Die(6)

#Rolling the dices for sometimes and store the results
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# Find the frequency of apearing of every possible values

values = [value for value in range(3, die_1.num_sides * die_2.num_sides +1)]
frequencies = [results.count(value) for value in range(3, die_1.num_sides * die_2.num_sides +1)]
frequency_tuples = [(value, results.count(value)) for value in range(3, die_1.num_sides * die_2.num_sides +1)]
print(frequency_tuples)

# Visualization of frequency of apearing of every possible values

data = [Bar(x=values, y=frequencies)]
x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}

my_layout = Layout(title='Result of rolling three d8 1000 time in a row', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data,'layout': my_layout}, filename='multiply_two_d6.html')
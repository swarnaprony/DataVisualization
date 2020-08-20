from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# Analyze the result
frequencies = []
frequencies_tuple = []
values = []
for value in range(2, die_1.num_sides+die_2.num_sides+1):
    values.append(value)
    frquency = results.count(value)
    frequencies.append(frquency)
    frquency_tuple = [(value, frquency)] 
    frequencies_tuple.append(frquency_tuple)

print(frequencies)
print(frequencies_tuple)


# Visualize the results.
data = [Bar(x=values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6
die = Die()

# Make some rolls and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# Analyze the result
frequencies = []
frequencies_tuple = []
values = []
for value in range(1, die.num_sides+1):
    values.append(value)
    frquency = results.count(value)
    frequencies.append(frquency)
    frquency_tuple = [(value, frquency)] 
    frequencies_tuple.append(frquency_tuple)

print(frequencies)
print(frequencies_tuple)


# Visualize the results.
data = [Bar(x=values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axix_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axix_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6html')
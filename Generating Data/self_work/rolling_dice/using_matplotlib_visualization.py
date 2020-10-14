import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



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





x_axis = np.arange(len(values))

plt.bar(x_axis, frequencies, align='center', alpha=0.5)
plt.xticks(x_axis, values)
plt.ylabel('Frequencies of apearing each value.')
plt.title('Result of rolling three d8 1000 time in a row')

plt.show()
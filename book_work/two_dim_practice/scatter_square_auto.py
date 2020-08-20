
#Calculating data automatically

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

#defining custom colour
#ax.scatter(x_values, y_values, c = 'green', s = 10)
#this should not use
#ax.scatter(x_values, y_values, c = (0, 0.2, 0.5), s = 10)

#using a Colormap
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)


#set chart title and label axes

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set size of tick labels.
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

#set the range for axis
ax.axis([0, 1100 , 0, 1100000])

#Saving plots Automstically
plt.savefig('square_plot.png', bbox_inches = 'tight')



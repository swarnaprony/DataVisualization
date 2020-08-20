#exercise_15_3_4_5
#date: 18/08/2020

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make a random walk
rw = RandomWalk()

rw.fill_walks()

#Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth = 0.5, color = 'r')
plt.show()


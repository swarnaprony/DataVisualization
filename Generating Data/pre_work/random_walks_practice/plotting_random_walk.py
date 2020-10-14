#Plotting the Random Walk

import matplotlib.pyplot as plt

from random_walk import RandomWalk


#keep creating random walks, as long as the program is actice.

while True:
    #create a random walk blueprint with increasing the value of num_points
    rw = RandomWalk(500_000)
    rw.fill_walks()

    #Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (15,9))

    #style the plotting

    #coloring the points
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)


    #plotting the starting and ending point
    ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

    #Cleaning up the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    #plt.savefig('plotting_random_walk.png', bbox_inches = 'tight')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

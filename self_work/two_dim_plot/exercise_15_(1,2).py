#exercise_15_(1,2)
#date: 29/06/2020
#cubes

import matplotlib.pyplot as plt

def cube_number():
    """Calculate cubes of first 5 numbers"""

    x_values = [1, 2, 3, 4, 5]
    y_values = [x**3 for x in x_values]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.scatter(x_values, y_values, c = 'pink' , s = 10)

    ax.set_title('Cube of Numbers', fontsize = 22)
    ax.set_xlabel('Values', fontsize = 12)
    ax.set_ylabel('Cube values', fontsize = 12)
    ax.tick_params( axis = 'both', which = 'major', labelsize = 14)


    plt.show()

cube_number()


def cube_number_range():
    """Calculate cubes of first 5000 numbers"""

    x_values = range(1, 5001)
    y_values = [x**3 for x in x_values]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    #exercise_15_2
    #using colormap on this figure
    ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Greens, s = 10)

    ax.set_title('Cube of Numbers', fontsize = 22)
    ax.set_xlabel('Values', fontsize = 12)
    ax.set_ylabel('Cube values', fontsize = 12)
    ax.tick_params( axis = 'both', which = 'major', labelsize = 14)
    ax.axis([0, 6000, 0, 216000000000])


    plt.savefig('cube_plot_range.png', bbox_inches = 'tight')

cube_number_range()
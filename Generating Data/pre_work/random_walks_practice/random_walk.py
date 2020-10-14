#creating random walks class
#date: 29/06/2020

from random import choice

#Creating the Randomwalk() class
class RandomWalk():
    """A class to generate random walks"""

    def __init__(self, num_points = 50000):
        """Initialize attribues of a walk"""
        self.num_points = num_points
 
        #All walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    #Chosing Directions

    def get_x_step(self):
        #Decide which direction to go and how far to go in that direction.
            
        x_direction = choice([1])
        x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x = x_direction * x_distance
        return x

    def get_y_step(self):
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y = y_direction * y_distance
        return y



    def fill_walks(self):
        """Calcutates all te points in the walk"""

        #keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            x_step = self.get_x_step()
            y_step = self.get_y_step()
            print(x_step, y_step)
            
            #Reject steps that goes nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

ranwalk = RandomWalk()
ranwalk.fill_walks()
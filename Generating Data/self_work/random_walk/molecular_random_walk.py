#creating random walks class
#date: 29/06/2020

from random import choice

#Creating the Randomwalk() class
class RandomWalk():
    """A class to generate random walks"""

    def __init__(self, num_points = 5000):
        """Initialize attribues of a walk"""
        self.num_points = num_points
 
        #All walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        self.x_step = []
        self.y_step = []

    #Chosing Directions

    def get_step(self):
        #Decide which direction to go and how far to go in that direction.

        #keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:


            #Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            self.x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            self.y_step = y_direction * y_distance

            #Reject steps that goes nowhere
            if self.x_step == 0 and self.y_step == 0:
                continue

    def fill_walks(self):
        """Calcutates all te points in the walk"""


        #Calculate the new position
        for x_step in self.x_step:
            x = self.x_values[-1] + x_step
            self.x_values.append(x)
        for y_step in self.y_step:
            y = self.y_values[-1] + self.y_step
            self.y_values.append(y)
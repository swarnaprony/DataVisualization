#exercise_15_(6_10)
#date: 19/08/2020

from random import randint

class Die:
    """A class representing a simple die"""

    def __init__(self, num_sides=8):
        """Asume a six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
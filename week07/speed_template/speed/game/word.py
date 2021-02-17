import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here

class Food(Actor):
    """Delicious red apples for an herbivorous snake to eat
        In charge of keeping track of appearance and position of food.

    Stereotype:
        Information Holder

    Attributes:
        _points: integer, the number of points a fruit is worth
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.set_text('@')
        self.set_position(Point(0, 0))
        self.set_velocity((0, 0))
        self.reset()

    def get_points(self):
        """
        Returns the current number of points
        """
        self._points = random.randint(1, 5)
        return self._points

    def reset(self):
        """
        Resets the position of the food
        """
        self.set_position(Point((random.randint(1, 60)), (random.randint(1,20))))
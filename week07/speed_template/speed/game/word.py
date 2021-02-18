import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """Delicious red apples for an herbivorous snake to eat
        In charge of keeping track of appearance and position of food.

    Stereotype:
        Information Holder

    Attributes:
        _points: integer, the number of points a fruit is worth
    """
    def __init__(self):
        super().__init__()
        # self._points = 0
        # self.set_text('@')
        # self.set_position(Point(0, 0))
        self.set_velocity((0.5, 0))
        # self.reset()

        self.word_library = constants.LIBRARY

    def send_word(self):
        """
        This class will return word_library when called

            self.word_library: a list of all the words from constant "library"
        """
        return self.word_library[random.randint(0, len(self.word_library) - 1)]

    # def reset(self):
    #     """
    #     Resets the position of the food
    #     """
    #     self.set_position(Point((random.randint(1, 60)), (random.randint(1,20))))
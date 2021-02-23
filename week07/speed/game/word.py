import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """A subclass of actor. In charge of keeping track of a word. Also remembers position and velocity of the word.

    Stereotype:
        Information Holder

    Attributes:
        text: the value of the word
        position: the initial position of the word
        velocity: how fast it is moving
        
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initiallizes the library with all the words, 
        sets the position, sets velocity, and sets point value equal to length of word.
        
        Args:
            self (Word): an instance of Word.
        """
        super().__init__()
        self.set_text(constants.LIBRARY[random.randint(0, len(constants.LIBRARY) - 1)])
        self.set_position(Point(0, (random.randint(2, constants.MAX_Y - 2))))
        self.set_velocity(Point(1, 0))

        # Let's make the points be worth the length of the word.
        self._points = len(self._text)

    def get_points(self):
        """Returns the points earned from the word being typed.
        
        Args:
            self (Word): an instance of Word.
        """
        return self._points




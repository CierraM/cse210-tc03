from game import constants
from game.actor import Actor
from game.point import Point

# CHANGE THIS ONE

class Buffer(Actor):
    """The spot where you write words
        A subclass of actor
        Keeps track of letters the player is typing in
        Add letter

    Stereotype:
        Information holder

    Attributes:
        _letters: keeps track of the letters the player inputted
    """
    def __init__(self):
        """
            The class constructor.
        
        Args:
            self (buffer): An instance of buffer.
        """
        super().__init__()
        self._letters = []
        self.set_position(Point(7, constants.MAX_Y))
        self.set_text("Buffer:")
    def add_letter(self, letter):
        """
            If the letter is a *, clear the buffer. Otherwise, it adds the letter onto the buffer

        Args:
            self (buffer): An instance of buffer.
            letter (str): the letters the user inputs
        """
        if letter == '*':
            self._letters.clear()
        else:
            self._letters.append(letter)
        
        self.set_text("".join(self._letters))

    def is_word(self, word):
        """
            Makes the list of letters into a string, and compares them to the words on the screen.

        Args:
            self (buffer): An instance of buffer.
            word (str): the word on the screen
        """
        word_to_string = ''.join(self._letters)
        if word_to_string == word:
            return True
        else:
            return False

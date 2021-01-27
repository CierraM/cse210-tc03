from flipper import Flipper
"""
Imports the flipper class from the previous file.
"""
class Host:
    """
    This class is responsible for keeping control over the sequence of play.
    Attributes include: Setting the player's base score as 300 at the start of the game, keep playing whether or
    not the player wants to keep playing, and displaying score and asking for another round.
    """
    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.flipper = Flipper()
    """
    Class constructor. Calls other functions. 
    """
    def start(self):
        self.card_input()
        while self.keep_playing:
            self.card_guess()
            self.card_input()
            self.card_update()
    """
    Start sequence of game, starts the loop.
    """            
    def card_input(self):
        self.flipper.card_flip()
    """
    Gets the inputs at the beginning of each round, AKA flipping the cards.
    """
    def card_guess(self):
        self.score += self.flipper.compare()
        print(f"Your score is: {self.score}")
    """
    Displays card score to user.
    """
    def card_update(self):
        choice = input("Keep playing? [y/n] ")
        self.keep_playing = (choice == "y")
    """
    Asks the user if they want to keep playing the game.
    """
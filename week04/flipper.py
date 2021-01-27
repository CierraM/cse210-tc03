import random
"""
Importing the random function to get a truly random number for the game.
"""
class Flipper:
    """
    This code is a template for flipping cards, the responsibility for the class is to add or subtract points
    from the player if they do not guess the right option for the second card drawn based on the first card
    drawn. 
    """
    def __init__(self):
        self.card = 0
        self.previous_card = 0
    """
    __init__ starts off the hard value of the player's card and the dealer's card as 0.
    """
    def compare(self):
        print(f"\nThe card is: {self.previous_card}")
        print("Higher or lower? [h/l] ")
        guess = input()
        print(f"\nNext card was: {self.card}")
        if guess == "h":
            if self.card > self.previous_card:
                return 100
            else:
                return -75
        else:
            if self.card < self.previous_card:
                return 100
            else:
                return -75
    """
    Compare displays the card numbers, and adds/subracts points to/from the user based on the input.
    """
    def card_flip(self):
        self.previous_card = self.card
        self.card = random.randint(1, 13)
    """
    Random card number generator between 1 and 13.
    """
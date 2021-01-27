import random
"""
"""
class Flipper:
    """
    """
    def __init__(self):
        self.card = 0
        self.previous_card = 0
    """
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
    """
    def card_flip(self):
        self.previous_card = self.card
        self.card = random.randint(1, 13)
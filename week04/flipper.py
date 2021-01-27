import random
"""
"""
class Flipper:
    """
    """
    def __init__(self):
        initial = random.randint(1,13)
        self.card = initial
        self.previous_card = 0


    """
    """
    def compare(self):



        print(f"\nThe card is: {self.check_for_face(self.previous_card)}")
        print("Higher or lower? [h/l] ")
        guess = input()
        
        print(f"\nNext card was: {self.check_for_face(self.card)}")
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

    """
    Checks if the card is a face card, returns the proper card name
    """
    def check_for_face(self, card):

        if card == 11:
            return "Jack"
        elif card == 12:
            return "Queen"
        elif card == 13:
            return "King"
        elif card == 1:
            return "Ace"
        else:
            return card

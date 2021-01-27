from flipper import Flipper
"""
"""
class Host:
    """
    """
    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.flipper = Flipper()
    """
    """
    def start(self):
        self.card_input()
        while self.keep_playing:
            self.card_guess()
            self.card_input()
            self.card_update()
    """
    """            

    def card_input(self):
        self.flipper.card_flip()
    """
    """
    def card_guess(self):
        self.score += self.flipper.compare()
        print(f"Your score is: {self.score}")
    """
    """
    def card_update(self):
        choice = input("Keep playing? [y/n] ")
        self.keep_playing = (choice == "y")
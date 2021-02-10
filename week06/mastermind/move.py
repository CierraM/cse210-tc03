class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (integer): The player's guess.

    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self.guess = guess

    def get_guess(self):
        """Returns The player's guess.

        Args:
            self (Move): an instance of Move.
        """
        return self.guess
    

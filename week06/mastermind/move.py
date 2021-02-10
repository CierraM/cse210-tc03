class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of a move.
    
    Stereotype: 
        Information Holder

    Attributes:
        _move: a number representing a guess
        
    """
    def __init__(self, move):
        self._move = move

    def get_move(self):
        return self._move
    

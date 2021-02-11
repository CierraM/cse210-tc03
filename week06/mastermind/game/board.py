import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _codes (list): The number of codes of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._codes = [] #random generated code
        self._hints = [] #Special charecters
        self._guess = [] #last guess
        self.winner = False
        

    def add_roster(self, roster):
        self._roster = roster
        self.num_players = roster.get_players()
        self._prepare()

    def generate_hint(self, code, guess):
        s_code = str(code)
        hint = ''
        s_guess = str(guess)
        for i in range(0, len(s_guess)):
            if s_guess[i] == s_code[i]:
                hint += 'x'
            elif s_code.find(s_guess[i]) != -1:
                hint += 'o'
            else:
                hint += '*'
        return hint

    def is_winner(self):
        return self.winner

    def apply(self, player, move):
        """Applies the given guess to the playing surface. In this case, that 
        means updating the hint for player
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
        guess = move.get_guess()

        #calculate the new hint from the guess
        # self._codes = [] random genreated code
        # self._hints = [] Special charecters
        # self._guess = [] last guess
        # self._guess = guess
        code = self._codes[player.get_index()]
        self._guess[player.get_index()] = guess
        self._hints[player.get_index()] = self.generate_hint(code, guess)
        return "xxxx" == self._hints[player.get_index()]


    def to_string(self):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """ 
        text =  "\n--------------------"
        for n in range(self.num_players):
            print(self._roster.players[n].get_name())
            print(self._guess[n])
            print(self._hints[n])
            text += (f"\nPlayer {self._roster.players[n].get_name()}: {self._guess[n]}, {self._hints[n]}")
        text += "\n--------------------"
        return text

    def _prepare(self):
        """Sets up the board with random numbers for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        for n in range(self.num_players):
            self._codes.append(random.randint(1000, 9999)) 
            self._hints.append("****")
            self._guess.append("----") 

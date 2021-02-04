from Console import Console
from Jumper import Jumper
from Word import Word

class Director:
    """
    The code template for the user to direct the hangman game, director is in charge of the control over the sequence of play
        
         Stereotype:
        Controller
    """
    def __init__(self):
        self.console = Console()
        self.jumper = Jumper()
        self.word = Word()
        self.keep_playing = True
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """

    def start_game(self):

        while self.keep_playing:
            self.do_updates(self.get_inputs())
            if self.jumper.is_dead():
                self.console.write("You are DEAD!")
                self.keep_playing = False
            if self.word.check_finish():
                self.console.write("You are a Winner")
                self.keep_playing = False
            self.do_outputs()
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
    def get_inputs(self):
        letter = self.console.read_letter("Guess a letter [a-z]:")
        return letter
        """Gets the inputs at the beginning of each round of play. Gets the letter from the user.

        Args:
            self (Director): An instance of Director.
        """
    def do_updates(self,letter):
        if not self.word.guess(letter):
            self.jumper.cut_line()
        """Updates the important game information for each round of play. Which would include if not the chosen letter cutting the parachute.

        Args:
            self (Director): An instance of Director.
        """
    def do_outputs(self):
        self.console.horiz_array(self.word.send_updated_puzzle())
        self.console.vertical_array(self.jumper.get_parachute())
        """Outputs the important game information for each round of play. letting the User know what words are right and how many chnaces they have left.

        Args:
            self (Director): An instance of Director.
        """
    

    

    

    

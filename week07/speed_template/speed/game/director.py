from time import sleep
import random
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer


# CHANGE THIS ONE
class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        word: The word displayed on screen.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        buffer : The holding spot
    """
    def init_word_list(self):
        #THis is calling the word object so it can look up the word and store it
        #Also sets it location
        for n in range(self.max_word):
            #pick a random y position, x is 0.
            self.word_list.append(Word(0,self.random_row_number()))


    def random_row_number(self):
        # rows on the screen 
        # 1 score
        # 2-19 words randomly placed
        # 20 buffer
        y = random.randint(2, 19)
        while self.rows[y] == True:
            y = random.randint(2, 19)
        self.rows[y] = True        
        return y

    def init_row_list(self):
        for n in range(self.max_rows):
            self.rows[n] = False

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.max_word = 5
        self.max_rows = 20
        self.word_list = []
        self.rows = []
        self.init_row_list()
        self.init_word_list()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def move_words(self):
        for word in self.word_list:
            #Move needs to change the location
            word.move()


    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        new_letter = self._input_service.get_letter()

        # buffer.add_letter needs to: 
        # 1. If new letter is * then clear buffer.
        # 2. otherwise add letter to end of buffer.
        self._buffer.add_letter(new_letter) 

        self.move_words()
          
    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        for x in range(self.max_word):
            # buffer.is_word returns true if word is in the buffer.
            if self._buffer.is_word(self.word_list[x]):
                self.word_list[x] = Word(0,self.random_row_number())
                self._score.add_points(3)
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actors(self.word_list)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()

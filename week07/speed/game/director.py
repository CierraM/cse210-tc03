from time import sleep
import random
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer
from game.point import Point


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
    

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
            _word-list: a list of word objects
            _input_service: an instance of InputService
            _output_service: an instance of OutputService
        """

        self._word_list = [] # A list of word objects
        self._init_word_list()
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

        print('Game Over')


    def _init_word_list(self):
        """This is calling the word object so it can look up the word and store it
        Args:
            self (Director): An instance of Director.
        """
        for n in range(constants.MAX_WORDS):
            #pick a random y position, x is 0.
            self._word_list.append(Word())

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means checking for inputs from the user, checks to see if the word has gone off screen and replaces it if it has

        Args:
            self (Director): An instance of Director.
        """
        new_letter = self._input_service.get_letter()
        

        # buffer.add_letter needs to: 
        # 1. If new letter is * then clear buffer.
        # 2. otherwise add letter to end of buffer.
        self._buffer.add_letter(new_letter) 

        # Check to see if word has gone off screen and
        for x in range(constants.MAX_WORDS):
            if self._word_list[x].get_position().get_x() > (constants.MAX_X - 10):
                self._word_list[x] = Word()
                self._score.add_points(-3)

          
    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a match between a word coming down the screen and a word in the buffer, and adding a new word to word_list if one has been deleted

        Args:
            self (Director): An instance of Director.
        """
        for x in range(constants.MAX_WORDS):
            # buffer.is_word returns true if word is in the buffer.
            if self._buffer.is_word(self._word_list[x].get_text()):
                self._score.add_points(self._word_list[x].get_points())
                self._word_list[x] = Word()
            # Use move_next inherited from Actor to move the word
            self._word_list[x].move_next()

        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means rendering new information to the screen and removing words that have been typed

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actors(self._word_list)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()
        # if self._score.get_points() < -1:
        #     self._keep_playing = False

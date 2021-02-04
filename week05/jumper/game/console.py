"""
writing puzzle, writing parachute, read letter
"""
import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """

    def read_letter(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            float: The user's input as a float.
        """
        return input(prompt)#.lower
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)

    def vertical_array (self,text_array):
        for i in text_array:
            print(i)
        """Displays the given text veriacally

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """

    def horiz_array (self,text_array):
        for i in text_array:
            print(i, end = " ")
        print()
        """Displays the given text horizontally. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """

import sys
from asciimatics.event import KeyboardEvent

# CHANGE THIS ONE

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk. Exits game is esc is hit

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_key()
        if not event is None:
            if event == -1 or event == 27: # -1 = esc key
                sys.exit()

            elif event == 13: # 10 = linefeed, 13 = charecter turn aka enter
                result = "*" # special return value to clear buffer
            elif event >= 97 and event <= 122: #lower case letter range
                result = chr(event)
        return result
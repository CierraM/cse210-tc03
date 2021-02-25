from game.action import Action

# TODO: Define the DrawActorsAction class here
class DrawActorsAction(Action):
    """An action to draw actors on the screen when called
    
    Stereotype:
        controller

    Attributes:
        output: an instance of output_service
    """
    def __init__(self, output):
        self._output = output

    def execute(self, cast):
        """Executes action on given actors by drawing them to the screen
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output.clear_screen()
        for value in cast.values():
            self._output.draw_actors(value)
        self._output.flush_buffer()


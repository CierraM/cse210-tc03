class Jumper:
    """
    A code template for the jumper. It is in charge of
    keeping track of the parachute, how much of it is left, and
    also keeping track of whether the person is still alive.

    Stereotype: Information holder
    """
    def __init__(self):
        """
        Initializes parachute
        values: parachute: an array that when printed will show a picture of a parachute
        """
        self.parachute = ["  ___", " /___\\", " \   /", "  \ /", "   0", "  /|\\", "  / \\", "", "^^^^^^^"]

    def get_parachute(self):
        """
        returns the current state of the parachute
        """
        return self.parachute

    def cut_line(self):
        """
        Cuts off the top line of the parachute
        """
        self.parachute.pop(0)

    def is_dead(self):
        """
        Checks to see how much parachute is left. If there is only the guy left, you are dead. Returns true or false. 
        Also changes the guy's head to an 'x' if he is dead.
        """
        if len(self.parachute) <= 5:
            self.parachute.pop(0)
            self.parachute.insert(0, "   x")
            return True
        else:
            return False

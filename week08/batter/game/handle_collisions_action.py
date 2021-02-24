import random
import sys
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
        check if ball collides with paddle or brick, or wall
        Do something to change ball direction
        Do something to make the brick it hit disappear
    
    Stereotype:
        Controller
    """
    def wall_bounce(self, ball, jester):
        point1 = ball.get_position()
        jester.set_text(f"y = {str(point1.get_y())}")
        if point1.get_y() == 1:
            ball.set_velocity(ball.get_velocity().reverse_y())
        if point1.get_x() == 1 or point1.get_x() == constants.MAX_X - 1:
            ball.set_velocity(ball.get_velocity().reverse_x())  
        if point1.get_y() == constants.MAX_Y - 1:
            sys.exit(0)

    def paddle_bounce(self, paddle, ball, jester):
        ball_point = ball.get_position()
        paddle_left = paddle.get_position()
        paddle_right = len(paddle.get_text())
        if ball_point.get_y() == paddle_left.get_y() - 1:
            x = ball_point.get_x()
            paddle_x = paddle_left.get_x()
            if x >= paddle_x and x <= paddle_x + paddle_right:
                ball.set_velocity(ball.get_velocity().reverse_y())



    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0]
        jester = cast["jester"][0]
        self.paddle_bounce(paddle, ball, jester)
        self.wall_bounce(ball, jester)

        # robot = cast["robot"][0] # there's only one
        # artifacts = cast["artifact"]
        # marquee.set_text("")
        # for artifact in artifacts:
        #     if robot.get_position().equals(artifact.get_position()):
        #         description = artifact.get_description()
        #         marquee.set_text(description) 
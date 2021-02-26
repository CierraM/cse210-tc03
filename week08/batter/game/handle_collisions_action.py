import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
        check if ball collides with paddle or brick, or wall
        Do something to change ball direction
        Do something to make the brick it hit disappear
    
    Stereotype:
        Controller
    """
    def __init__(self):
        """The class constructor.
        self.point: Will keep track of points earned and be used in the cast["score"]
        """
        self.point = 0

    def wall_bounce(self, ball):
        """Detects collisions between the ball and the walls of the screen. Top collision will reverse direction of ball.
        Left or Right side collision will reverse direction of the ball. Bottom collision will end the game.

        Args
            self
            ball: an instance of the ball as saved in cast["ball"]
        """
        point1 = ball.get_position()
        if point1.get_y() == 1:
            ball.set_velocity(ball.get_velocity().reverse_y())
        if point1.get_x() == 1 or point1.get_x() == constants.MAX_X - 1:
            ball.set_velocity(ball.get_velocity().reverse_x())  
        if point1.get_y() == constants.MAX_Y - 1:
            sys.exit(0)

    def paddle_bounce(self, paddle, ball):
        """Detects collisions between the ball and the paddle. If the ball hits the left or right edge of the paddle, the velocity
        will increase. If the ball hits the middle of the paddle, the velocity will recent to base speed. Once collision is detected, 
        the ball will reverse direction.

        Args
            self
            ball: an instance of the ball as saved in cast["ball"]
            paddle: an instance of paddle as saved in cast["paddle"]
        """
        ball_point = ball.get_position()
        paddle_left = paddle.get_position()
        paddle_right = len(paddle.get_text())
        ball_velocity = ball.get_velocity()
        vel_x = ball_velocity.get_x()
        vel_y = ball_velocity.get_y()
        if ball_point.get_y() == paddle_left.get_y() - 1:
            x = ball_point.get_x()
            y = ball_point.get_y()
            paddle_x = paddle_left.get_x()
            if x >= paddle_x + 4 and x <= paddle_x + paddle_right - 4:
                if vel_x == -2:
                    vel_x = -1
                elif vel_x == 2:
                    vel_x = 1
                vel_y = vel_y * -1
                ball.set_velocity(Point(vel_x, vel_y))
            elif x >= paddle_x and x <= paddle_x + paddle_right - 10:
                vel_x = vel_x * 2
                vel_y = vel_y * -1
                ball.set_velocity(Point(vel_x, vel_y))
            elif x >= paddle_x + 10 and x <= paddle_x + paddle_right:
                vel_x = vel_x * 2
                vel_y = vel_y * -1
                ball.set_velocity(Point(vel_x, vel_y))
            else:
                pass

    def brick_bounce(self, ball, bricks, score):
        """Detects collisions between the ball and the bricks at the top of the screen. If the ball collides, the velocity will be reset
        to base speed, the ball will reverse direction, the brick will be popped, and the point counter will increase.

        Args
            self
            ball: an instance of the ball as saved in cast["ball"]
            bricks: an instance of brickes as saved in cast["brick"]
            score: and instance of score as saved in cast["score"]
        """
        ball_velocity = ball.get_velocity()
        vel_x = ball_velocity.get_x()
        vel_y = ball_velocity.get_y()
        for i in range(len(bricks)):
            if ball.get_position().equals(bricks[i].get_position()):
                self.point += 1
                score.set_text(f"Score: {self.point}")
                bricks.pop(i)
                if vel_x == -2:
                    vel_x = -1
                    vel_y = vel_y * -1
                    ball.set_velocity(Point(vel_x, vel_y))
                elif vel_x == 2:
                    vel_x = 1
                    vel_y = vel_y * -1
                    ball.set_velocity(Point(vel_x, vel_y))
                else:
                    ball.set_velocity(ball.get_velocity().reverse_y())
                break

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0]
        bricks = cast["brick"]
        score = cast["score"][0]
        self.paddle_bounce(paddle, ball)
        self.wall_bounce(ball)
        self.brick_bounce(ball, bricks, score)
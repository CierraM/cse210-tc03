import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):
    """ Defines and adds all major functions to a dictionary called "cast." Creates script to be sent to director for game startup."""
    # create the cast {key: tag, value: list}
    cast = {}

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 2)
    position = Point(x, y)
    paddle = Actor()
    paddle.set_text("▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    paddle.set_position(position)
    paddle.set_velocity(Point(1, 0))
    cast["paddle"] = [paddle]

    x = int(1)
    y = int(0)
    position = Point(x, y)
    score = Actor()
    score.set_text("Score: 0")
    score.set_position(position)
    score.set_velocity(Point(0, 0))
    cast["score"] = [score]

    cast["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("◘")
            brick.set_position(position)
            cast["brick"].append(brick)

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1)
    ball = Actor()
    ball.set_text("○")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)
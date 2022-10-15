import constants

from game.casting.cast import Cast
from game.casting.score1 import Score1
from game.casting.score2 import Score2
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()
    cast.add_actor("cycles", Cycle(Point(int(constants.MAX_X/4),int(constants.MAX_Y/2))))
    cast.add_actor("cycles", Cycle(Point(int((constants.MAX_X/4)*3),int(constants.MAX_Y/2))))
    cast.add_actor("score1", Score1(Point(int(constants.MAX_X),int(constants.MAX_Y))))
    cast.add_actor("score2", Score2(Point(int(constants.MAX_X-130),int(constants.MAX_Y))))

    cycles = cast.get_actors("cycles")

    cycles[0].set_color(constants.GREEN)
    
    cycles[1].set_color(constants.RED)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
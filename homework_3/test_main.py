from space_object import Spaceship
from event_loop import EventLoop
from command import SpaceshipCommand

def test_move_spaceship():
    spaceship = Spaceship([0, 0], [1, 1])
    event_loop = EventLoop()

    event_loop.add(SpaceshipCommand(spaceship, "move"))
    event_loop.run()
    assert spaceship.position == [1,1]

def test_rotate_spaceship():
    spaceship = Spaceship([0, 0], [1, 1])
    event_loop = EventLoop()

    event_loop.add(SpaceshipCommand(spaceship, "rotate", 30))
    event_loop.run()
    assert spaceship.angle == 30


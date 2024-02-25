from space_object import Spaceship, Torpedo
from event_loop import EventLoop
from command import SpaceshipCommand

spaceship = Spaceship([0, 0], [1, 1])
torpedo = Torpedo([0, 0], [1, 1])
event_loop = EventLoop()

print(spaceship.position)
print(spaceship.angle)
event_loop.add(SpaceshipCommand(spaceship, "move"))
event_loop.add(SpaceshipCommand(spaceship, "rotate", "asd"))
event_loop.add(SpaceshipCommand(spaceship, "move"))
event_loop.add(SpaceshipCommand(spaceship, "rotate", 30))
event_loop.add(SpaceshipCommand(spaceship, "move"))
event_loop.add(SpaceshipCommand(spaceship, "stop"))
event_loop.add(SpaceshipCommand(spaceship, "move"))
event_loop.add(SpaceshipCommand(spaceship, "rotate", 320))
event_loop.run()
print(spaceship.position)
print(spaceship.angle)

from abc import ABC
import math


class Mover:
    def __init__(self, speed):
        self.speed = speed

    def move(self, position, velocity, distance):
        angle = math.atan2(velocity[1], velocity[0])
        new_position = (
            position[0] + distance * self.speed * math.cos(angle),
            position[1] + distance * self.speed * math.sin(angle),
        )

        return new_position


class Rotator:
    def __init__(self, rotation):
        self.rotation = rotation

    def rotate(self, angle):
        self.rotation = (self.rotation + angle) % 360

        return self.rotation


class FlyingObject(ABC):
    def __init__(self, position, velocity, mover, rotator):
        self.position = position
        self.velocity = velocity
        self.mover = mover
        self.rotator = rotator

    def move_forward(self, distance):
        self.position = self.mover.move(self.position, self.velocity, distance)

    def rotate(self, angle):
        self.rotation = self.rotator.rotate(angle)

    def destroy(self):
        self.status = "Destroyed"


class SpaceShip(FlyingObject):
    def fire_torpedo(self):
        torpedo = Torpedo(
            self.position,
            self.velocity,
            self.mover,
            self.rotator)
        return torpedo


class Torpedo(FlyingObject):
    pass

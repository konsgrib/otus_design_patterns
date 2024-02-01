import math


class Movable:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self):
        self.position = [
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        ]


class Rotatable:
    def __init__(self, angle=0):
        if angle < 0 or angle > 360:
            raise ValueError("Angle must be between 0 and 360 degrees")
        self.angle = angle

    def rotate(self, rotation):
        self.angle += rotation
        if self.angle > 360:
            self.angle = 0
        elif self.angle < 0:
            self.angle = 360
        return self.angle


class Spaceship(Movable, Rotatable):
    def __init__(self, position, velocity):
        Movable.__init__(self, position, velocity)
        Rotatable.__init__(self)


class Torpedo(Movable):
    def __init__(self, position, velocity):
        super().__init__(position, velocity)

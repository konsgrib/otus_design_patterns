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
    def __init__(self):
        self.angle = 0

    def rotate(self, rotation):
        new_angle = self.angle + rotation
        if new_angle > 360:
            self.angle = new_angle - 360
        elif new_angle < 0:
            self.angle = 360 + new_angle
        else:
            self.angle = new_angle
        return self.angle


class Spaceship(Movable, Rotatable):
    def __init__(self, position, velocity):
        Movable.__init__(self, position, velocity)
        Rotatable.__init__(self)


class Torpedo(Movable):
    def __init__(self, position, velocity):
        super().__init__(position, velocity)


class SpaceshipWithFuel(Spaceship):
    def __init__(self, position, velocity, fuel_level=10):
        super().__init__(position, velocity)
        self._fuel_level = fuel_level

    @property
    def fuel_level(self):
        return self._fuel_level

    def burn_fuel(self, amount):
        if self._fuel_level - amount >= 0:
            self._fuel_level -= amount
            return True
        else:
            return False

    def add_fuel(self, amount):
        self._fuel_level += amount

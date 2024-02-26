from datetime import datetime
from abc import ABC, abstractmethod
from space_object import Spaceship, SpaceshipWithFuel
from exceptions import CommandException


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SpaceshipCommand(Command):
    def __init__(self, spaceship: SpaceshipWithFuel, action: str, angle: int = None):
        self.spaceship = spaceship
        self.action = action
        self.angle = angle
        self.initial_position = self.spaceship.position
        self.initial_angle = self.spaceship.angle

    def execute(self):
        if self.action == "move":
            self.initial_position = self.spaceship.position
            self.spaceship.move()
            print("Moving forward...")
        elif self.action == "rotate":
            self.initial_angle = self.spaceship.angle
            self.spaceship.rotate(self.angle)
            print("Rotating...")
        else:
            raise ValueError("Invalid action")

    def undo(self):
        if self.action == "move":
            print("Restoring initial position...")
            self.spaceship.position = self.initial_position
        elif self.action == "rotate":
            print("Restoring initial angle...")
            self.spaceship.angle = self.initial_angle
        else:
            raise ValueError("Invalid action")


class CheckFuelComamnd(Command):
    def __init__(self, spaceship: SpaceshipWithFuel, amount_to_burn: int):
        self.spaceship = spaceship
        self.amount_to_burn = amount_to_burn

    def execute(self):
        if self.amount_to_burn > self.spaceship.fuel_level:
            raise CommandException("Not enough fuel")
        print("Fuel level:", self.spaceship.fuel_level)

    def undo(self):
        pass


class BurnFuelCommand(Command):
    def __init__(self, spaceship: SpaceshipWithFuel, amount_to_burn: int = 1):
        self.spaceship = spaceship
        self.amount_to_burn = amount_to_burn

    def execute(self):
        self.spaceship.burn_fuel(self.amount_to_burn)
        print("Burning fuel...")

    def undo(self):
        print("Restoring initial fuel level...")
        self.spaceship.add_fuel(self.amount_to_burn)


class LoggerCommand:
    def __init__(self, cmd, error):
        self.cmd = cmd
        self.error = error
        self.failed_class_name = self._get_cmd_class_name()
        self.exception_name = str(self.error.__class__.__name__)
        self.error_data = self.cmd.__dict__

    def _get_cmd_class_name(self):
        keys = list(self.cmd.__dict__.keys())
        klass_name = keys[0]
        return klass_name

    def execute(self):
        with open("log.txt", "a") as file:
            file.write(
                f"Time: {datetime.now()}, Object: {self.failed_class_name}, "
                f"Error: {self.exception_name}, Params: {self.error_data}\n"
            )


class RepeaterCommand(Command):
    def __init__(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


class DoubleRepeatedCommand(RepeaterCommand):
    pass

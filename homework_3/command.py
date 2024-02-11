from datetime import datetime
from abc import ABC, abstractmethod
from space_object import Spaceship


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SpaceshipCommand(Command):
    def __init__(self, spaceship: Spaceship, action: str, angle: int = None):
        self.spaceship = spaceship
        self.action = action
        self.angle = angle

    def execute(self):
        if self.action == "move":
            self.spaceship.move()
        elif self.action == "rotate":
            self.spaceship.rotate(self.angle)
        else:
            raise ValueError("Invalid action")


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

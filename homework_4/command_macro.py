from typing import List
from space_object import SpaceshipWithFuel
from command import Command


class MacroComamnd(Command):
    def __init__(self, spaceship: SpaceshipWithFuel, commands: List[Command]):
        self.spaceship = spaceship
        self.commands = commands

    def execute(self):
        for command in self.commands:
            try:
                command.execute()
            except Exception:
                # print("Error: ", str(e))
                self.undo()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()

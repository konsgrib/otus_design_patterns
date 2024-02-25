from space_object import SpaceshipWithFuel
from event_loop import EventLoop
from command import SpaceshipCommand, CheckFuelComamnd, BurnFuelCommand
from command_macro import MacroComamnd
import pytest
from exceptions import CommandException


@pytest.fixture()
def spaceship():
    return SpaceshipWithFuel([0, 0], [1, 1])


@pytest.fixture()
def macro(spaceship):
    move = SpaceshipCommand(spaceship, "move")
    check = CheckFuelComamnd(spaceship, 1)
    burn = BurnFuelCommand(spaceship, 1)
    macro = MacroComamnd(spaceship, [check, move, burn])
    return macro


def test_macro_initial(macro, spaceship):
    assert spaceship.position == [0, 0]
    assert spaceship.fuel_level == 10


def test_macro_last(macro, spaceship):
    for i in range(spaceship.fuel_level):
        macro.execute()
    assert spaceship.position == [10, 10]
    assert spaceship.fuel_level == 0


def test_check_no_fuel(macro, spaceship):
    for i in range(spaceship.fuel_level):
        macro.execute()
    with pytest.raises(CommandException):
        macro.execute(), "Fuel level should be negative"

    assert spaceship.position == [10, 10], "Spaceship should not move"
    assert spaceship.fuel_level == 0, "Fuel level should not be negative"


def test_burn_fuel_command(spaceship):
    burn = BurnFuelCommand(spaceship, 1)
    burn.execute()
    assert spaceship.fuel_level == 9


def test_burn_no_fuel_command(spaceship):
    burn = BurnFuelCommand(spaceship, 15)
    burn.execute()
    assert spaceship.fuel_level == 10, "Fuel level should not be negative"


def test_check_fuel_command(spaceship):
    check = CheckFuelComamnd(spaceship, 1)
    check.execute()
    assert spaceship.fuel_level == 10


def test_check_fuel_command(spaceship):
    check = CheckFuelComamnd(spaceship, 15)
    with pytest.raises(CommandException):
        check.execute()
    assert (
        spaceship.fuel_level == 10
    ), "Amount to furn shouldn't be bigger than existing fuel level"

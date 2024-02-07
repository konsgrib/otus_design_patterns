import pytest
from main import Spaceship, Torpedo


def test_spaceship_rotate():
    spaceship = Spaceship([0, 0], [1, 1])
    assert spaceship.rotate(45) == 45
    assert spaceship.rotate(40) == 85
    assert spaceship.rotate(400) == 125
    assert spaceship.rotate(40) == 165
    assert spaceship.rotate(40) == 205
    assert spaceship.rotate(-40) == 165
    assert spaceship.rotate(-40) == 125
    assert spaceship.rotate(-40) == 85


def test_spaceship_init():
    spaceship = Spaceship([0, 0], [1, 1])
    assert spaceship.position == [0, 0]
    assert spaceship.velocity == [1, 1]
    assert spaceship.angle == 0


def test_spaceship_move():
    spaceship = Spaceship([12, 5], [-7, 3])
    spaceship.move()
    assert spaceship.position == [5, 8]


def test_torpedo_init():
    torpedo = Torpedo([0, 0], [1, 1])
    assert torpedo.position == [0, 0]
    assert torpedo.velocity == [1, 1]


def test_torpedo():
    torpedo = Torpedo([0, 0], [1, 1])
    assert torpedo.position == [0, 0]
    assert torpedo.velocity == [1, 1]
    torpedo.move()
    assert torpedo.position == [1, 1]


def test_spaceship_failed_to_move_nonreadable_position():
    spaceship = Spaceship([], [1, 1])
    with pytest.raises(IndexError):
        spaceship.move()


def test_spaceship_failed_to_move_nonreadable_velocity():
    spaceship = Spaceship([1, 1], [])
    with pytest.raises(IndexError):
        spaceship.move()

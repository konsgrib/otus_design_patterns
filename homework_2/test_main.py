import pytest
from spaceship import Movable, Rotatable, Spaceship, Torpedo

def test_movable_move():
    movable = Movable([0, 0], [1, 1])
    movable.move()
    assert movable.position == [1, 1]

def test_rotatable_rotate():
    rotatable = Rotatable()
    assert rotatable.rotate(45) == 45
    assert rotatable.rotate(400) == 40

def test_spaceship_init():
    spaceship = Spaceship([0, 0], [1, 1])
    assert spaceship.position == [0, 0]
    assert spaceship.velocity == [1, 1]
    assert spaceship.angle == 0

def test_torpedo_init():
    torpedo = Torpedo([0, 0], [1, 1])
    assert torpedo.position == [0, 0]
    assert torpedo.velocity == [1, 1]

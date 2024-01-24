import pytest
import math
from main import Mover, Rotator, FlyingObject, SpaceShip, Torpedo


def test_mover():
    mover = Mover(1)

    assert mover.move((0, 0), (1, 0), 1) == (1, 0)


def test_rotator():
    rotator = Rotator(0)

    assert rotator.rotate(90) == 90


def test_flying_object():
    mover = Mover(1)
    rotator = Rotator(0)
    flying_object = FlyingObject((0, 0), (1, 0), mover, rotator)
    flying_object.move_forward(1)
    assert flying_object.position == (1, 0)
    flying_object.rotate(90)
    assert flying_object.rotation == 90
    flying_object.destroy()
    assert flying_object.status == "Destroyed"


def test_spaceship():
    mover = Mover(1)
    rotator = Rotator(0)
    spaceship = SpaceShip((0, 0), (1, 0), mover, rotator)
    torpedo = spaceship.fire_torpedo()
    assert isinstance(torpedo, Torpedo)


def test_torpedo():
    mover = Mover(1)
    rotator = Rotator(0)
    torpedo = Torpedo((0, 0), (1, 0), mover, rotator)
    assert isinstance(torpedo, Torpedo)


def test_mover_move():
    mover = Mover(1)
    position = (12, 5)
    velocity = (-7, 3)
    distance = 1
    angle = math.atan2(velocity[1], velocity[0])
    expected_new_position = (
        position[0] + distance * mover.speed * math.cos(angle),
        position[1] + distance * mover.speed * math.sin(angle),
    )
    actual_new_position = mover.move(position, velocity, distance)

    assert actual_new_position == expected_new_position


def test_mover_move_no_position():
    mover = Mover(1)

    class ObjectWithoutPosition:
        velocity = (-7, 3)

    obj = ObjectWithoutPosition()
    with pytest.raises(AttributeError):
        mover.move(obj.position, obj.velocity, 1)


def test_mover_move_no_velocity():
    mover = Mover(1)

    class ObjectWithoutVelocity:
        position = (12, 5)

    obj = ObjectWithoutVelocity()

    with pytest.raises(AttributeError):
        mover.move(obj.position, obj.velocity, 1)


def test_mover_move_no_position_setter():
    mover = Mover(1)

    class ObjectWithoutPositionSetter:
        position = (12, 5)
        velocity = (-7, 3)

        @property
        def position(self):
            return self._position

    obj = ObjectWithoutPositionSetter()

    with pytest.raises(AttributeError):
        mover.move(obj.position, obj.velocity, 1)

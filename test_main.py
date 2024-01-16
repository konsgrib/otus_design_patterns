import pytest
from math import isclose
from main import Solver


def test_solve_positive_discriminant():
    result = Solver.solve(1, -3, 2)
    assert isclose(result[0], 2.0, rel_tol=1e-5), "Root is close to 2.0"
    assert isclose(result[1], 1.0, rel_tol=1e-5), "Root is close to 1.0"


def test_solve_zero_discriminant():
    result = Solver.solve(1, -2, 1)
    # assert len(result) == 2, "Two roots are expected"
    assert isclose(result[0], 1.0, rel_tol=1e-5), "Root is close to 1.0"


def test_solve_negative_discriminant():
    result = Solver.solve(1, 1, 1)
    assert result == [], "No roots are expected if discriminant is less than 0"


def test_solve_one():
    result = Solver.solve(1, 0, 1)
    assert result == [], "No roots are expected if discriminant is less than 0"


def test_solve_two():
    result = Solver.solve(1, 0, -1)
    assert len(result) == 2, "Two roots are expected"
    assert isclose(result[0], 1.0, rel_tol=1e-5), "Root ins close to 1.0"
    assert isclose(result[1], -1.0, rel_tol=1e-5), "Root is close to 1.0"


def test_solve_three():
    result = Solver.solve(1, 2, 1)
    assert len(result) == 1, "One root is expected"
    assert isclose(result[0], -1.0, rel_tol=1e-5), "Root ins close to 1.0"


def test_solve_a_four():
    with pytest.raises(ZeroDivisionError):
        Solver.solve(0, -2, 1)

def test_solve_is_numeric():
    with pytest.raises(TypeError):
        Solver.solve("q",1,2)

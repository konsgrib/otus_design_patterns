import pytest
from math import isclose
from main import Solver


def test_solve_positive_discriminant():
    result = Solver.solve(1, -3, 2)
    assert isclose(result[0], 2.0, rel_tol=1e-5), "Root is close to 2.0"
    assert isclose(result[1], 1.0, rel_tol=1e-5), "Root is close to 1.0"


def test_solve_zero_discriminant():
    result = Solver.solve(1, -2, 1)
    assert isclose(result[0], 1.0, rel_tol=1e-5), "Root is close to 1.0"


def test_solve_negative_discriminant():
    result = Solver.solve(1, 1, 1)
    assert result == [], "No roots are expected if discriminant is less than 0"


def test_solve_one():
    "Написать тест, который проверяет, что для уравнения x^2+1 = 0 корней нет (возвращается пустой массив)"
    result = Solver.solve(1, 0, 1)
    assert result == [], "No roots are expected if discriminant is less than 0"


def test_solve_two():
    "Написать тест, который проверяет, что для уравнения x^2-1 = 0 есть два корня кратности 1 (x1=1, x2=-1)"
    result = Solver.solve(1, 0, -1)
    assert len(result) == 2, "Two roots are expected"
    assert isclose(result[0], 1.0, rel_tol=1e-5), "Root ins close to 1.0"
    assert isclose(result[1], -1.0, rel_tol=1e-5), "Root is close to 1.0"


def test_solve_three():
    "Написать тест, который проверяет, что для уравнения x^2+2x+1 = 0 есть один корень кратности 2 (x1= x2 = -1)."
    result = Solver.solve(1, 2, 1)
    assert len(result) == 1, "One root is expected"
    assert isclose(result[0], -1.0, rel_tol=1e-5), "Root ins close to 1.0"


def test_solve_a_four_a_equal_to_zero():
    "Написать тест, который проверяет, что коэффициент a не может быть равен 0. В этом случае solve выбрасывает исключение."
    with pytest.raises(ZeroDivisionError):
        Solver.solve(0, -2, 1)
        

def test_solve_a_four_a_less_than_epsilon():
    "Тест, который проверяет, что коэффициент a может быть больше 0 но меньше машинного эпсилона. В этом случае solve выбрасывает исключение."
    with pytest.raises(ZeroDivisionError):
        Solver.solve(2.220446049250313e-17, -2, 1)
        
        
def test_solve_a_four3_a_bigeer_than_epsilon():
    """Написать тест, который проверяет, что коэффициент a может быть близок к 0 но больше машинного эпсилона. 
    В этом случае solve не выбрасывает исключение т.к. при положительном дискриминанте имеем два корня."""
    result = Solver.solve(2.220446049250313e-14, -2, 1)
    assert len(result) == 2, "Two roots are expected"


def test_solve_is_numeric():
    with pytest.raises(TypeError):
        Solver.solve("q",1,2)

def test_solve_is_numeric_nan():
    with pytest.raises(ValueError):
        Solver.solve(1,float("NaN"),1)
        Solver.solve(1,2,float("NaN"))
        Solver.solve(float("NaN"),1,2)

def test_solve_is_numeric_inf():
    with pytest.raises(ValueError):
        Solver.solve(1,float("inf"),1)
        Solver.solve(1,2,float("inf"))
        Solver.solve(float("inf"),1,2)
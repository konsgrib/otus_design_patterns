from typing import List
from math import sqrt, isclose, isnan, isinf

class Solver:
    def __init__(self):
        self.machine_epsilon = self._get_machine_epsilon()

    def _get_machine_epsilon(self):
        machine_epsilon = 1.0
        while 1.0 + machine_epsilon != 1.0:
            machine_epsilon /= 2.0
        return machine_epsilon * 2.0

    def _not_acceptable_numeric(self, a, b, c):
        if isnan(a) or isnan(b) or isnan(c):
            return True
        if isinf(a) or isinf(b) or isinf(c):
            return True
        return False

    def solve(self, a: float, b: float, c: float) -> List[float]:
        if 0 < self.machine_epsilon > a:
            raise ZeroDivisionError("Value is less than machine epsilon")
        if self._not_acceptable_numeric(a, b, c):
            raise ValueError("Incorrect value")
        d = (b * b) - (4 * a * c)
        if d < 0:
            return []
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        if isclose(x1, x2, rel_tol=1e-5):
            return [x1]
        return [x1, x2]
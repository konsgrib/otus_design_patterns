

Homework #1

Class Solver and its methods description:

_get_machine_epsilon:
        Private method to calculate the machine epsilon, which is the smallest
        floating-point number that when added to 1.0 gives a result different
        from 1.0.

_not_acceptable_numeric:
        Private method to check if any of the coefficients a, b, or c is NaN
        (Not a Number) or infinite.


solve:
        Static method to solve the quadratic equation ax^2 + bx + c = 0.
        Args:
            a (float): Coefficient of x^2.
            b (float): Coefficient of x.
            c (float): Constant term.
        Returns:
            List[float]: List of solutions to the equation. If the equation has
            no real solutions, an empty list is returned.
        Raises:
            ZeroDivisionError: If the coefficient 'a' is less than the machine
            epsilon (smallest floating-point number).
            ValueError: If any of the coefficients a, b, or c is NaN or infinite.



Tests description:
    test_solve_positive_discriminant:

    test_solve_zero_discriminant:

    test_solve_negative_discriminant:

    test_solve_one:

    test_solve_two:

    def test_solve_three:

    test_solve_a_four_a_equal_to_zero:

    test_solve_a_four_a_less_than_epsilon:

    test_solve_a_four3_a_bigeer_than_epsilon:

    test_solve_is_numeric:

    test_solve_is_numeric_nan:

    test_solve_is_numeric_inf:


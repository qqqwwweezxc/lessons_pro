def factorial(number: int) -> int:
    """Function calculates the factorial of a number"""
    if number < 0:
        raise ValueError("Factorial is defined only for non-negative numbers")
    result: int = 1
    for i in range(1, number + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    """Function finds the greatest common divisor (GCD) of two numbers—the largest number that divides both."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def is_even(n: int) -> bool:
    """
    Перевіряє, чи є число парним.
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return n % 2 == 0

def factorial(n: int) -> int:
    """
    Обчислює факторіал числа n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    >>> factorial(10)
    3628800
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


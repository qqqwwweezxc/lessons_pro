import pytest

def divide(a: int, b: int) -> float:
    """Divides two numbers."""
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    return a / b

def test_divide_correct():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-8, 2) == -4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (5, 2, 2.5),
        (-6, 3, -2),
        (7, -1, -7),
    ],
)
def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected
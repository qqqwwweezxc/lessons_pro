# Write a function calculate_circle_area(radius) that:

#     Takes the radius of a circle.
#     Returns the area of ​​a circle.
#     Use this function in a program that asks the user for a radius and prints out the area.

import math


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    param radius: Radius of the circle.
    return: Area of the circle.
    """
    return math.pi * radius**2


# Create a Rectangle class that represents a rectangle.

# Class requirements:

#     Class attributes:
#     width — the width of the rectangle.
#     height — the height of the rectangle.
#     Class methods:
#     __init__(self, width, height) — a constructor that accepts the width and height of the rectangle.
#     area(self) — a method that returns the area of ​​the rectangle.
#     perimeter(self) — a method that returns the perimeter of the rectangle.
#     is_square(self) — a method that returns True if the rectangle is a square (the width is equal to the height), otherwise False.
#     resize(self, new_width, new_height) — a method that changes the width and height of the rectangle.

# Create an object of the Rectangle class and test all the methods.


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle instance.

        param width: Width of the rectangle.
        param height: Height of the rectangle.
        """
        self.width = width
        self.height = height

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        return: Area of the rectangle.
        """
        return self.height * self.width

    def get_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        return: Perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Check if the rectangle is a square.

        return: True if width equals height, otherwise False.
        """
        return self.width == self.height

    def resize(self, new_width: float, new_height: float) -> None:
        """
        Resize the rectangle.

        param new_width: New width of the rectangle.
        param new_height: New height of the rectangle.
        """
        self.width = new_width
        self.height = new_height

    def __str__(self) -> str:
        """
        Return a string representation of the rectangle.
        """
        return f"Rectangle (width={self.width}, height={self.height}, area={self.get_area()})"


# Testing
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 3)

assert r1.get_area() == 8, "Test 1"
assert r2.get_area() == 9, "Test 2"

assert r1.get_perimeter() == 12, "Test 3"
assert r2.get_perimeter() == 12, "Test 4"

assert r1.is_square() == False, "Test 5"
assert r2.is_square() == True, "Test 6"

r1.resize(5, 5)
assert r1.get_area() == 25, "Test 7"
assert r1.is_square() == True, "Test 8"

print("OK")

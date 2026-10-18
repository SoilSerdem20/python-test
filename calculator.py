"""
calculator.py - A simple calculator module.

This file defines four basic math functions (add, subtract, multiply, divide).
It is a small example project used to show how Python code and its tests are
organised in a GitHub repository. The matching tests live in test_calculator.py.

Run it directly to see a quick demo:
    python calculator.py
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the result of a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises ValueError if b is zero, because dividing by zero is undefined.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# This block only runs when the file is executed directly (not when imported).
if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", subtract(7, 4))
    print("5 x 6 =", multiply(5, 6))
    print("10 / 4 =", divide(10, 4))

# shapes.py

"""A collection of functions for printing basic shapes.
"""

CHAR = '*'
SPACE = ' '

def rectangle(height, width):
    """Prints a rectangle. """
    for row in range(height):
        for col in range(width):
            print(CHAR + SPACE, end='')
        print()

def square(side):
    """Print a square."""
    rectangle(side, side)

def triangle(height):
    """Print a right triangle."""
    for row in range(height):
        for col in range(1, row + 2):
            print(CHAR + SPACE, end='')
        print()


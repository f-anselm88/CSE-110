"""
Author: Anselm Munango

Purpose: Use functions to calculate areas.
"""

import math

def compute_area_square(side):
    """Purpose: Compute the area of a square."""
    area = side * side
    return area

def compute_area_rectangle(length, width):
    """Purpose: Compute the area of a rectangle."""
    area = length * width
    return area

def compute_area_circle(radius):
    """Purpose: Compute the area of a circle."""
    area = math.pi * radius * radius
    return area

# The main program starts here.
shape = ""

while shape != "quit":
    shape = input("What shape do you have? (square, rectangle, circle, or quit to exit): ")

# Convert the shape to lowercase to make it case-insensitive.
    shape = shape.lower()

    if shape == "square":
        side = float(input("What is the length of the side of the square: "))
        area = compute_area_square(side)
        print(f"The area of the square is: {area:.2f}")

    elif shape == "rectangle":
        length = float(input("What is the length of the rectangle: "))
        width = float(input("What is the width of the rectangle: "))
        area = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is: {area:.2f}")

    elif shape == "circle":
        radius = float(input("What is the radius of the circle: "))
        area = compute_area_circle(radius)
        print(f"The area of the circle is: {area:.2f}")

    elif shape != "quit":
        print("Invalid shape. Please enter square, rectangle, circle, or quit.")
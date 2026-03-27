"""
Title: Area of Shapes
Author: Anselm Munango

Description: This program will take inputs from the user and provide the area of the shapes 
of a rectangle, a square, and a circle.
"""
#STEP ONE: IMPORT ANY LIBRARIES
import math

#STEP TWO: Get inputs from the user

squade_side = float(input("What is the length of the side of your square in centimeters? "))
rectangle_length = float(input("What is the length of your rectangle in centimeters? "))
rectangle_width = float(input("What is the width of your rectangle in centimeters? "))
radius = float(input("What is the radius of your circle in centimeters? "))
#STEP THREE: Use inputs to get the area

#Square - side squared
area_square = squade_side ** 2

#Rectangle - length times width
area_rectangle = rectangle_length * rectangle_width

#Circle - pi r squared
area_circle = math.pi * (radius ** 2)

#STEP FOUR: Print the results
print(f"The area of your square is {area_square} cm^2")
print(f"The area of your rectangle is {area_rectangle} cm^2")
print(f"The area of your circle is {area_circle:.2f} cm^2")

#Enhacement: The answer in meters
print()
print(f"The area of your square is {area_square/10000} m^2")
print(f"The area of your rectangle is {area_rectangle/10000} m^2")
print(f"The area of your circle is {area_circle/10000:.2f} m^2")

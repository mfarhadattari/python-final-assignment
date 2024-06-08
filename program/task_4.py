# Write a python program to find the area of circle and area of rectangle using function.

import math

def area_of_circle(radius):
    try:
        radius = float(radius)
        return math.pi * radius * radius
    except ValueError:
        return "Invalid input. Please enter a numeric value for radius."

# Example usage
radius = input("Radius= ")
print(area_of_circle(radius))

def area_of_rectangle(length, width):
    try:
        length, width = float(length), float(width)
        return length * width
    except ValueError:
        return "Invalid input. Please enter numeric values for length and width."

# Example usage
length, width = input("length= ") , input("Width= ")
print(area_of_rectangle(length, width))
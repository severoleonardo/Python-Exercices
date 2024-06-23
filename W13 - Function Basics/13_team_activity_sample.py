"""
File: 13_team_activity_sample.py
Author: Leonardo Severo

Purpose: Write functions to compute and return the areas of squares, rectangles, and circles.
"""
import math

def compute_area_square(side):
    return side * side
    
def compute_area_rectangle(lenght, width):
    return lenght * width

def compute_area_circle(radius):
    return math.pi * radius * radius

# The main program starts here...
shape = ""

while shape != "quit":
    shape = input("What the shape do you have? ")

    # Convert it to lower case once, so we don't have to keep converting it
    shape = shape.lower()

    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area_square(side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area - compute_area_rectangle(length, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area}")
        


   


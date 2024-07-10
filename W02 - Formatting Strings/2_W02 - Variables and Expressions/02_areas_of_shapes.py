"""
Title: 02 Team Activity: Areas of Shapes
Author: Leonardo Severo

Purpose: Write a program to compute the areas of three different shapes
"""

#Square 

square_side = float(input('What is the length of a side of the square? '))
area = square_side **2
print(f"The area of the square is: {area}")

#Rectangle

rectangle_length_side = float(input('What is the length of the rectangle? '))
rectangle_width_side = float(input('What is the width of the rectangle? '))
area = rectangle_length_side * rectangle_width_side
print(f"The area of the rectangle is: {area} ")

#Circle

radius_circle = float(input('What is the radius of the circle? '))
area = 3.14 * (radius_circle ** 2)
print(f"The area of the circle is: {area} ")


# Stretch 1: import math

import math
radius = float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area}")


# Stretch 2: Many areas shapes from a unique value
import math
value = float(input('Please insert a value: '))

# Calculate

area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)

# Display results

print(f"Area of the square: {area_square}")
print(f"Area of the circle: {area_circle}")
print(f"Volume of the cube: {volume_cube}")
print(f"Volume of the sphere: {volume_sphere}")


#Stretch 3: centimeters to meters conversion

# Area of the square
side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2

print(f"The area of the square is: {area} cm^2")
print(f"The area of the square is: {area / 10000} m^2")

# Area of the rectangle

length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width

print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")	

# Area of tje circle
radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")
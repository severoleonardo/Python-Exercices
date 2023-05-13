"""
Title: 04 Prepare: Checkpoint - Unit Conversion
Author: Leonardo Severo

Purpose: Write a program to convert from Fahrenheit to Celsius. 
"""

#Prompt
fahrenheit = float(input("What is the temperature in Fahrenheit? "))

#Calculate
celsius = (fahrenheit - 32) * 5/9

#Display
print(f"The temperature in Celsius is {celsius:.1f} degrees.")






#Sample solution
"""
degrees_f = float(input("What is the temperature in Fahrenheit? "))
degrees_c = (degrees_f - 32) * 5 / 9

print(f"The temperature in Celsius is {degrees_c:.1f} degrees.")
"""
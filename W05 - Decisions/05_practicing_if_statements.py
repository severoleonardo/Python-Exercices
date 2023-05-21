"""
Title: 05 Prepare - Practicing If Statements
Author: Leonardo Severo

Purpose: Practicing If Statements
"""

first_number = int(input("Please, insert the first number: "))
second_number = int(input("Please, insert the second number: "))


if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")


if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")


if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater"),

print()

favorite_animal = input("What is your favorite animal? ")

if favorite_animal.lower() == "dog":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite animal.")


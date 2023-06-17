"""
File: 07_checkpoint
Author: Leonardo Severo

Purpose: Practice while loops.
"""

# Continue asking as long as the number is negative, then display the number.
number = int(input("Please type a positive number: "))


while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")

answer = ""

while answer != "yes":
    answer = input("May I have a piece of candy? ")

print("Thank you.")
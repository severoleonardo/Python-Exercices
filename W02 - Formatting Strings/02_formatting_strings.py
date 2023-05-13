"""
File: check02_assignment.py
Author: Leonardo Severo

Purpose: Display text to the screen.
"""


#variables
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

#display message
output = 'Your name is {1}, {0} {1}.'.format(first_name, last_name)
print(output)





# Be aware that there are many ways to do the formatting of that line, such as:
# print("Your name is " + last + ", " + first + " " + last + ".")
# print("Your name is {}, {} {}.".format(last, first, last))
# print("Your name is {0}, {1} {0}.".format(last, first))
"""
File: 08_sample_iterating_through_strings.py
Author: Leonardo Severo

Purpose: practice looping through letters in a word and comparing a letter to another letter to determine what should be printed.
"""

# print("This is line one.", end=" ")
# print("This is line two.")


word = "Commitment"

letter_typed = input("What is your favorite letter? ")

###
# Core Requirements #1 and #2
###
for letter in word:
    # Just in case the word or the user's letter contain a capital, we
    # should convert the letters to lowercase when we compare them
    if letter.lower() == letter_typed.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

###
# Core Requirement #3
###
for letter in word:
    if letter.lower() == letter_typed.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()

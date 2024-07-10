"""
File: 04 Project Milestone - Word Puzzle
Author: Leonardo Severo

Purpose: create a puzzle game that follows a Wordle pattern part 1.

Milestone Requirements
By the middle of the week, to help make sure you are on track to finish the assignment, you need to complete the following:

1. Have a secret word stored in the program.
2. Prompt the user for a guess.
3. Continue looping as long as that guess is not correct.
4. Calculate the number of guesses and display it at the end.
"""

import random

word_list = ["apple", "banana", "orange", "grape", "lemon"]
secret_word = random.choice(word_list)
word_length = len(secret_word)
attempts = 0

print("Welcome to the word guessing game!")

while True:
    guess = input("What is your guess? ").lower()

    if len(guess) != word_length:
        print(f"Your guess must be {word_length} letters long.")
        continue

    attempts += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {attempts} guesses.")
        break
    else:
        print("Your guess was not correct.")

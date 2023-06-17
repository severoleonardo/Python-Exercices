"""
File: 07_Milestone
Author: Leonardo Severo

Purpose: create a puzzle game that follows a Wordle pattern part 1.
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
        print("Your guess was not correct")
        continue

    attempts += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {attempts} guesses.")
        break

    if attempts == 1:
        print("Your guess was not correct")
    elif attempts == 2:
        print("Your guess was not correct")
    else:
        print("Your guess was not correct")
    
    if attempts >= 3:
        print(f"The word was: {secret_word}")
        print(f"It took you {attempts} guesses.")
        break


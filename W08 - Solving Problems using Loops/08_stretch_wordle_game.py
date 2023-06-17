"""
File: 08_stretch_wordle_game.py
Author: Leonardo Severo

Purpose: Guess my number game - Final Requirements.
"""

import random

word_list = ["apple", "banana", "orange", "grape", "lemon"]
secret_word = random.choice(word_list)
word_length = len(secret_word)
max_attempts = 5
attempts = 0
guessed_letters = set()

print("Welcome to the word guessing game!")
print()
hint = ""
for _ in range(word_length):
    hint += "_ "


print(f"Your hint is: {hint}")
print("You have 5 attempts to guess the word")

while attempts < max_attempts:
    guess = input("What is your guess? ").lower()

    if len(guess) != word_length:
        print("Invalid guess. Please enter a word with the correct length.")
        continue

    attempts += 1

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {attempts} guesses.")
        break

    hint = ""
    for i in range(word_length):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += "_"

    guessed_letters.add(guess)
    print(f"Your hint is: {hint}\n")

if attempts >= max_attempts:
    print("Game over! You ran out of attempts.")
    print(f"The word was: {secret_word}")
    print(f"It took you {attempts} guesses.")
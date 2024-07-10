"""
File: 04 Project - Word Puzzle
Author: Leonardo Severo

Final Requirements
In addition to the Milestone requirements, your final program must:

1. Use a loop to generate the initial hint.
2. Add a check to verify that the length of the guess is the same as the length of the secret word. If it is not, display a message. If they are the same, then proceed to give the hint.
3. Add the hints according to the rules above.
4. Make sure to account for the following in your hints:
  . Letters that are not present at all in the secret word (underscore _).
  . Letters that are present in the secret word, but in a different spot (lowercase).
  . Letters that are present in the secret word at that exact spot spot (uppercase).

Added Features: The game now includes a history of previous guesses and their respective hints, providing players with more context for their future guesses.
"""
import random

word_list = ["apple", "banana", "orange", "grape", "lemon"]
secret_word = random.choice(word_list)
word_length = len(secret_word)
max_attempts = 5
attempts = 0
guess_history = []

print("Welcome to the word guessing game!\n")

hint = "_ " * word_length
print(f"Your hint is: {hint}")
print(f"You have {max_attempts} attempts to guess the word\n")

while attempts < max_attempts:
    guess = input("What is your guess? ").lower()

    if len(guess) != word_length:
         print(f"Invalid guess. Please enter a word with {word_length} letters.\n")
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


    guess_history.append((guess, hint))
    print(f"Your hint is: {hint}")
    print("Guess history:")
    for g, h in guess_history:
        print(f"Guess: {g}, Hint: {h}")

    print(f"You have {max_attempts - attempts} attempts remaining.\n")

if attempts >= max_attempts and guess != secret_word:
    print("Game over! You ran out of attempts.")
    print(f"The word was: {secret_word}")
    print(f"It took you {attempts} guesses.")
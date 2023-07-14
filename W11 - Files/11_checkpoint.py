"""
File: check11_sample.txt
Author: Leonardo severo

Purpose: Demonstrate the basics of reading from a text file in Python.
"""

# Open the file.
# The "with" syntax makes it so I don't have to worry about closing it later

with open("books.txt") as book_file:

    # Go through each line in the file, one by one
    for line in book_file:
        # The .strip() function returns a new line that doesn't have leading or trailing whitespace. In other words, it strips off the "\n" that would otherwise be at the end of the line.
        book = line.strip()

        # Print the book out to the screen
        print(book)
"""
File: 09_sample_lists_of_numbers.py
Author: Leonardo Severo

Purpose: Practice using numbers in lists.
"""

numbers = []
number = -1 #None

print("Enter a list of numbers, type 0 when fineshed.")
while number != 0:
    number = int(input("Enter number: "))
    
    # Without this if statement, I would put "end" into my list as well
    if number != 0:
       numbers.append(number)

print()

for number in numbers:
    print(number)
print()

# Compute the sum
total = sum(numbers)
print(f"The sum is: {total}")

# Compute the average
average = total / len(numbers)
print(f"The average is: {average}")

# Find the maximum number
maximum = max(numbers)
print(f"The largest number is: {maximum}")
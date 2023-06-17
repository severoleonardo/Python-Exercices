"""
File: 09_stretch_lists_of_numbers.py
Author: Leonardo Severo

Purpose: Stretch Challenge 1: Find the smallest positive number:
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

# Compute the sum
total = sum(numbers)
print(f"The sum is: {total}")

# Compute the average
average = total / len(numbers)
print(f"The average is: {average}")

# Find the maximum number
maximum = max(numbers)
print(f"The largest number is: {maximum}")

# Find the smallest positive number 
smallest_positive = None
for number in numbers:
    if number > 0:
        if smallest_positive is None or number < smallest_positive:
            smallest_positive = number
print(f"The smallest positive number is: {smallest_positive}")

# Sorting the list
sorted_list = sorted(numbers)
print("The sorted list is:")
for number in sorted_list:
    print(number)

print()
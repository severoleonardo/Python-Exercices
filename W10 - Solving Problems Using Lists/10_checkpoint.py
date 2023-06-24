"""
File: 10_checkpoint.py
Author: Leonardo Severo

Purpose: Practice working with list indexes.
"""

# First prepare the list, just like the previous checkpoint
print("Enter the items of the shopping list (type: 'quit' to finish): ")

shopping_list = []
item = None


while item != "quit":
    item = input("Item: ")
    
    # Without this if statement, I would put "end" into my list as well
    if item != "quit":
       shopping_list.append(item)

# We now have the list. Print it out to verify:
print("\nThe shopping list is: ")
for item in shopping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

    # I could have just put shopping_list[i] directly in my print statement
    # rather than creating a separate variable if I wanted. I decided to do it
    # this way to make it easier to read.

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

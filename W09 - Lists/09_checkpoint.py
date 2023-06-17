"""
File: 09_checkpoint.py
Author: Leonardo Severo

Purpose: Practice using lists, by adding the names of friends.
"""

friends = []

new_friend = None #None

while new_friend != "end":
    new_friend = input("Type the name of a friend: ")
    
    # Without this if statement, I would put "end" into my list as well
    if new_friend != "end":
        friends.append(new_friend)

print()
print("Your friends are: ")

for friend in friends:
    print(friend)
print()
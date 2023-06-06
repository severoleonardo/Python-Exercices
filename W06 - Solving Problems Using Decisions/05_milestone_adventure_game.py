"""
Title: 05 Milestone - Adventure Game
Author: Leonardo Severo

Purpose: Create your own text-based adventure game with at least three levels of choices. It's up to you to determine the scenarios, the choices, and the consequences.
"""


### Print a welcome message
# Presentation of the scenario and prompt for the user to make the 1# choice

print("\nWelcome to The Investigator!")
print("\nYou are a young rookie investigator and your first mission involves solving a wild animal trafficking investigation case. The alleged crime scene is close to a village in the Amazon jungle.")
print("Go there and see what you discover about the criminals' plans. Our goal is to arrest the gang and return the animals to the local authorities responsible for protecting the forest.")

### Prompt user for a choice
items_choice = input("\nYou are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")

#Convert items to uppercase
items = items_choice.upper()

# First plot
if items == "MATCH":
    print(f"\nYou pick up the MATCH and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want  to RUN, or HIDE behind a tree?")

    items_choice = input ("> ")


elif items == "FLASHLIGHT":
    print(f"\nYou pick up the FLASHLIGHT and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
else:
    print("\nThis option is currently not available. Choose from the items that are appearing on the screen")


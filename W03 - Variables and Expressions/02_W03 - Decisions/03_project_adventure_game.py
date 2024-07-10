"""
Title: 03 Project - Adventure Game
Author: Leonardo Severo

Purpose: Create your own text-based adventure game with at least three levels of choices. It's up to you to determine the scenarios, the choices, and the consequences.
"""

'''
Criteria:

# Three levels of scenarios
# More than two choices
# Choice in CAPS
# Choices not case sensitive
# Choices lead to different scenarios
# Choice match questions
# Incorret Input
# Shows creativity and exceeds requirements
# Extra Credit: The program was shown and explained to two other people
'''


# Presentation of the plot and prompt for the user to make decisions
print("\nWelcome to The Investigator.")
print("\nYou are a young rookie investigator and your first mission involves solving a wild animal trafficking investigation case. The alleged crime scene is close to a village in the Amazon jungle.")
print("Go there and see what you discover about the criminals' plans. Our goal is to arrest the gang and return the animals to the local authorities responsible for protecting the forest.")


# First level of scenario
items = input("\nYou are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")

#Turn off sensitive case: The Forest
items = items.lower()


if items == "match":
    print(f"\nYou pick up the MATCH and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.")
    action = input("\nDo you want to RUN, or HIDE behind a tree? ")
    #Turn off sensitive case
    action = action.lower()
    if action == "run":
       print("\nYou sprint away from the bear, narrowly escaping its reach.")
    elif action == "hide":
        print("\nYou quickly hide behind a tree, hoping the bear doesn't spot you.")
    else:
        #Incorret input
        print("\nThis option is currently not available. Choose from the items that are appearing on the screen")
elif items == "flashlight":
    print(f"\nYou pick up the FLASHLIGHT and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
    action = input("\nDo you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
    if action == "folllow":
        print("\nYou decide to follow the path, eager to uncover the souce of the noise")
    elif action == "look":
        print("\nYou shine the flashlight towards the trees, searching for the thing that made the noise.")
    else:
        #Incorret input
        print("\nThis option is currently not available. Choose from the items that are appearing on the screen")
else:
    #Incorret input
    print("\nThis option is currently not available. Choose from the items that are appearing on the screen")

## Second level of scenario: The Cave
print("\nFurther ahead you come across a hidden cave entrance. It's damp and ominous.")
choice = input("\nDo you want to ENTER the cave or CONTINUE on your current path? ")
 #Turn off sensitive case
choice = choice.lower()

#Three choices
if choice == "enter":
        print("\nYou gather your courage and step into the cave, the darkness swallowing you.")
        explore = input("Do you want to LIGHT a torch or RETURN to the forest? ")
         #Turn off sensitive case
        explore = explore.lower()
        if explore == "light":
            print("\nYou search your bag and find a torch. With the torch lit, you cautiously enter the cave.")
        elif explore == "return":
             print("\nYou decide to return to the forest, leaving tge nysterious cave behind.")
        else:
          #Incorret input
          print("\nThis option is currently not available. Choose from the items that are appearing on the screen")        
elif choice == "continue":
        print("\nYou decide to continue on your current path, leaving the mysterious cave behind.")
        search = input("You keep looking for traces that will lead you to you goal. Do you prefer looking for clues on the GROUND, in the TREES or in the SKY? ")
         #Turn off sensitive case
        search = search.lower()
        if search == "ground":
            print("\nYou found tire marks in the clay that could be from the criminals.")
        elif search == "trees":
            print("You discovered a pattern of marks carved into the trees that indicate a direction.")
        elif search == "sky":
            print("\nYou look over the treetops and see smoke.")
        else:
            #Incorret input
            print("\nThis option is currently not available. Choose from the items that are appearing on the screen")
else:
    #Incorret input
    print("\nThis option is currently not available. Choose from the items that are appearing on the screen")

### Third level of scenario
print("\nAs a result of your search, you managed to find the criminal's hideout.")
outcome = input("\nYou have an important decision to make: do call for reinforcement and WAIT for you team to arrive, or do you FIGTH the group of criminals alone? ")
 #Turn off sensitive case
outcome = outcome.lower()
if outcome == "wait":
    print("\nThe reinforcement was already on alert and it didn't take long to surround the group of criminals.")
elif outcome == "fight":
    print("\nYou approach to apprehend the criminals, but soon realize you've been surrounded by the group and just walked into an ambush.")
else:
    #Incorret input
    print("\nThis option is currently not available. Choose from the items that are appearing on the screen")

print("\nCongratulations! You have completed the adventure game.")



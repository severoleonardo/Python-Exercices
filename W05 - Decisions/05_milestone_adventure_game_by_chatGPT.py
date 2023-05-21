import time

# Function to handle invalid choices
def handle_invalid_choice():
    print("Invalid choice. Please select a valid option.")

# Function for the first level scenario
def level_one_scenario():
    print("\nLevel One: The Mysterious Cave")
    print("You find yourself standing at the entrance of a dark cave.")
    print("There are two paths ahead of you, one leading to the left and the other to the right.")
    time.sleep(2)

    while True:
        action = input("Which path do you choose? (Enter 'LEFT' or 'RIGHT'): ")
        action = action.upper()

        if action == "LEFT":
            print("\nYou take the left path and venture deeper into the cave.")
            # Continue the story based on this choice
            break
        elif action == "RIGHT":
            print("\nYou choose the right path, following the dim light coming from that direction.")
            # Continue the story based on this choice
            break
        else:
            handle_invalid_choice()

# Function for the second level scenario
def level_two_scenario():
    print("\nLevel Two: The Enchanted Forest")
    print("You emerge from the cave and find yourself in a magical forest.")
    print("As you explore, you come across a fork in the road.")
    time.sleep(2)

    while True:
        action = input("Which path do you take? (Enter 'FORWARD', 'LEFT', or 'RIGHT'): ")
        action = action.upper()

        if action == "FORWARD":
            print("\nYou decide to continue straight ahead, eager to uncover the secrets of the forest.")
            # Continue the story based on this choice
            break
        elif action == "LEFT":
            print("\nYou veer left, hoping to find something interesting in that direction.")
            # Continue the story based on this choice
            break
        elif action == "RIGHT":
            print("\nYou take the right path, drawn by the enchanting sounds you hear.")
            # Continue the story based on this choice
            break
        else:
            handle_invalid_choice()

# Function for the third level scenario
def level_three_scenario():
    print("\nLevel Three: The Lost Temple")
    print("You've journeyed deep into the heart of the forest and discovered an ancient temple.")
    print("The entrance to the temple is guarded by two statues.")
    time.sleep(2)

    while True:
        action = input("How do you approach the statues? (Enter 'QUIETLY' or 'BRAVELY'): ")
        action = action.upper()

        if action == "QUIETLY":
            print("\nYou decide to approach the statues quietly, hoping to avoid any unwanted attention.")
            # Continue the story based on this choice
            break
        elif action == "BRAVELY":
            print("\nWith a brave heart, you boldly walk towards the statues, ready for whatever awaits.")
            # Continue the story based on this choice
            break
        else:
            handle_invalid_choice()

# Main function to start the game
def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You are about to embark on an exciting journey filled with mysteries and choices.")
    time.sleep(2)

    level_one_scenario()
    level_two_scenario()
    level_three_scenario()

    print("\nCongratulations! You have completed the adventure game.")

# Start the game
start_game()

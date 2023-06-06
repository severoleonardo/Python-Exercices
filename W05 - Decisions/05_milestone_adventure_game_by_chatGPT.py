import time

# Function to handle invalid choices
def handle_invalid_choice():
    print("Invalid choice. Please select a valid option.")

# Function for the forest scenario
def forest_scenario():
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
    time.sleep(2)

    while True:
        item_choice = input("Which one do you want to pick up? (Enter 'MATCH' or 'FLASHLIGHT'): ")
        item_choice = item_choice.lower()

        if item_choice == "match":
            print("\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated.")
            print("You see a large grizzly bear, and then the match burns out.")
            time.sleep(2)

            while True:
                action = input("Do you want to RUN or HIDE behind a tree? ")
                action = action.lower()

                if action == "run":
                    print("\nYou sprint away from the bear, narrowly escaping its reach.")
                    # Continue the story based on this choice
                    break
                elif action == "hide":
                    print("\nYou quickly hide behind a tree, hoping the bear doesn't spot you.")
                    # Continue the story based on this choice
                    break
                else:
                    handle_invalid_choice()

            # End the scenario
            break

        elif item_choice == "flashlight":
            print("\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you,")
            print("but you thought you also heard something off to the side.")
            time.sleep(2)

            while True:
                action = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
                action = action.lower()

                if action == "follow":
                    print("\nYou decide to follow the path, eager to uncover the source of the noise.")
                    # Continue the story based on this choice
                    break
                elif action == "look":
                    print("\nYou shine the flashlight towards the trees, searching for the thing that made the noise.")
                    # Continue the story based on this choice
                    break
                else:
                    handle_invalid_choice()

            # End the scenario
            break

        else:
            handle_invalid_choice()

# Main function to start the game
def start_game():
    print("Welcome to the Text Adventure Game!")
    time.sleep(2)

    forest_scenario()

    print("\nCongratulations! You have completed the adventure game.")

# Start the game
start_game()

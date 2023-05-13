"""
Title: 02 Prove: Assignment - Word Games
Author: Leonardo Severo

Purpose: Implement a program that generates Mad Libs stories 
"""

print("Please select a story:")

# Display the options for stories
print("1. Terror in the hallway")
print("2. The Mystery of the Haunted Mansion")
print("3. The Quest for the Golden Dragon")

# Ask the user to select a story
story_choice = input("Enter the number of the story you want to personalize: ")

#Ask the user for a series of words
print("Please enter the follwing:")
adjective = input("Adjective: ")
animal = input("Animal: ")
first_verb = input("Verb 1: ")
exclamation = input("Exclamation: ")
second_verb = input("Verb 2: ")
third_verb = input("Verb 3: ")

# Create a list of stories
stories = [

    #Terror in the hallway
    "The other day, I was really in trouble. It all started when I saw a very \n{adjective} {animal} {first_verb} down the hallway. {exclamation}! I yelled. But all \nI could think to do was to {second_verb} over and over. Miraculously, \nthat caused it to stop, but not before it tried to {third_verb} \nright in front of my family.",
    
    #The Mystery of the Haunted Mansion
    "It was a dark and stormy night when I decided to explore the abandoned mansion on the hill. As I entered the old building, I heard a loud \n{exclamation} coming from upstairs. Without hesitation, I grabbed my {adjective} {animal} and slowly made my way up the stairs. Suddenly, \nI saw a shadow move and I knew that something was not right. I quickly {first_verb} to the nearest room and hid behind a {second_verb}. \nThat's when I saw it... a {third_verb} in the corner of the room!",
    
    #The Quest for the Golden Dragon
    "In a far-off land, there was a legendary treasure hidden away in a cave guarded by a fearsome {animal}. \nI knew I had to have it, so I set out on a quest to find the cave. As I journeyed through the mountains, \nI came across a {adjective} {exclamation} who offered to help me on my quest. \nTogether, we climbed the highest peaks and crossed the widest rivers until we finally found the cave. But as we approached, the {animal} appeared and tried to {first_verb} us. \nWith quick thinking, we {second_verb} and {third_verb} the creature out of the way, and we finally reached the treasure."
]

# Display the personalized story based on the user's choices
print("\nYour story is:\n")
print(stories[int(story_choice) - 1].format(adjective=adjective, animal=animal, first_verb=first_verb, exclamation=exclamation.capitalize(), second_verb=second_verb, third_verb=third_verb))

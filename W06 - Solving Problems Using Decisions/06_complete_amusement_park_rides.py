"""
File: Team Activity - Amusement Park Rides (ALL REQUERIMENTS) 
Author: Leonardo Severo

Purpose: Write a program for a fictitious amusement park ride.
"""

rider_aboard = False

first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider? "))

if first_rider_age >= 12 and first_rider_age < 18:
    golden_passport1 = input("Does the rider have a golden passport (yes/no? ")

is_second_rider = input("Is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = int(input("What is the height of the second rider? "))

    if second_rider_age >= 12 and second_rider_age < 18:
        golden_passport2 = input("Is there a golden passport (yes/no)? ")

    if first_rider_height < 36 or second_rider_height < 36:
        rider_aboard = False
    else:
        #3 core requirement  
        if first_rider_age >= 18 or golden_passport1.lower() == "yes" or golden_passport2.lower() == "yes":
            # At least one is an adult
              rider_aboard = True
        else:
            # Neither is an adult

        #4 core requirement
            if first_rider_age >= 12 and first_rider_height >= 52 and second_rider_age >= 12 and second_rider_height >= 52:
                rider_aboard = True
            elif (first_rider_age and second_rider_age >= 14) or (first_rider_age >= 14 and second_rider_age >= 16):
                #6 core requirement
                rider_aboard = True
            else:
                rider_aboard = False
else: # There is only one rider
    #2 core requirement
    if (first_rider_age >= 18 or golden_passport1.lower() == "yes") and first_rider_height >=62:
        rider_aboard = True
    else:
        rider_aboard = False

if rider_aboard:
    print("Welcome aboard rider!")
else:
    print("Sorry, you can't ride this time!")

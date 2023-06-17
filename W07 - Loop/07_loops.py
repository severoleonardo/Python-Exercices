#First example
'''

number = 0

#keep looping as long as the number is less than 10
while number < 10:
    number = int(input("What is the number? "))

print("Finished with the loop")
'''

#Second example
'''
# Start with the number 1
number = 1

# Start with the number 1
while number <= 100000:
    # Display the number
    print(f"The number is: {number}")

    # Update the number to be one more than it was
    number = number + 1

print("Finished with the loop")
'''

# This code first declares the variable "name" before the loop so that it can be used afterward.

number = 0
name = ""

while number < 10:
    number = int(input("What is the number? "))
    name = input("What is your name? ")

print(f"Your name is: {name}")

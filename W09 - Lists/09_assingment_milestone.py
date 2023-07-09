"""
File: 09_assignment_milestone.py
Author: Leonardo Severo

Purpose: create a program that stores a list of products in a shopping cart along with their prices.
"""

#Milestone Requirements: The Menu
# 1. Have menu system that repeats until the user chooses quit
# 2. Creat a list that will store the names of the items in the shopping cart
# 3. Complete the option to add the name of the item to the list
# 4. Complete the option to display the names of the items in the list

cart = []

print()
print("Welcome to the Shopping Cart Program!")

print("\n\nPlease select one of the following:")
while action != "5":
    # Add a new it
    print("1. Add Item")
    print("2. Display cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = input("\nPlease enter an action: ")

    
    if action == "1":
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to cart.")
    elif action == "2":
        if len(cart) == 0:
            print("The cart is empty")
        else:
            # Display the contents of the shopping cart
            print("The contents of the shopping cart are:")
            for item in cart:
                print(item)
    elif action == "3":
        item = input("What item would you like to remove? ")
        if item in cart:
            cart.remove(item)
            print(f"'{item}' has been removed from cart.")
        else:
            print(f"'{item}' is not in the cart.")
    elif action == "4":
        total = len(cart)
        print(f"The total number of items in the cart is: {total}")
    elif action == "5":
        break
    else:
        print("Invalid action. Please try again.")
    
print("Thank you. Goodbye")



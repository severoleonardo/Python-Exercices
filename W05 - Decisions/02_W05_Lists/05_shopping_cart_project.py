# For "Showing Creativity and Exceeding Requirements" I added an apply discount functionality.
# When the user chooses to apply a discount, the program checks if the cart is empty; 
# if so, it prints a message indicating that there are no items to apply a discount to
# Otherwise, it displays the items in the cart and asks the user to enter the number of the item to apply a discount to
# It then applies the discount to the selected item by updating the item_discounts list
# Prints a confirmation message indicating that the discount has been applied
# I've also added some formatting to improve the information that is shown to the user on the screen.

"""
File: 05 Project: Shopping Cart
Author: Leonardo Severo

Purpose: create a program that stores a list of products in a shopping cart along with their prices.
"""

# Final Requirements
# 1 . Store prices as well as names.
# 2 . Change the add functionality to also ask for and store the price of the item.
# 2 . Change the display functionality to also display the prices of the items.
# 4 . When displaying the items, display a number in front of each item. The numbers should start with 1.
# 5 . Complete the option to display the total amount of the prices of all the items in the shopping cart.
# 6 . Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)
# 7 . Complete the option to remove an item from the shopping cart.
# 8 . When removing an item, you should verify the following:
# 8.1. Both the item name and price are removed from their respective lists.
# 8.2. The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.
# 8.3. The program allows you to remove any item from the list including the first one and the last one. (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)

cart = []
item_names = []
item_prices = []
item_quantities = []
item_discounts = []

print()
print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Apply discount")
    print("0. Quit")

    choice = input("Please enter an action: ")

    if choice == "1":
        # Add item functionality
        item_name = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{item_name}'? "))
        item_quantity = int(input(f"How many '{item_name}' would you like to add? "))

        # Append item details to respective lists
        cart.append(item_name)
        item_names.append(item_name)
        item_prices.append(item_price)
        item_quantities.append(item_quantity)
        item_discounts.append(0)  # Initialize discount to zero
        print(f"{item_quantities} '{item_name}' has been added to cart.")
    elif choice == "2":
         # Display cart functionality
        if len(cart) == 0:
            print("Sorry! It looks like your cart is empty.")
        else:
            print("\nThe contents of the shopping cart are:")
            print("\nItem Name        |    Price  |  Quantity  | Discount")
            print("------------------------------------------------")
            for i, item in enumerate(cart, start=1):
                price = item_prices[i-1]
                quantity = item_quantities[i-1]
                discount = item_discounts[i-1]
                total_price = (price - discount) * quantity # Compute the total price per item
                print(f"{i}. {item.ljust(13)} | ${price:8.2f} | {quantity:10} | ${discount:8.2f}")
    elif choice == "3":
        # Remove item functionality
        if len(cart) == 0:
            print("No items in your cart.")
        else:
            print("Items in your cart:")
            for i, item in enumerate(cart, start=1):
                price = item_prices[i-1]
                quantity = item_quantities[i-1]
                print(f"{i}. {item} - ${price:.2f} - Quantity: {quantity}")

            item_index = int(input("Which item would you like to remove? ")) - 1
            if 0 <= item_index < len(cart):
                 # Remove item from all corresponding lists
                item_names.pop(item_index)
                item_prices.pop(item_index)
                item_quantities.pop(item_index)
                item_discounts.pop(item_index)
                removed_item = cart.pop(item_index)
                print(f"'{removed_item}' has been removed from the your cart.")
            else:
                print("Invalid item number.")
    elif choice == "4":
        # Compute total functionality
        total = sum([max((price - discount), 0) * quantity for price, discount, quantity in zip(item_prices, item_discounts, item_quantities)])

        print(f"The total price of the items in the shopping cart is: ${total:.2f}")
    elif choice == "5":
        # Apply discount functionality
        if len(cart) == 0:
            print("Sorry! It looks like your cart is empty.")
        else:
            print("Items in your cart:")
            for i, item in enumerate(cart, start=1):
                price = item_prices[i-1]
                quantity = item_quantities[i-1]
                print(f"{i}. {item} - ${price:.2f} - Quantity: {quantity}")
            
            item_index = int(input("Enter the number of the item to apply discount: ")) - 1
            if 0 <= item_index < len(cart):
                discount = float(input("Enter the discount amount: "))
                item_discounts[item_index] = discount
                print("Discount applied to the selected item.")
            else:
                print("Invalid item number.")
    elif choice == "0":
        # Quit the program
        break
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")

print("\nThank you. Goodbye.")

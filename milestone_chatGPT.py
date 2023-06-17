cart = []

print("Welcome to the Shopping Cart Program!\n")

while True:
    print("Please select one of the following:")
    print("1. Add Item")
    print("2. Display cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = input("Please enter an action: ")

    if action == "1":
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to cart.")
    elif action == "2":
        if len(cart) == 0:
            print("The cart is empty")
        else:
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

print("\nThank you. Goodbye.")

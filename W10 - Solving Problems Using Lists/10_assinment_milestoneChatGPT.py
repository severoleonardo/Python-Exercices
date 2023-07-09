cart = []
item_names = []
item_prices = []
item_quantities = []
item_discounts = []

while True:
    print("\nShopping Cart Menu:")
    print("1. Add item")
    print("2. Display cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Apply discount")
    print("0. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))

        cart.append(item_name)
        item_names.append(item_name)
        item_prices.append(item_price)
        item_quantities.append(item_quantity)
        item_discounts.append(0)  # Initialize discount to zero
        print(f"'{item_name}' has been added to cart.")
    elif choice == "2":
        if len(cart) == 0:
            print("The cart is empty.")
        else:
            print("Items in cart:")
            print("Item Name    |  Price    |  Quantity  | Discount")
            print("------------------------------------------------")
            for i, item in enumerate(cart, start=1):
                price = item_prices[i-1]
                quantity = item_quantities[i-1]
                discount = item_discounts[i-1]
                total_price = (price - discount) * quantity
                print(f"{i}. {item.ljust(13)} | ${price:8.2f} | {quantity:10} | ${discount:8.2f}")
    elif choice == "3":
        if len(cart) == 0:
            print("The cart is empty.")
        else:
            print("Items in cart:")
            for i, item in enumerate(cart, start=1):
                price = item_prices[i-1]
                quantity = item_quantities[i-1]
                print(f"{i}. {item} - ${price:.2f} - Quantity: {quantity}")

            item_index = int(input("Enter the number of the item to remove: ")) - 1
            if 0 <= item_index < len(cart):
                item_names.pop(item_index)
                item_prices.pop(item_index)
                item_quantities.pop(item_index)
                item_discounts.pop(item_index)
                removed_item = cart.pop(item_index)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Invalid item number.")
    elif choice == "4":
        total = sum([max((price - discount), 0) * quantity for price, discount, quantity in zip(item_prices, item_discounts, item_quantities)])

        print(f"The total amount of the prices in the cart is: ${total:.2f}")
    elif choice == "5":
        if len(cart) == 0:
            print("The cart is empty.")
        else:
            print("Items in cart:")
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
        break
    else:
        print("Invalid choice. Please try again.")

print("\nShopping cart program has ended.")

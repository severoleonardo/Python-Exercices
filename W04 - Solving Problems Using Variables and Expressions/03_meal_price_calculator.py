"""
Title: 03 Prove: Milestone - Meal Price Calculator
Author: Leonardo Severo

Purpose: Write a program to calculate the price of a meal.
"""
"""
# Prompts

child_mealprice = float(input("What is the price of a child's meal? "))
adult_mealprice = float(input("What is the price of an adult's meal? "))
children_number = int(input("How many children are there? "))
adults_number = int(input("How many children are there? "))
tax_rate = float(input("What is the sales tax rate? "))

# Calculate 
subtotal = (children_number * child_mealprice) + (adults_number * adult_mealprice)

sales_tax = subtotal * tax_rate / 100

total = subtotal + sales_tax

#Display 

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")


# Payment amount

payment = float(input("\nWhat is the payment amount? "))
print(f"Change: ${payment - total:.2f}")
"""

# Below is the duplicated code with some changes I made in order to exceed the requirements.

# Meal and drink options and prices
child_meal_price = 5.99
adult_meal_price = 10.99
soda_price = 1.99
juice_price = 2.50

# Number of people
print("Hello, welcome to our family diner! Make yourself at home while enjoying our delicious options of meals and drinks. \nPlease, Check out our Menu and select your order below:")
number_of_children = int(input("\nHow many children are eating? "))
number_of_adults = int(input("How many adults are eating? "))

# Tax rate
tax_rate = float(input("What is the tax rate? "))

# Calculate subtotal
subtotal = (number_of_children * child_meal_price) + (number_of_adults * adult_meal_price)

# Add drink prices to subtotal
number_of_sodas = int(input("How many sodas? "))
number_of_juices = int(input("How many juices? "))
subtotal += (number_of_sodas * soda_price) + (number_of_juices * juice_price)

# Calculate tax and total
tax_amount = subtotal * (tax_rate / 100)
total = subtotal + tax_amount

# Display results
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")

# Payment amount

payment = float(input("\nWhat is the payment amount? "))
print(f"Change: ${payment - total:.2f} \n\nThanks! Your order will be prepared and delivered within minutes. We hope you have a pleasant experience and come back soon!")


"""
File: 10_multiple_lists.py
Author: Leonardo Severo

Purpose: Practice working with parallel lists.
"""

# Step 1: Create empty lists for bank accounts and balances
account_names = []
account_balances = []

account_name = None

# Step 2: Loop to get account names and balances from the user
while account_name != "quit":
    account_name = input("What is the name of this account? ")

    if account_name.lower() != "quit":
        account_balance = float(input("What is the balance? "))

         # Add the account name and balance to their respective lists
        account_names.append(account_name)
        account_balances.append(account_balance)

# Step 3: Loop through the lists using an index and display account names with balances
print("\nAccount Information:")
for i in range(len(account_names)):
    print(f"{account_names[i]}: {account_balances[i]}")

# Step 4: Compute and display total balance and average balance
total_balance = sum(account_balances)
average_balance = total_balance / len(account_balances)
print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")
print()
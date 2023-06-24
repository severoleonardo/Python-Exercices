"""
File: 10_stretch_multiple_lists.py
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
    print(f"{i}. {account_names[i]}: ${account_balances[i]:.2f}")

# Step 4: Compute and display total balance and average balance
total_balance = sum(account_balances)
average_balance = total_balance / len(account_balances)
print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")
print()

# Stretch Challenges:
# Step 5:  Determine the bank account with the highest balance and display its name and balance

max_balance = max(account_balances)
max_balance_index = account_balances.index(max_balance)
print(f"Highest balance: {account_names[max_balance_index]} (${max_balance:.2f})")

# Step 6: Update account balances based on user input
update_account = "yes"

while update_account == "yes":
    update_account = input("\nDo you want to update and account?(yes/no): ")

    if update_account == "yes":
        account_index = int(input("What account index do you want to update? "))
        new_balance = float(input("What is the new amount? "))

        account_balances[account_index] = new_balance

        print("\n Account information:")
        for i in range(len(account_names)):
            print(f"{i}: {account_names[i]}: {account_balances[i]:.2f}")
    
    print("\n Account information:")
    for i in range(len(account_names)):
            print(f"{i}: {account_names[i]}: {account_balances[i]:.2f}")
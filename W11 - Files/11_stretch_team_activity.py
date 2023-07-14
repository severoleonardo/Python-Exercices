"""
File: 11_stretch_team_activity.py
Author: Leonardo severo

Purpose: write a program to iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data.
"""

with open("hr_system.txt") as employee_data:

    for line in employee_data:
        # Strip off leading/trailing whitespace.
        # This is important, otherwise, our last variable will have \n characters with it. 
        clean_line = line.strip()

        # Split the current line into its parts based on a space " " as the separator
        parts = line.split(" ")

        # Save each part into a variable
        name = parts[0]
        id = parts[1]
        title = parts[2]
        salary = float(parts[3])

        # Calculate the paycheck amount
        pay_amount = salary / 24

        # Compute engineering bonus
        if title.lower() == "engineer":
            pay_amount += 1000


        # Output the data as desired
        print(f"{name} (ID: {id}), {title} - ${pay_amount:.2f}")
"""
File: 11_sample_team_activity.py
Author: Leonardo severo

Purpose: write a program to iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data.
"""

# The File
# The format of each line is:
# name id_number job_title salary


# Open the file.
# The "with" syntax makes it so I don't have to worry about closing it later

with open("hr_system.txt") as employee_data:
    # The file has now been opened and stored in a variable "employee_data"

    # Go through each line in the file, one by one
    for line in employee_data:
       
       # Split the current line into its parts based on a space " " as the separator
        parts = line.split(" ")

        # Save the parts we need into variables
        name = parts[0]
        title = parts[2]

        # Output the name and title as desired
        print(f"Name: {name}, Title: {title}")
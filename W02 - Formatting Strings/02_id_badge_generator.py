#02 Teach: Programming Activity
##D Badge Generator

#First name
#Last name
#Email address
#Phone number
#Job Title
#ID Number

"""

Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------
"""
"""
I. Core requirements
File: 02_id_badge_generator.py
Author: Leonardo Severo

Purpose: Practice formatting strings.
"""

#variables
first_name = input("First Name: ")
last_name = input("Last Name: ")
email_adress = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job Title: ")
id_number = input("ID number: ")


#formatting strings
output = f"\n\nThe ID Card is: \n_______________________________\n\n{last_name.upper()}, {first_name.title()} \n{job_title.title()} \nID: {id_number} \n\n{email_adress} \n{phone_number}\n_______________________________\n" 

#display message
print(output)


"""
File: teach02_sample.py
Author: Brother Burton

Purpose: Practice formatting strings.
"""
"""
print("Please enter the following information:")

# This prints a blank line
print()

first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

# This time I used a \n to make a blank line before this:
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print("----------------------------------------")
"""
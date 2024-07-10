#Write a program that does the following:

#Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
# age = int(input("How old are you? "))
# next_year_age = age + 1
# print(f"On your next birthday, you will be {next_year_age}.") OR #print(f"On your next birthday, you will be {age + 1}.")


#Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.
# cartons = int(input("How many egg cartons do you have? "))
# eggs = cartons * 123
# print(f"You have {eggs} eggs")


#Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.
cookies = int(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))

cookies_per_person = cookies / people

print(f"Each person may have {cookies_per_person} cookies")
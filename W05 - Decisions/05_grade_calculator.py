"""
Title: 05 Teach - Grade Calculator
Author: Leonardo Severo

Purpose: Write a program that determines the letter grade for a course according to the following scale:

A >= 90

B >= 80

C >= 70

D >= 60

F < 60
"""

# Prompt the user for the grade percentage
percentage = float(input("Please, insert the percentage of your grade: "))

# Determine the letter grade based on the percentage
if percentage >= 90:
    letter_grade = 'A'
elif percentage >= 80:
    letter_grade = 'B'
elif percentage >= 70:
    letter_grade = 'C'
elif percentage >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'   


# Determine the sign for the grade
last_digit = percentage % 10   

if letter_grade == 'A':
    if last_digit >= 7:
        sign = ''
    else:
        sign = '-'
elif letter_grade == 'F':
    sign = ''
else:
    if last_digit >= 7:
        sign = '+'
    elif last_digit < 3:
        sign = '-'
    else:
        sign = ''              

#Combine the letter grade and the sign
letter_grade = letter_grade + sign

# Display the letter grade
print(f"Your letter grade is: {letter_grade}")


# Check if the user passed the course
if percentage >= 70:
    print("Congratulations! You passed the course.")
else:
    print("Unfortunately, you did not pass the course. Keep up the good work next time!")
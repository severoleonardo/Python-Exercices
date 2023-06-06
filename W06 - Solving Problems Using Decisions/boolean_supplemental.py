#
# Boolean logic evaluated one or more conditions to be true or false.
#
# As we evaluate conditions, it allows our program to behave in special
# ways based off of the outcome of those conditions.
#

#
# NOT - Provides the inverse of a boolean evaluation something which is not
#       false is true
#

# Assume we set the value of circle_filled to true.
circle_filled = True

# This will give me the inverse of the value added on the line above.
boolean_not = not circle_filled

# This will print "False"
print(f"The value of boolean_not is: {boolean_not}")

# This could also be reversed, as well. We are negating the negation. This
# doesn't frequently happen, but is useful to understand.
not_boolean_not = not boolean_not

# This will print "True"
print(f"The value of not_boolean_not is: {not_boolean_not}")

#
# AND - Requires all (two or more) evaluated conditions to be true in a set of
#       evaluated conditions.
#

age = int(input("What is your age? "))
sport = input("What is your favorite sport? ")

# Both the age being less than 17 and the sport being baseball must be true
# True and True -> Excecute this code block.
if age < 17 and sport.lower() == 'baseball':

    school_team = input(
        f"Do you play on your school {sport.lower()} team? "
    ).lower()

    if 'y' in school_team:
        print("Fantastic! I hope you do well this year!")
    else:
        print("You should consider playing!")

# Again, the age must be greater than 17 and the age must be less than 50 for
# this code block to execute.
elif age > 17 and age < 50:

    school = input(
        "You are old enough to attend university. If so, where do you go? "
    ).lower()

    if 'byu' in school:
        print("Glad you are attending one of the Lord's universities!")
    else:
        print("Glad you are receiving an education!")



#
# OR - Requires only one evaluated condition to be true in a set of evaluated
#      conditions.
#

color = input("What is the circle's color? ").lower()

if color == 'blue' or color == 'red':
    print(f"{color.capitalize()} is one of my favorite colors!")
elif color == 'black' or color == 'gray':
    print(f"{color.capitalize()} is pretty and dark!")
else:
    print(f"{color.capitalize()} is a nice color!")

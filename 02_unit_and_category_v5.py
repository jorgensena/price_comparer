""" Get the product category and unit
Version 5 : Create a function with regex to check input is not blank or
contains digits
Created by Amy Jorgensen
08/09/21
"""

import re

def no_digit(question):
    valid = False
    while not valid:
        # get value
        value = input(question)
        # Check for digits
        digit = re.search("\d", value)
        # Print error if digit present
        if digit:
            print("Oops, you entered a digit")
            print()
        # Print error if blank
        elif value == "":
            print("Oops, you left it blank")
            print()
        else:
            return value

# Main routine
# Get the product category and check it doesn't contain numbers
category = no_digit("What is the product category? e.g. biscuits : ")

# Get the product unit and check it doesn't contain numbers
unit = no_digit("Enter the common unit for the products: ")

# Print output
print()
print("You entered {}".format(category))

# Print output
print("You entered {}".format(unit))
print()

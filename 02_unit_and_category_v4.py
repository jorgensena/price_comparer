""" Get the product category and unit
Version 4 : Create a function to check that numbers have not been entered
Created by Amy Jorgensen
10/08/21
"""


# Not_blank function
def not_blank(question):
    error = "Oops, you've left it blank!"
    valid = False
    while not valid:
        value = input(question)
        if not value:
            print(error)
        else:
            return value

def no_number(test, question):
    valid = False
    while not valid:
        error = "Oops, you tried to enter a number"
        numbers = False

        for letter in test:
            if letter.isdigit():
                numbers = True
        if numbers is True:
            print(error)
            test = input(question)
        else:
            return test


# Main routine
# Get the product category and check it doesn't contain numbers
category = no_number(not_blank("What is the product category? e.g. biscuits "
                               ": "), "What is the product category?: ")
# Print output
print("You entered {}".format(category))
print()
        
# Get the product unit and check it doesn't contain numbers
unit = no_number(not_blank("Enter the common unit for the products: "),
                 "Enter the common unit for the products: ")

# Print output
print("You entered {}".format(unit))
print()

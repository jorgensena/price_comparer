""" Get the product category and unit
Version 2 : Create a not blank function
Created by Amy Jorgensen
03/08/21
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
            print("You entered {}".format(value))
            print()
            return value


# Main routine
# Get the product category
category = not_blank("What is the product category? e.g. biscuits : ")

# Get the product unit
unit = not_blank("Enter the common unit for the products: ")

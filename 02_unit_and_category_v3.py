""" Get the product category and unit
Version 3 : Check that numbers have not been entered
Created by Amy Jorgensen
09/08/21
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


# Main routine
# Get the product category and check it doesn't contain numbers
valid_2 = False
while not valid_2:
    numbers = False
    category = not_blank("What is the product category? e.g. biscuits : ")

    # Check the category does not contain numbers
    for letter in category:  # Check for digits in category
        if letter.isdigit():
            numbers = True

    if numbers is True:
        print("Oops, please enter the category")

    else:
        valid_2 = True
        print("You entered {}".format(category))
        print()


# Get the product unit and check it doesn't contain numbers
valid_2 = False
while not valid_2:
    numbers = False
    unit = not_blank("Enter the common unit for the products: ")

    # Check the unit does not contain numbers
    for letter in unit:  # Check for digits in unit
        if letter.isdigit():
            numbers = True

    if numbers is True:
        print("Oops, please enter the unit")

    else:
        valid_2 = True
        print("You entered {}".format(unit))
        print()

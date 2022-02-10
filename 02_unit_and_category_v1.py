""" Get the product category and unit, check they are not blank
Version 1
Created by Amy Jorgensen
03/08/21
"""

# Main routine
# Loop to ask category name
valid = False
while not valid:
    # Get the product category
    category = input("What is the product category? e.g. biscuits : ")

    # Category error message
    error_1 = "Oops! Please enter a category."

    # Check that category is not blank
    if not category:
        print(error_1)
    else:
        print("Ooh, today we'll be looking for {}".format(category))
        print()
        valid = True


# Loop to ask unit
valid = False
while not valid:
    # Get the product unit
    unit = input("Enter the common unit for the products: ")

    # Unit error message
    error_2 = "Oops! Please enter a unit."

    # Check that unit is not blank
    if not unit:
        print(error_2)
    else:
        print("So, today we're using {}".format(unit))
        valid = True

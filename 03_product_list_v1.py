""" Get the product names, add them to a list and then print the list
Version 1
Created by Amy Jorgensen
04/08/21
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
# Set up product list
product_list = []

# Get product names
# Need at least two products to compare
valid_list = False
while not valid_list:
    product_name = not_blank("Enter the product name (or 'X' to exit): "
                             "").title()

    # Check for exit code
    if product_name != 'X':
        # If exit code not entered add product to list
        product_list.append(product_name)
    else:
        # Check the list contains at least two items
        if len(product_list) >= 2:
            # Break loop
            valid_list = True
            # Print the list
            print()
            print("Today we will compare these products:"
                  "\n{}".format(product_list))
        else:
            print("You need to enter at least two products to compare")


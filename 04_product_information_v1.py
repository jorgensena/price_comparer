""" Add to component 3, get amount and price, if valid add to list
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


# number checking function
def num_check(question):
    valid = False
    error = "Please enter a number, higher than 0"
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        # if not a number print error
        except ValueError:
            print(error)


# Main routine
# Set up product list
product_list = []

# Get product names
# Need at least two products to compare
valid_list = False
while not valid_list:

    # Get the product name
    product_name = not_blank("Enter the product name (or 'X' to exit): "
                             "").title()

    # Check for exit code
    if product_name != 'X':

        # Get product amount
        product_amount = num_check("Enter the mass/volume of the product: ")

        # Get product price
        product_price = num_check("Enter the price of the product: $")


        # If exit code not entered add product to list
        product_list.append("{} units {} for ${}".format(product_amount,
                                                         product_name,
                                                         product_price))
    else:
        # Check the list contains at least two items
        if len(product_list) > 1:
            # Break loop
            valid_list = True
            # Print the list with each products information on a new line
            print()
            print("Today we will compare these products:")
            for i in product_list:
                print(i)
        else:
            print("You need to enter at least two products to compare")


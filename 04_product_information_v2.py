""" Add to component 3, get amount and price, if valid add to list
Version 2: Create formatting to be reasonable e.g. number of decimal places
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

# Get product information
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

        # Remove decimal point for whole numbers
        if product_amount % 1 == 0:
            product_amount = int(product_amount)
        elif product_amount * 10 % 1 == 0:
            product_amount = "{:.1f}".format(product_amount)  # 1dp (removes
            # 2nd dp when it's 0 e.g. 0.50)
        else:
            product_amount = "{:.2f}".format(product_amount)  # 2dp

        # Get product price
        product_price = num_check("Enter the price of the product: $")

        # Make price 2dp as price is always in 2dp
        product_price = "{:.2f}".format(product_price)

        # If exit code not entered add product to list on one line
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

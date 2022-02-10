""" Calculate the unit price and add it to a list
Version 1
Created by Amy Jorgensen
11/08/21
"""


# Main routine
# Set up unit_price list
unit_price_list = []

# Get product information
# Need at least two products to compare
valid_list = False
while not valid_list:

    # Get the product name
    product_name = input("Enter the product name (or 'X' to exit): "
                             "").title()

    # Check for exit code
    if product_name != 'X':

        # Get product amount
        product_amount = float(input("Enter the mass/volume of the product: "))

        # Get product price
        product_price = float(input("Enter the price of the product: $"))

        # Calculate the unit price
        calc_unit_price = product_price / product_amount

        # Add to list
        unit_price_list.append("{}: ${} per unit".format(product_name,
                                                         calc_unit_price))

    else:
        # Check the list contains at least two items
        if len(unit_price_list) > 1:
            # Break loop
            valid_list = True

            # Print the list with each products unit price on a new line
            print()
            print("Here are the unit prices:")
            for i in unit_price_list:
                print(i)
        else:
            print("You need to enter at least two products")

""" Recipe moderniser - full working program
Add to product loop - Get product amount and price (component 4)
Version 3
Created by Amy Jorgensen
01/09/21
"""

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

# Chech no numbers are present function
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
# Get and check budget
# Ask user for price budget and check its a number
budget = num_check("How much money are you willing to spend? ")

# Get and check category
# Get the product category and check it doesn't contain numbers
category = no_number(not_blank("What is the product category? e.g. biscuits "
                               ": "), "What is the product category?: ")

# Get and check unit
# Get the product unit and check it doesn't contain numbers
unit = no_number(not_blank("Enter the common unit for the products: "),
                 "Enter the common unit for the products: ")


# Get product information...
# Set up product list
product_list = []


# Need at least two products to compare
valid_list = False
# Loop each product
while not valid_list:
    # Check name isn't blank
    # Get product name
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
        product_list.append("{}{} {} for ${}".format(product_amount, unit,
                                                     product_name,
                                                     product_price))
    # Check the price is within the budget otherwise re-ask
    # Calculate the unit price

    else:
        # Check the list contains at least two items
        if len(product_list) >= 2:
            # Break loop
            valid_list = True
            # Print the list
            print()
            print("Today we are comparing these products:")
            for item in product_list:
                print(item)
        else:
            print("You need to enter at least two products to compare")


# Calculate average unit price
# Calculate the most expensive product
# Calculate the cheapest product
# Output a product list
# Output the calculated information
# Output the recommendation

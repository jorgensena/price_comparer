""" Recipe moderniser - full working program
Add to product loop - Ask for information on one line and calculate unit price
(component 5 & 7)
Version 4
Created by Amy Jorgensen
01/09/21
"""


# number checking function
def num_check(question):
    valid = False
    digit_error = "Please enter a number, higher than 0"
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(digit_error)
            else:
                return response
        # if not a number print error
        except ValueError:
            print(digit_error)


# Not_blank function
def not_blank(question):
    blank_error = "Oops, you've left it blank!"
    valid = False
    while not valid:
        value = input(question)
        if not value:
            print(blank_error)
        else:

            return value


# Check no numbers are present function
def no_number(test, question):
    valid = False
    while not valid:
        num_error = "Oops, you tried to enter a number"
        numbers = False

        for letter in test:
            if letter.isdigit():
                numbers = True
        if numbers is True:
            print(num_error)
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
# set up count to tell user what number product they are entering
count = 1

# print instructions for how to enter products
print("Enter the products - quantity, name, price (e.g. 250 cashews 2.50)"
      "\nor 'x' to exit:")

# Need at least two products to compare
valid_list = False
# Loop each product
while not valid_list:
    # error message
    type_error = "There was an error when entering a product, please re-enter"
    # Check name isn't blank
    # Get product name
    product = not_blank("{}. ".format(count)).title()

    # Check for exit code
    if product != 'X':
        try:
            # splits the line of the first space
            get_amount = product.split(" ", 1)

            # Convert the amount to float
            try:
                amount = eval(get_amount[0])  # Convert the amount to float if possible
            except NameError:  # NameError rather than ValueError
                amount = get_amount[0]

            product_price = get_amount[1]

            # Get price and name
            # splits the string into a list containing just the unit and ingredient
            # use rsplit() to split from end of string
            get_price = product_price.rsplit(" ", 1)

            # Convert the price to float
            try:
                price = eval(get_price[1])   # making the 2nd item in the list 'price'
            except NameError:  # NameError rather than ValueError
                price = get_price[1]

            name = get_price[0].title()  # making the 1st item in the list 'name'

            # Check the price is within the budget otherwise re-ask

            # Calculate the unit price
            unit_price = price / amount

            # add product to list
            product_line = [amount, name, price, unit_price]
            product_list.append(product_line)
            count += 1

        # In case the user inputs incorrectly print error and re-loop
        except IndexError:
            print(type_error)
        except SyntaxError:
            print(type_error)
        except TypeError:
            print(type_error)

    else:
        # Check the list contains at least two items
        if len(product_list) >= 2:
            # Break loop
            valid_list = True
            # Print the list
            print()
            print("Today we are comparing these products:")
            # Output a product list
            for item in product_list:
                print("{:.0f}{} {}, ${:.2f} and unit price: ${:0.3f}"
                      .format(item[0], unit, item[1], item[2], item[3]))
        else:
            print("You need to enter at least two products to compare")


# Calculate the most expensive product
# Calculate the cheapest product
# Output the calculated information
# Output the recommendation

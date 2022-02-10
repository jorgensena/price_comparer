""" Recipe moderniser - full working program
Add to product loop - Check the price is within the budget
Calculate the cheapest, most expensive, avg unit price, recommendation
Print final output (component 6)
Version 5
Created by Amy Jorgensen
03/09/21
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
                               ": "), "What is the product category?: ").title()

# Get and check unit
# Get the product unit and check it doesn't contain numbers
unit = no_number(not_blank("Enter the common unit for the products: "),
                 "Enter the common unit for the products: ")
print()

# Get product information...
# Set up lists
product_list = []
unit_prices = []

# set up count to tell user what number product they are entering
count = 1

# print instructions for how to enter products
print("Enter the products - quantity, name, price (e.g. 250 cashews 2.50)"
      "\nor 'x' to exit:")
print()
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

            # Check the price is within the budget
            if price > budget:
                print("Oops, this product is outside the budget, choose another "
                      "product")
            # If the price is valid then add product information to list
            else:
                # Calculate the unit price and add to list
                unit_price = price / amount
                unit_prices.append(unit_price)

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
        else:
            print("You need to enter at least two products within the budget "
                  "to compare")

# Calculations...
# Calculate the average unit price
average_unit_price = sum(unit_prices) / len(unit_prices)

# Calculate the most expensive product...
# Find the most expensive product from the unit price list
most_expensive_price = max(unit_prices)

# Get the most expensive product/s per unit price
expensive_products = []

# Check if there is more than one product with same expensive unit price
for item in product_list:
    if item[3] == most_expensive_price:
        expensive_products.append(item)

# Make it only one expensive by also comparing full price (in case more than 1)
f_price = 0
expensive = []
for item in expensive_products:
    if item[2] > f_price:
        expensive = item

# Calculate the cheapest product...
# Find the cheapest product from the unit price list
cheapest_price = min(unit_prices)

# Get the cheapest product/s per unit price
cheapest_products = []

# check if there is more than one product with same cheap unit price
for item in product_list:
    if item[3] == cheapest_price:
        cheapest_products.append(item)

# Make it only one cheapest by also comparing full price (in case more than 1)
f_price = 0
cheapest = []
for item in cheapest_products:
    if item[2] > f_price:
        cheapest = item

# Output the product list
print()
print("Here are your products for {}:".format(category))

# print the products numbered on a new line
number = 1
for item in product_list:
    print("{}. {:.0f}{} {}, ${:.2f} and unit price: ${:0.3f}"
          .format(number, item[0], unit, item[1], item[2], item[3]))
    number += 1
print()

# Output the calculate information
# Print the average unit price
print("The average unit price is ${:.3f}".format(average_unit_price))
print()

# Print the most expensive item
print("The most expensive product is {} for ${:.2f} as it has a unit price of "
      "${:.3f}".format(expensive[0], expensive[2], expensive[3]))

# Print the cheapest product
print("The cheapest product is {} for ${:.2f} as it has a unit price of ${:.3f}"
      .format(cheapest[0], cheapest[2], cheapest[3]))
print()

# Output the recommendation
print("----------------------------------------------------------------------")
print("Our recommendation of the best product to buy is the {} for ${:.2f} as "
      "\nit has the cheapest unit price within your budget, so you get more "
      "\nvalue for your money".format(cheapest[0], cheapest[2]))
print("----------------------------------------------------------------------")

""" Recipe moderniser - full working program
Usability testing improvements and checking formatting
Version 8
Created by Amy Jorgensen
08/09/21
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
                print()
            else:
                return response
        # if not a number print error
        except ValueError:
            print(digit_error)
            print()


# Not_blank function
def not_blank(question):
    blank_error = "Oops, you've left it blank!"
    valid = False
    while not valid:
        value = input(question)
        if not value:
            print(blank_error)
            print()
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
            print()
            test = input(question)
        else:
            return test


# Main routine
# Print introduction to the program
print("----------------- Welcome to the Price Comparer ---------------------")
print()
# Check if the user wants to read the instructions to the program
print_intro = input(("If you would like instructions explaining what this "
                     "\nprogram does press <enter> otherwise press any key to "
                     "continue: "))

# If the user wants the instructions then print
if not print_intro:
    print("----------------------- INSTRUCTIONS -----------------------------")
    print()
    print("This program will help you to decide what product to buy from a"
          "\nrange of options. By calculating the unit price of each product"
          "\nit will then give you the best recommendation within your budget."
          "\n"
          "\nThe program will ask for your budget to buy one product to help"
          "\nit decide the best recommendation for you."
          "\n"
          "\nThe program will then ask you for the category of the product you"
          "\nwant to buy. This can be as specific or general as you can think"
          "\nof. For example if you wanted to purchase a packet of biscuits"
          "\nthe category could be 'biscuits' or if you wanted to specify"
          "\nmore, you might say 'chocolate biscuits'."
          "\n"
          "\nThe program will ask for the general unit of all the products."
          "\nThis means you will need to make sure all the products are "
          "\nmeasured in the same unit, and if not, you will need to scale "
          "\nthem so they are all measured in the same unit."
          "\n"
          "\nWhen entering the products, PLEASE enter only ONE product per "
          "\nline. Enter the product like the following example - without the"
          "\nunit, dollar sign, or commas separating the information:"
          "\n"
          "\nIn the order: amount, name, price"
          "\ne.g. '250 peppermint chocolate 3.00")
print()
print("----------------------------------------------------------------------")
print()

# Get and check budget
# Ask user for price budget and check its a number
budget = num_check("How much money are you willing to spend? ")

# Get and check category
# Get the product category and check it doesn't contain numbers
category = no_number(not_blank("What is the product category? e.g. biscuits :"
                               " "), "What is the product category?: ").title()

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
# make the colour of the 'x' red to make it stand out more
print("Enter the products - quantity, name, price (e.g. 250 cashews 2.50)"
      "\nor '\033[31mx\033[0m' to finish:")
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
                # Convert the amount to float if possible
                amount = eval(get_amount[0])
            except NameError:  # NameError rather than ValueError
                amount = get_amount[0]

            product_price = get_amount[1]

            # Get price and name
            # splits the string into a list containing just the unit and
            # ingredient use rsplit() to split from end of string
            get_price = product_price.rsplit(" ", 1)

            # Convert the price to float
            try:
                # making the 2nd item in the list 'price'
                price = eval(get_price[1])
            except NameError:  # NameError rather than ValueError
                price = get_price[1]
            # making the 1st item in the list 'name'
            name = get_price[0].title()
            # Check the price is within the budget
            if price > budget:
                print("Oops, this product is outside the budget, choose "
                      "another product")
                print()
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
            print()
            print(type_error)
        except SyntaxError:
            print()
            print(type_error)
        except TypeError:
            print()
            print(type_error)

    else:
        # Check the list contains at least two items
        if len(product_list) >= 2:
            # Break loop
            valid_list = True
        else:
            print("You need to enter at least two products within the budget "
                  "to compare")
            print()

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
only_expensive = []
num_expensive = 1
for item in expensive_products:
    if item[2] > f_price:
        f_price = item[2]
        only_expensive = item
    # If there is more than 1 expensive with the same full price add to list
    elif item[2] == f_price:
        num_expensive += 1
        expensive.append(item)
# If only one most expensive, make sure only 1 item is added to list
if num_expensive == 1:
    expensive.append(only_expensive)

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
f_price = budget
cheapest = []
only_cheapest = []
num_cheapest = 1
for item in cheapest_products:
    if item[2] < f_price:
        f_price = item[2]
        only_cheapest = item
    # If there is more than 1 cheapest with the same full price add to list
    elif item[2] == f_price:
        num_cheapest += 1
        cheapest.append(item)
# If only one cheapest, make sure only 1 item is added to list
if num_cheapest == 1:
    cheapest.append(only_cheapest)

# Output the product list
print()
print("----------------------------------------------------------------------")
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
print("Here's what we found:")
# Print the average unit price
print("The average unit price is ${:.3f}".format(average_unit_price))
print()

# Print the most expensive item
# Check if there is more than one expensive item

if num_expensive > 1:
    exp_number = 1
    print("We found more than one product to be the most expensive:")
    for exp_item in expensive:
        print("{}. {} for ${:.2f} with unit price of ${:.3f}"
              .format(exp_number, exp_item[1], exp_item[2], exp_item[3]))
        exp_number += 1
else:
    for exp_item in expensive:
        print("The most expensive product:"
              "\n{} for ${:.2f} with a unit price of ${:.3f}"
              .format(exp_item[1], exp_item[2], exp_item[3]))
print()

# Print the cheapest product
# Check if there is more than one cheapest product
if num_cheapest > 1:
    print("We found more than one product to be the cheapest:")
    che_number = 1
    for che_item in cheapest:
        print("{}. {} for ${:.2f} with unit price of ${:.3f}"
              .format(che_number, che_item[1], che_item[2], che_item[3]))
        che_number += 1
    print()

    # Output the multiple recommendations
    rec_number = 1
    print("------------------------------------------------------------------")
    print("Due to there being more than one cheapest product, we recommend the"
          "\nbest product to be any of the following, and let you make the"
          "\nfinal decision of which you like more: ")
    # Print each product on a new line
    for recommendation in cheapest:
        print("{}. {} for ${:.2f}".format(rec_number, recommendation[1],
                                          recommendation[2]))
        rec_number += 1
    print()
    print("We recommend these products as they are they have the cheapest unit"
          "\nprice within your budget, so you get more value for your money")
    print("------------------------------------------------------------------")

else:
    for che_item in cheapest:
        print("The cheapest product:"
              "\n{} for ${:.2f} with a unit price of ${:.3f}"
              .format(che_item[1], che_item[2], che_item[3]))
        print()

        # Output the single recommendation
        print("--------------------------------------------------------------"
              "----")
        print("Our recommendation of the best product to buy is the {}"
              "\nfor ${:.2f} as it has the cheapest unit price within your"
              "\nbudget, so you get more value for your money"
              .format(che_item[1], che_item[2]))
        print("--------------------------------------------------------------"
              "----")

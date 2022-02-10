""" Recipe moderniser - full working program
Gets recipe name and recipe source (components 1 & 2)
Version 1: includes 'TO DO' list
Created by Amy Jorgensen
31/08/21
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

# Output values
print("Today's budget: ${:.2f}".format(budget))
print("Category:", category)
print("Unit:", unit)
print()

# Get product information...
# Loop each product
# Get product name
# Get product amount
# Get product price
# Check the price is within the budget otherwise re-ask
# Calculate the unit price
# Add information to product list

# Calculate average unit price
# Calculate the most expensive product
# Calculate the cheapest product
# Output a product list
# Output the calculated information
# Output the recommendation

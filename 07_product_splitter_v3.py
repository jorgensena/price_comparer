""" Further version of an product splitter which splits the product information
from one list of input into name, amount and price
Version 3: Stop the program crashing when its not inputted correctly and re-ask
Created by Amy Jorgensen
01/09/21
"""


# Product list
product_list = []
count = 1

# instructions of how to enter the product
print("Enter the products - quantity, name, price (e.g. 250 cashews 2.50)"
      "\nor 'x' to exit:")

# set up loop
valid = False
while not valid:
    # error message for a input error
    error = "There was an error when entering a product, please re-enter"
    # Get product information
    product = input("{}. ".format(count))

    # Check for exit code
    if product != 'x':
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

            # Check that amount and price have successfully been converted to digits by
            # working out unit_price
            unit_price = price / amount

            # add product to list
            product_line = [amount, name, price, unit_price]
            product_list.append(product_line)
            count += 1

        # In case the user inputs incorrectly print error and re-loop
        except IndexError:
            print(error)
        except SyntaxError:
            print(error)
        except TypeError:
            print(error)
    else:
        valid = True

# print output of each product in the list
for item in product_list:
    # # All 3 elements of the original recipe line are now broken into the 3 required variables
    print("{:.0f} {} {:.2f}".format(item[0], item[1], item[2]))
    # print unit_price
    print("The unit price is ${:.3f}".format(item[3]))
    print()

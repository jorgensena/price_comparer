""" Further version of an product splitter which splits the product information
from one list of input into name, amount and price
Version 2: testing on several products
Created by Amy Jorgensen
30/08/21
"""


# Product has amount followed by name and price
products = ["600.000 Roasted Almonds 16", "500 Roasted cashews 15.00",
            "750 Roasted Salted Peanuts 7.0",
            "400.0 Roasted Salted Mixed Nuts 11.00", "400 Walnut Halves 12.00",
            "300 Roasted salted pistachios 12.00"]

for product_line in products:
    # splits the line of the first space
    get_amount = product_line.split(" ", 1)

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
        price = eval(get_price[1])   # making the last item in the list 'price'
    except NameError:  # NameError rather than ValueError
        price = get_price[1]

    name = get_price[0].title()  # making the 1st item in the list 'name'

    # Check that amount and price have successfully been converted to digits by
    # working out unit_price
    unit_price = price / amount

    # # All 3 elements of the original recipe line are now broken into the 3 required variables
    print("{:.0f} {} {:.2f}".format(amount, name, price))
    # print unit_price
    print("The unit price is ${:.3f}".format(unit_price))
    print()

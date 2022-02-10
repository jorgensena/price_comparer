""" Calculate cheapest, most expensive, average unit price and give a
recommendation
Version 4: Simplify code and get product input with budget
Created by Amy Jorgensen
26/08/21
"""


# Main routine
# Get budget
budget = float(input("Enter the budget (NOTE: Any product outside of the "
                     "\nbudget will automatically be removed from the list): "))
print()

# set up product lists
product_information = []
unit_prices = []

# Create a loop to check the budget can buy a product
valid = False

while not valid:
    # Get product information
    p_name = input("Enter the product name or 'x' to exit: ")

    # check the exit code hasn't been entered
    if p_name != 'x':
        # get rest of product information
        p_amount = float(input("Enter the product amount: "))
        p_price = float(input("Enter the price: $"))

        # make sure the product is within the budget
        if p_price > budget:
            print("Oops, this product is outside the budget, choose another "
                  "product")
        else:
            # calculate unit price and add to list
            u_price = p_price / p_amount
            unit_prices.append(u_price)

            # Add to lists
            product = [p_name, p_amount, p_price, u_price]
            product_information.append(product)

    # Check there is at least 2 products to compare
    elif len(product_information) < 2:
        print("You need to enter 2 or more products to compare")
    else:
        valid = True

# Calculate the average unit price
average_unit_price = sum(unit_prices) / len(unit_prices)

# Find the most expensive product from the unit price list
most_expensive_price = max(unit_prices)

# Get the most expensive product/s per unit price
expensive_products = []

# check if there is more than one product with same expensive unit price
for item in product_information:
    if item[3] == most_expensive_price:
        expensive_products.append(item)

# Make it only one expensive by also comparing full price (in case more than 1)
f_price = 0
expensive = []
for item in expensive_products:
    if item[2] > f_price:
        expensive = item

# Print list (for testing purposes)
print("Most expensive per unit price:", expensive_products[0])

# Find the cheapest product from the unit price list
cheapest_price = min(unit_prices)

# Get the cheapest product/s per unit price
cheapest_products = []

# check if there is more than one product with same cheap unit price
for item in product_information:
    if item[3] == cheapest_price:
        cheapest_products.append(item)

# Make it only one cheapest by also comparing full price (in case more than 1)
f_price = 0
cheapest = []
for item in cheapest_products:
    if item[2] > f_price:
        cheapest = item

# Print list (for testing purposes)
print("Most expensive per unit price:", cheapest_products[0])

# Output
# Print all the products:
for item in product_information:
    print("{} units {} for ${} and a unit price of ${:.3f}"
          .format(item[1], item[0], item[2], item[3]))

# Print the average unit price
print("The average unit price is ${:.3f}".format(average_unit_price))

# Print the most expensive item
print("The most expensive product is {} for ${} as it has a unit price of "
      "${:.3f}".format(expensive[0], expensive[2], expensive[3]))

# Print the cheapest product
print("The cheapest product is {} for ${} as it has a unit price of ${:.3f}"
      .format(cheapest[0], cheapest[2], cheapest[3]))
print()

# Print final recommendation
print("----------------------------------------------------------------------")
print("Our recommendation of the best product to buy is the {} for ${:.2f} as "
      "\nit has the cheapest unit price within your budget, so you get more "
      "\nvalue for your money".format(cheapest[0], cheapest[2]))
print("----------------------------------------------------------------------")

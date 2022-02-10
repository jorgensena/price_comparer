""" Calculate cheapest, most expensive, average unit price and give a
recommendation
Version 1
Created by Amy Jorgensen
12/08/21
"""


# find name function
def find_product(product_list, value):
    # get the information for one product
    for y in product_list:
        try:
            # If the value matches to the product then return the product name
            y.index(value)
            name = y[0]
            return name
        # If it does not match then continue to next product information
        except ValueError:
            continue


# Main routine
# product information list for testing [name, amount, price]
product_information = [["Countdown Walnuts", 450, 10],
                       ["Sliced Almonds", 70, 2.50], ["Pumpkin Seeds", 375, 5]]

# unit_price list for testing [name, unit_price]
unit_price_list = [["Countdown Walnuts", 0.022], ["Sliced Almonds", 0.036],
                   ["Pumpkin Seeds", 0.013]]

# Get just the unit prices
unit_prices = []

for i in unit_price_list:
    product = i
    # Add the unit price to a new list
    unit_prices.append(product[1])

# Calculate the average unit price
average_unit_price = sum(unit_prices) / len(unit_prices)

# Print list
print(unit_prices)
print()

# Get budget
budget = float(input("Enter the budget: "))
print()

# Find the most expensive product from the unit price list
most_expensive_price = max(unit_prices)

# Find the name of the price by using the find product function
expensive_name = find_product(unit_price_list, most_expensive_price)

# Find the cheapest product from the unit price list
cheapest_price = min(unit_prices)

# Find the name of the cheapest by using the find product function
cheapest_name = find_product(unit_price_list, cheapest_price)

# Find the price of the cheapest product
cheapest_full_price = 0

for i in product_information:
    try:
        i.index(cheapest_name)
        cheapest_full_price = i[2]
        break
    except ValueError:
        continue


# Output
# Print the average unit price
print("The average unit price is ${:.3f}".format(average_unit_price))

# Print the most expensive item
print("The most expensive product is {}".format(expensive_name))

# Print the cheapest product
print("The cheapest product is {}".format(cheapest_name))
print()

# Check the price does not exceed the budget
# If the product does exceed the budget then print a warning
if cheapest_full_price > budget:
    print("WARNING:"
          "\nThe cheapest product is currently too expensive for you to buy,"
          "\nplease keep this in mind when making your final decision")
elif cheapest_full_price == budget:
    print("WARNING:"
          "\nThe cheapest product is the same as your budget, please keep this"
          "\nin mind when making your final decision")

# Print final recommendation
print("----------------------------------------------------------------------")
print("Our recommendation of the best product to buy is the {} for ${}"
      .format(cheapest_name, cheapest_full_price))
print("----------------------------------------------------------------------")


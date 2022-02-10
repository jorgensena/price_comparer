""" Calculate cheapest, most expensive, average unit price and give a
recommendation
Version 3: Remove any products from the list which are outside the budget
Created by Amy Jorgensen
20/08/21
"""


# find name function
def find_product(product_list, value):
    # get the information for one product
    name = []
    for x in product_list:
        try:
            # If the value matches to the product then return the product name
            x.index(value)
            name.append(x[0])

        # If it does not match then continue to next product information
        except ValueError:
            continue
    return name


# Make it only one value (min/max)
def one_value(v_name, all_names, all_prices, amount, value):
    # Find the full prices
    full_prices = []

    for name in v_name:
        try:
            # Find the position of the name in product names
            i = all_names.index(name)
            # Using the position add the full price
            full_prices.append(all_prices[i])
        except ValueError:
            continue

    # Make it only one value for the cheapest/most expensive
    # Set up final list to be returned
    name_price = []

    if amount > 1:
        # Get the min/max
        type = value(full_prices)
        # Find the position of the min/max price
        position = full_prices.index(type)
        # Get the name of the min/max price
        type_name = v_name.pop(position)

        # Add to the list
        name_price.append(type_name)
        name_price.append(type)

    else:
        # Add the original info to the list
        name_price.append(v_name[0])
        name_price.append(full_prices[0])

    return name_price


# Main routine
# Create a loop to check the budget can buy a product
valid = False
while not valid:

    # product information lists for testing
    product_names = ["Countdown Walnuts", "Sliced Almonds", "Pumpkin Seeds"]
    product_amounts = [450, 70, 375]
    product_prices = [10, 3, 5]

    # unit_price list for testing [name, unit_price]
    unit_price_list = [["Countdown Walnuts", 0.022], ["Sliced Almonds", 0.036],
                       ["Pumpkin Seeds", 0.013]]

    # Get just the unit prices
    unit_prices = []

    for product in unit_price_list:
        # Add the unit price to a new list
        unit_prices.append(product[1])

    # Calculate the average unit price
    average_unit_price = sum(unit_prices) / len(unit_prices)

    # Get budget
    budget = float(input("Enter the budget: "))
    print()

    # Remove any products from the lists that are outside the budget
    for price in product_prices[:]:
        if price > budget:
            # Find the place of the price outside of the budget
            place = product_prices.index(price)
            # Remove the product from all lists
            del product_prices[place]
            del product_names[place]
            del product_amounts[place]

    # Check how many products are left within budget range
    # Must be more than 2 products to compare
    if len(product_prices) == 0:
        print("All the products are outside your budget, please enter a budget"
              "\nable to compare at least two products")
    elif len(product_prices) < 2:
        print("Please enter a budget that is able to at least compare two "
              "products")
    else:
        valid = True

# Find the most expensive product from the unit price list
most_expensive_price = max(unit_prices)

# In case there are two or more the same which are the max
num_max_prices = 0

# Count how many are the max price
for price in unit_prices:
    if price == most_expensive_price:
        num_max_prices += 1

# Find the name of the price by using the find product function
expensive_name = find_product(unit_price_list, most_expensive_price)

# Print list (for testing purposes)
print("Most expensive per unit price:", expensive_name)

# Make sure it is only one product
most_expensive = one_value(expensive_name, product_names, product_prices,
                           num_max_prices, max)

# Find the cheapest product from the unit price list
cheapest_price = min(unit_prices)

# In case there are two or more the same which are the min
num_min_prices = 0

# Count how many are the max price
for price in unit_prices:
    if price == cheapest_price:
        num_min_prices += 1

# Find the name of the cheapest by using the find product function
cheapest_name = find_product(unit_price_list, cheapest_price)

# Print list (for testing purposes)
print("Cheapest per unit price:", cheapest_name)
print()

# Make sure it is only one product
cheapest = one_value(cheapest_name, product_names, product_prices,
                     num_min_prices, min)

# Output
# Print the average unit price
print("The average unit price is ${:.3f}".format(average_unit_price))

# Print the most expensive item
print("The most expensive product is {} for ${:.2f} as it has a unit price of "
      "${}".format(most_expensive[0], most_expensive[1], most_expensive_price))

# Print the cheapest product
print("The cheapest product is {} for ${:.2f} as it has a unit price of ${}"
      .format(cheapest[0], cheapest[1], cheapest_price))
print()

# Print final recommendation
print("----------------------------------------------------------------------")
print("Our recommendation of the best product to buy is the {} for ${:.2f} as "
      "\nit has the cheapest unit price within your budget, so you get more "
      "\nvalue for your money".format(cheapest[0], cheapest[1]))
print("----------------------------------------------------------------------")

# Check the price does not exceed the budget
# If the product exceeds the budget then print warning
if cheapest[1] > budget:
    print("{} is currently too expensive for you to buy, please keep this "
          "in mind when making your final decision".format(cheapest[0]))
elif cheapest[1] == budget:
    print("{} is the same as your budget, please keep this in mind "
          "\nwhen making your final decision".format(cheapest[0]))

print()
print(product_names)

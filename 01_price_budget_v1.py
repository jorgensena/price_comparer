""" Get the price budget from the user, check that it is not left blank
Version 1
Created by Amy Jorgensen
02/08/21
"""

# Ask user for price budget
budget = float(input("How much money are you willing to spend? "))

# Error message - in the event that the budget is blank
error = "Your budget is blank! Please enter an amount"

# Print error message if budget is blank
if not budget:
    print(error)
else:
    print("Thank you, I'll keep that in mind as I recommend the best option "
          ":)")

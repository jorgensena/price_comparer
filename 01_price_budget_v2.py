""" Get the price budget from the user, check that it is not left blank
Version 2 : Use a number checking function to ensure input is a number and
not blank
Created by Amy Jorgensen
02/08/21
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

# Main routine
# Ask user for price budget and check its a number
budget = num_check("How much money are you willing to spend? ")

# print final statement accepting the budget value
print("Thank you, I'll keep that in mind as I recommend the best option :)")


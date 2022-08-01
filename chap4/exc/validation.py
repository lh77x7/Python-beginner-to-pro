#!/usr/bin/env python3

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value

# float validation
def get_float():
    # implementation
    print()
def get_int():
    # implementation
    print()
    
# the main() function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float(input("Enter monthly investement:\t"))
        yearly_interest_rate = get_float(input("Enter yearly interest rate:\t"))
        years = get_int(input("Enter number of years:\t\t"))

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

# if this module is the main module, call the main() function
# to test the other functions
if __name__ == "__main__":
    main()
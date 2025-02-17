#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":
    # get input from the user

    # monthly investment
    isTrue = True
    while isTrue == True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0:
            isTrue = False
        else:
            print("Entry must be greater than 0. Please try again.")
    
    # yearly interest rate
    isTrue = True
    while isTrue == True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            isTrue = False
        else:
            print("Entry must be greater than 0 and less than or equal to 15.",
            "Please try again.")

    # number of years
    isTrue = True
    while isTrue == True:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            isTrue = False
        else:
            print("Entry must be greater than 0 and less than or equal to 50.",
            "Please try again.")

    print()

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(1, months + 1):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

        # display the result for each year
        if i % 12 == 0:
            print("Year: ", i // 12 , "\tFuture Value:\t", round(future_value, 2))

    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)?: ")
    print()

print("Bye")
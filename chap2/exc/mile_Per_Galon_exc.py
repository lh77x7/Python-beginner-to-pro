#!/usr/bin/env python3

# display a title
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons or gas used:\t\t"))
cost_per_galon = float(input("Enter cost per gallon:\t\t"))

# calculate and round miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg,2)
costPerMile = round(((gallons_used / miles_driven) * cost_per_galon), 2)

# display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Costs:\t\t" + str(gallons_used * cost_per_galon))
print("Cost Per Mile:\t\t" + str(costPerMile))
print()
print("Bye")
#!/usr/bin/env python3

# display welcome message
print("The Area and Parimeter program")
print()

length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

# calculate area and perimeter 
area = length * width
perimeter = 2 * (length + width)

# display results
print("Area = ", area)
print("Perimeter = ", perimeter)
print("Thanks for using this program!\n")

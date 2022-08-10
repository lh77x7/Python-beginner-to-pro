#!/usr/bin/env python3

# display a title
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("=======================")

# get scores from the user and accumulate the total
total_score = 0 # initialize the variable
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))

# calculate average score
average_score = round(total_score / 3)

# format and display the result
print("=======================")
print("Total Score: ", total_score,
"\nAverage Score: ", average_score)
print()
print("Bye")
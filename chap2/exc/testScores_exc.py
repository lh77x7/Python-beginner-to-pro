#!/usr/bin/env python3

# display a title
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("=======================")

# get scores from the user and accumulate the total
total_score1 = 0; total_score2 = 0; total_score3 = 0 # initialize the variable
total_score1 += int(input("Enter test score: "))
total_score2 += int(input("Enter test score: "))
total_score3 += int(input("Enter test score: "))
total_score = total_score1 + total_score2 + total_score3

# calculate average score
average_score = round((total_score / 3), 2)
sum = 0

# format and display the result
print("=======================")
print("Your Scores: ", total_score1, total_score2, total_score3)
print("Total Score: ", total_score)
print("Average Score: ", average_score)
print()
print("Bye")
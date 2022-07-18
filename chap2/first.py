#!/usr/bin/env python3

# this is tutorial program the ilustrates the use of the while
# and if statement

# initialize value
counter = 0
score_total = 0
test_score = 0

# get scores
while test_score != 999:
    test_score = int(input("Enter test score: "))
    if 0 <= test_score <= 100:
        score_total += test_score   # add score to total
        counter += 1                # add 1 to counter
# calculate average score
# average_score = score_total / counter
# average_score = round(average_score)
average_score = round(score_total / counter)

# display the result
print("--------------------------------------")
print("Total Score: " + str(score_total) + "\nAverage score: " + str(average_score))

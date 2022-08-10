#!/usr/bin/env python3

choice = "y"
while choice.lower() == "y":
    # display a welcome message
    print("The Test Scores program")
    print()
    print("Enter \'end\' to end input")
    print("======================")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0

    while True:
        test_score = input("Enter test score: ")
        if test_score.lower() == "end":
            break
        else:
            test_score = float(test_score)
            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print("Test score must be from 0 through 100. Score discarder. Try again.")

    # calculate average score
    average_score = round((score_total / counter), 2)
    score_total = round(score_total, 2)

    # format and display the result
    print("=========================")
    print("Total Score:", score_total, 
    "\nAverage Score: ", average_score)

    # see if the user wants to continue
    choice = input("Enter another set of test scores (y/n)? ")
    print()

print("Bye")
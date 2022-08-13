#!/usr/bin/env python3

# display a welcome message
from statistics import median

def welcome():
    print("The Test Scores application")
    print()
    print("Enter test scores")
    print("Enter 'x' to end input")
    print("======================")


# initialize variables
counter = 0
score_total = 0
test_score = 0
list = []

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        test_score = int(test_score)
        counter += 1
    else:
        break
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

def main():

    welcome()
    # dalej

if __name__ == "__main__":
    main()







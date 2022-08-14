#!/usr/bin/env python3

# display a welcome message
def welcome():
    print("The Test Scores application")
    print()
    print("Enter test scores")
    print("Enter 'x' to end input")
    print("======================")

# get the scores
def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 to 100. " +
                "Score discarded. Try again.")


# process scores and show results
def process_scores(scores):
    # calculate total
    total = 0
    for score in scores:
        total += score
    
    # calculate averaga
    average = round(total / len(scores))

    # get min and max values
    min_value = min(scores)
    max_value = max(scores)

    # get median
    median_index = len(scores) // 2
    if len(scores) % 2 == 1: # odd result
        median_score = scores[median_index]
    else:
        middle1 = scores[median_index]
        middle2 = scores[median_index - 1]
        median_score = (middle1 + middle2) / 2

    # format and display result
    print()
    print("Total:           ", total)
    print("Nr Scores:       ", len(scores))
    print("Average Score:   ", average)
    print("Min Score:       ", min_value)
    print("Max Score:       ", max_value)
    print("Media Score:     ", median_score)
          
# main function            
def main():

    welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Koniec!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()







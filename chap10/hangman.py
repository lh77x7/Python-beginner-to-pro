import random

# list of words from https://www.randomlists.com/random-words?dup=false&qty=30

words = [
    "purring",
    "attach",
    "educated",
    "curved",
    "creator",
    "ill",
    "shiny",
    "squealing",
    "wry",
    "towering",
    "animated",
    "godly",
    "well-off",
    "nervous",
    "fog",
    "detailed",
    "broken",
    "actor",
    "fowl",
    "hungry",
    "apologise",
    "majestic",
    "reduce",
    "cruel",
    "join",
    "special",
    "title",
    "sudden",
    "drawer",
    "white"
]

def get_random_word():
    word = random.choice(words)
    return word

import wordlist

# get a random word from the word list
def get_word():
    word = wordlist.get_random_word()
    return word.upper()

# add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    print("Word:", add_spaces(displayed_word),
    "   Guesses:", num_guesses,
    "   Wrong:", num_wrong,
    "   Tried:", add_spaces(guessed_letters))

# get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()

        # make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. " +
            "Please enter one and only one letter.")
            continue
        # don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess




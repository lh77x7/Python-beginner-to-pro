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
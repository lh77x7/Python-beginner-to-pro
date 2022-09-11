import sys
from os.path import dirname, join
current_dir = dirname(__file__)
FILENAME = "plik_wyjsciowy.txt" # operate on txt file
file_path = join(current_dir, FILENAME)

def get_words_from_file(FILENAME):
    with open(file_path) as file:
        text = file.read()  # read str from file

    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()

    words = text.split(" ") # convert str to list
    print(words)
    return words

def count_words(words):
    # define a dict to store the word count
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1   # increment count for word
        else:
            word_count[word] = 1    # add word with count of 1
    return word_count

def display_word_count(word_count):
    words = list(word_count.keys())
    words.sort(key=str.lower)
    for word in words:
        count = word_count[word]
        print(word, "=", count)

def main():
    print("The Word Count program")
    print()

    # change filename to switch text file
    filename = "plik_wyjsciowy.txt"

    # get words, count, and display
    words = get_words_from_file(filename)
    word_count = count_words(words)
    display_word_count(word_count)

if __name__ == "__main__":
    main()
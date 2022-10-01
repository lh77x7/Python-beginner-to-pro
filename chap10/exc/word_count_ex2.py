from os.path import dirname, join
current_dir = dirname(__file__)
FILENAME = "movies.txt" # operate on txt file
file_path = join(current_dir, FILENAME)

def get_words_from_file(file_path):
    with open(file_path,  errors="ignore") as file:
        text = file.read() # read str from file

    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()

    words = text.split(" ") # convert str to list
    words.sort()
    return words

def get_sentences_from_file(file_path):
    with open(file_path) as file:
        text = file.read()  # read str from file

    sentences = text.split(".")     # convert str to list
    return sentences

def get_unique_words(words):
    unique_words = []
    unique_words.append(words[0])

    for i in range(1, len(words)):
        if words[i] == words[i - 1]:
            continue
        else:
            unique_words.append(words[i])
    return unique_words

def main():
    print("The Word Counter program\n")

    # get sentences
    sentences = get_sentences_from_file(file_path)

    # get words and unique words
    words = get_words_from_file(file_path) # get list of words
    unique_words = get_unique_words(words)

    # display number of sentences, words, and unique words
    print("Number of sentences =", len(sentences))
    print("Number of words = ", len(words))
    print("Number of unique words = ", len(unique_words))

    # display unique words and their word counts
    print("Unique word occurrences:")
    for word in unique_words:
        print("     ", word, "-", words.count(word))

if __name__ == "__main__":
    main()
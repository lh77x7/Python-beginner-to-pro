import mywordlist

# get a random word from the word list
def get_word():
    word = mywordlist.get_random_word()
    return word.upper()

# add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    draw_hangman(num_wrong)
    print("Word:", add_spaces(displayed_word),
    "   Guesses:", num_guesses,
    "   Wrong:", num_wrong,
    "   Tried:", add_spaces(guessed_letters))

def draw_hangman(num_wrong):
    print("_________")
    print("    |")
    if num_wrong == 0:
        print()
    elif num_wrong == 1:
        print("    O\n")
    elif num_wrong == 2:
        print("    O")
        print("    |\n")
    elif num_wrong == 3:
        print("    O")
        print("    |/\n")
    elif num_wrong == 4:
        print("    O")
        print("   \\|/")
        print("    |\n")
    elif num_wrong == 5:
        print("    O")
        print("   \\|/")
        print("    |\n")
    elif num_wrong == 6:
        print("    O")
        print("   \\|/")
        print("    |")
        print("   /\n")
    elif num_wrong == 7:
        print("    O")
        print("   \\|/")
        print("    |")      
        print("   / \\\n")

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

# the input/precess/draw technique is common in game programming
def play_game():
    word = get_word()

    word_length = len(word)
    remainig_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0
    num_guesses = 0
    guessed_letters = ""

    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    while num_wrong < 7 and remainig_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess

        pos = word.find(guess, 0)

        if pos != -1:
            displayed_word = ""
            remainig_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remainig_letters -= 1
                else:
                    displayed_word += "_"
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    if remainig_letters == 0:
        print("Congratulations! You got it in",
        num_guesses, "guesses.")
    else:
        print("Sorry, you lost.")
        print("The word was:", word)

def main():
    print("Play the HANGMAN game")
    draw_hangman(7)
    while True:
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()


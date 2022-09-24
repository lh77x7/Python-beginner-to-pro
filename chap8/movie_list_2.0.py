import csv
import sys
from os.path import dirname, join
current_dir = dirname(__file__)
FILENAME = "movies.csv" # operate on csv file
file_path = join(current_dir, FILENAME)

def display_menu():
    print()
    print("COMMAND MENU\n")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def list_movies(movies):
    for i in range(0, len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie[0] + " (" + str(movie[1]) + ")")
        print()

def add_movies(movies):
    name = input("Name: ")
    while True:
        year = int(input("Year: "))
        if year <= 0:
            print("Year must be greater than zero. Please try again.")
            continue
        else:
            break
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    write_movies(movies)
    print(name + " was added.\n")

def read_movies():
    try:
        movies = []
        with open(file_path, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(movies)
    except Exception as e:
        print(type(e), e)
        exit_program()

def exit_program():
    print("Terminating program.")
    sys.exit()

def delete_movies(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. " +
            "Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(movie[0] + " was deleted.\n")

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movies(movies)
        elif command == "del":
            delete_movies(movies)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
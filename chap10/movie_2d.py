from os.path import dirname, join
current_dir = dirname(__file__)
FILENAME = "movies.txt" # operate on txt file
file_path = join(current_dir, FILENAME)

# write to file
def write_movies(movies):
    with open(file_path, "w") as file:
        for movie in movies:
            line = "|".join(movie)
            file.write(line + "\n")

# read from file
def read_movies():
    movies = []
    with open(file_path) as file:
        for line in file:
            line = line.replace("\n", "")
            movie = line.split("|")
            movies.append(movie)
        return movies

# show the list
def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie[0])
    print()

# add movie
def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(movie + " was added.\n")

# remove movie
def delete_movie(movies):
    index = int(input("Number: "))
    movie = movies.pop(index - 1)
    write_movies(movies)
    print(movie + " was deleted.\n")

# display menu options
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

# main function definition
def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

# check if main is first function to call
if __name__ == "__main__":
    main()
    
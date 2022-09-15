def show_book(book_catalog):
    title = input("Enter the title for book: ")
    if title in book_catalog:
        book = book_catalog(title)
        print("Title:       " + title)
        print("Author:      " + book["author"])
        print("Pub year:    " + book["pubyear"])
    else:
        print("Sorry, " + title + " doesn't exist in the catalog.")

def add_edit_book(book_catalog, mode):
    title = input("Enter title of the book: ")
    if mode == "add" and title in book_catalog:
        print(title + " already exists in the catalog.")
        response = input("Would you like to edit it? (y/n): ").lower()
        if(response != "y"):
            return
    elif mode == "edit" and title not in book_catalog:
        print(title + " doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if(response != "y"):
            return
        
    
    # get book data and create a dictionary for the data
    author = input("Enter author name: ")
    pubyear = input("Enter publication year: ")
    book = {"author": author, "pubyear": pubyear}

    # add the book data to the catalog using title as key
    book_catalog[title] = book

def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + " removed from catalog.")
    else:
        print(title + " doesn't exist in the catalog.")
    
def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print("add - Add book")
    print("edit - Edit book")
    print("del - Delet ebook")
    print("exit - Exit program")

def main():
    book_catalog = {
        "Moby Dick":
        {"author": "Herman Melville",
        "pubyear":  "1851"},
        "The Hobbit":
        {"author": "J.R. R. Tolkien",
        "pubyear": "1937"},
        "Slaughterhouse Five":
        {"author": "Kurt Vonnegut",
        "pubyear": "1969"}
    }

    display_menu()

    while True:
        print()
        command = input("Command : ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode = "add")
        elif command == "edit":
            add_edit_book(book_catalog, mode = "edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
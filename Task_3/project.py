import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
books_file = os.path.join(current_directory, "books.json")

def loadBooks():
    global books
    try:
        with open(books_file, "r") as file:
            books = json.load(file)
            for book in books:
                book["id"] = int(book["id"])
                book["publicationYear"] = int(book["publicationYear"])
    except (FileNotFoundError, json.JSONDecodeError):
        books = []

loadBooks()

def saveBooks():
    with open(books_file, "w") as file:
        json.dump(books, file, indent=4)

def addBook():
    while True:
        try:
            book_id = int(input("Enter Book's ID: ").strip())
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    title = input("Enter Book's Title: ").strip()
    author = input("Enter Book's Author: ").strip()

    while True:
        try:
            publication_year = int(input("Enter Book's Publication Year: ").strip())
            if publication_year > 2025:
                print("Invalid year! Publication year cannot be in the future.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid year (integer).")
            
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "publicationYear": publication_year
    })

    saveBooks()

def viewBooks():
    if not books:
        print("No books available.")
        return
    print("\n\n\nAvailable Books:\n")
    for book in books:
        for key, value in book.items():
            print(key.ljust(15), ":", value)
        print("")

def searchBook():
    while True:
        try:
            num = int(input("Do you want to search with Id or Title:\n 1. Id\n 2. Title\n"))
            if num not in [1, 2]:
                print("Invalid number! Please enter 1 or 2 only.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if num == 1:
        while True:
            try:
                book_id = int(input("Please enter the id you want to search: ").strip())
                break
            except ValueError:
                print("Invalid input! Please enter a valid id (integer).")

        for book in books:
            if book["id"] == book_id:
                for key, value in book.items():
                    print(f"{key.ljust(15)}: {value}")
                return
        
        print("There is no book with this Id!")
    
    else:
        title = input("Please enter the bookTitle you want to search: ").strip()
        for book in books:
            if book["title"].lower() == title.lower():
                for key, value in book.items():
                    print(f"{key.ljust(15)}: {value}")
                return
        
        print("There is no book with this Title!")

def updateBook():
    while True:
        try:
            num = int(input("Do you want to update a book with an ID or Title:\n 1. Id\n 2. Title\n"))
            if num not in [1, 2]:
                print("Invalid number! Please enter 1 or 2 only.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if num == 1:
        while True:
            try:
                book_id = int(input("Please enter the Id you want to search: ").strip())
                break
            except ValueError:
                print("Invalid input! Please enter a valid Id (integer).")

        for book in books:
            if book["id"] == book_id:
                updateHelper(book)
    
    else:
        title = input("Please enter the Id you want to search: ").strip()
        for book in books:
            if book["title"] == title:
               updateHelper(book)       
               
    saveBooks() 

def updateHelper(book):
    for key, value in book.items():
        print(f"{key.ljust(15)}: {value}")
    while True:
        operation = input("Which property do you want to edit?\n 1. Id\n 2. Title\n 3. Author\n 4. Publication Year\n Or press Q to Exit\n").strip()
        if operation.upper() == 'Q':
            print("Updates Done Successfully!")
            for key, value in book.items():
                print(f"{key.ljust(15)}: {value}")
            return
        
        try:
            operation = int(operation)
            if operation == 1:
                book["id"] = int(input("Enter the new ID: ").strip())
            elif operation == 2:
                book["title"] = input("Enter the new Title: ").strip()
            elif operation == 3:
                book["author"] = input("Enter the new Author: ").strip()
            elif operation == 4:
                book["publicationYear"] = int(input("Enter the new Publication Year: ").strip())
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
                continue  
            saveBooks()
        except ValueError:
            print("Invalid input! Please enter a correct value.")

def deleteBook():
    while True:
        try:
            book_id = int(input("Enter Id you want to delete: ").strip())
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            saveBooks()
            print(f"Book with Id {book_id} deleted successfully.")
            return

    print("No book found with this Id.")

while True:
    while True:
        try:
            operation = input(
                "Choose an operation number to perform:\n"
                " 1. Add Book\n 2. View Books\n 3. Search Book\n"
                " 4. Update Book Details\n 5. Delete Book\n"
                " Or Press Q to Quit\n"
            )
            if operation.upper() == 'Q':
                print("Goodbye! See you again later")
                saveBooks()
                exit()

            operation = int(operation) 

            if 1 <= operation <= 5:
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input! Please enter a number (1-5) Or Press Q to Quit.")

    if operation == 1:
        addBook()
    elif operation == 2:
        viewBooks()
    elif operation == 3:
        searchBook()
    elif operation == 4:
        updateBook()
    else:
        deleteBook()

books = []

def addBook():
    while True:
        try:
            book_id = int(input("Enter Book's ID: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    title = input("Enter Book's Title: ")
    author = input("Enter Book's Author: ")

    while True:
        try:
            publication_year = int(input("Enter Book's Publication Year: "))
            if publication_year > 2025:
                print("Invalid year! Publication year cannot be in the future.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid year (integer).")

while True:
    while True:
        try:
            operation = int(input("Choose an operation number to perform:\n 1. Add Book\n 2. View Books\n 3. Search Book\n 4. Update Book Details\n 5. Delete Book\n"))
            if 1 <= operation <= 5:
                break 
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input! Please enter a number (1-5), not letters or symbols.")
    
    if operation == 1:
        addBook()
    elif operation == 2:
        print("Viewing books...")
    elif operation == 3:
        print("Searching for a book...")
    elif operation == 4:
        print("Updating book details...")
    elif operation == 5:
        print("Deleting a book...")
        
        
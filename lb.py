class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'"{book_name}" added to library.')

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Books in Library:")
            for book in self.books:
                print("-", book)

    def issue_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'"{book_name}" has been issued.')
        else:
            print("Book not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f'"{book_name}" returned to library.')


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
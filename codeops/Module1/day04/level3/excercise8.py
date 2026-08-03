# Exercise 8: Library System

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

class Library:
    def __init__(self):
        self.__books = []  # private list of Book objects

    def add_book(self, book):
        # Adds a book to the library
        self.__books.append(book)
        print(f"Added book: '{book.title}' by {book.author}")

    def borrow_book(self, isbn):
        # Marks a book as unavailable if found and available
        for book in self.__books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'.")
                else:
                    print(f"'{book.title}' is currently unavailable.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        # Marks a book as available again
        for book in self.__books:
            if book.isbn == isbn:
                book.available = True
                print(f"You have returned '{book.title}'.")
                return
        print("Book not found.")

    def list_books(self):
        # Prints all books and their availability
        print("\n--- Library Catalog ---")
        for book in self.__books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")

# Create Book objects and a Library, then test add, borrow, and return
library = Library()

book1 = Book("The Alchemist", "Paulo Coelho", "12345")
book2 = Book("1984", "George Orwell", "67890")

library.add_book(book1)
library.add_book(book2)

library.list_books()

library.borrow_book("12345")
library.borrow_book("12345")  # should say unavailable
library.list_books()

library.return_book("12345")
library.list_books()
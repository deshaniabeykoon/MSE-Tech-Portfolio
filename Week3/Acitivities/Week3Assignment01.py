class Library:
    # This class represents a library that can hold multiple books.
    # It has methods to add, remove, and show books in the library.
    # The class is used to manage the collection of books.
    
    # The constructor initializes an empty list of books.
    def __init__(self):
        self.books = [] # List to hold book objects
        # The books list will be used to store book objects.
        # List is used as we need to store more than one book object.
        
    # The add_book method adds a book to the library and prints a message.
    def add_book(self, book):
        self.books.append(book) # Append - adds the book object to the books list
        bookname = book.upper()
        print(bookname,"\nhas been added to the library!\n")

    # The remove_book method removes a book from the library and prints a message.
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book) # Remove - removes the book object from the books list
            print((book),"\nhas been removed from the library.")
        else:
            print((book),"is not found in the library.")

    # The show_books method displays all the books in the library.
    def show_books(self):
        if not self.books: # Check if the books list is empty
            # If the books list is empty, print a message.
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print("- ",(book))

class Book:
    # This class represents a book with a title and an author.
    # It has a constructor to initialize the title and author, and a string representation method.
    # The print_book_det method returns a formatted string with the book's title and author.
    # The class is used to add, remove and show book objects in the library.

    # constructor to initialize the title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        text = f"{self.title} by {self.author}"
        return text

def print_header():
    print('|-----------------------------|')
    print("|  Library Management System  |")
    print('|-----------------------------|')

library = Library()
while True:
    print_header()
    print("|       Menu                  |")
    print('|-----------------------------|')
    print("|       1. Add Book           |")
    print("|       2. Remove Book        |")
    print("|       3. Show Books         |")
    print("|       4. Exit               |")
    print('|-----------------------------|')

    choice = input(" Enter your choice: ")
    #print('|-----------------------------|')

    if choice == '1':
        print(' You will be adding a book   ' )
        print_header()
        title = input(" Enter book title: ")
        author = input(" Enter book author: ")
        book = Book(title, author)
        library.add_book(book)
    elif choice == '2':
        print(' You will be Removing a book   ' )
        print_header()
        title = input(" Enter book title to remove: ")
        library.remove_book(title)
    elif choice == '3':
        print(' You are attempting to view books ' )
        print_header()
        library.show_books()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
# This code implements a simple library management system where users can add, remove, and view books in the library.

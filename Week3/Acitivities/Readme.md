## Assignment 01 - Library Book Manager Using classes
# This code implements a simple library management system where users can add, remove, and view books in the library.
01. class Library represents a library that can hold multiple books. It has methods to add, remove, and show books in the library. It is used to manage the collection of books.
02. The constructor initializes an empty list of books. The books list will be used to store book objects. List is used as we need to store more than one book object.
03. The add_book method adds a book to the library and prints a message.
04. The remove_book method removes a book from the library and prints a message. If the books list is empty it prints a message. 05. The show_books method displays all the books in the library. If books are available for display a for loop is used to iterate through each book in the books list and prints the title and author in uppercase.
06. class Book represents a book with a title and an author. It has a constructor to initialize the title and author, and a string representation method. It is used to add, remove and show book objects in the library.
07. __str__  method returns a string representation of the book object and is used to print the book's title and author in a formatted way. The __str__ method is called when the object is printed and the3 text variable is used to store the formatted string.
08. A function has been used to print a header. 
09. A menu is created to prompt the user for input and it is called using a while loop. The while loop runs indefinitely until the break statement is selected and the user chooses to exit.

## Assignment 02 - Simple Student Grading System Using classes
# This code implements a Python program for a simple student grading system. 
01. It allows users to enter student names and their respective grades, calculates the average grade for each student, and displays the information in a formatted table. 
02. The program includes input validation to ensure that the number of students and grades are within specified limits, the entered values are numeric and that grades are between 0 and 100. 
03. The Student count has been limited to 5 and the subject count has been limited to 4
04. The output is printed in a formatted manner and so trailing spaces have been used
05. A print function is available to print headers

## Assignment 03 - Rewrite sample code (from activity w3-6) without using initializer & self
# This is possible. Each method is declared as a @staticmethod. This allows them to be called without creating an instance of the class. Each method takes the number directly as a parameter instead of using self.
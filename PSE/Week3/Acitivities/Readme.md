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
10. Duplicate handling has not been done

|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 3
 You are attempting to view books 
|-----------------------------|
|  Library Management System  |
|-----------------------------|
No books available in the library.
|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 2
No books available to remove.
|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 1
 You will be adding a book   
|-----------------------------|
|  Library Management System  |
|-----------------------------|
 Enter book title: Learning Python, 6th Edition
 Enter book author: Mark Lutz
LEARNING PYTHON, 6TH EDITION by MARK LUTZ has been added to the library!

|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 1
 You will be adding a book   
|-----------------------------|
|  Library Management System  |
|-----------------------------|
 Enter book title: Learning Python, 5th Edition
 Enter book author: 
LEARNING PYTHON, 5TH EDITION by  has been added to the library!

|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 3
 You are attempting to view books 
|-----------------------------|
|  Library Management System  |
|-----------------------------|
Books available in the library:
-  LEARNING PYTHON, 6TH EDITION by MARK LUTZ
-  LEARNING PYTHON, 5TH EDITION by
|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 2
 You will be removing a book   
|-----------------------------|
|  Library Management System  |
|-----------------------------|
 Enter book title to remove: Learning Python, 6th Edition
LEARNING PYTHON, 6TH EDITION by MARK LUTZ has been removed from the library.
|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 3
 You are attempting to view books 
|-----------------------------|
|  Library Management System  |
|-----------------------------|
Books available in the library:
-  LEARNING PYTHON, 5TH EDITION by
|-----------------------------|
|  Library Management System  |
|-----------------------------|
|       Menu                  |
|-----------------------------|
|       1. Add Book           |
|       2. Remove Book        |
|       3. Show Books         |
|       4. Exit               |
|-----------------------------|
 Enter your choice: 4
Exiting the program.




## Assignment 02 - Simple Student Grading System Using classes
# This code implements a Python program for a simple student grading system. 
01. It allows users to enter student names and their respective grades, calculates the average grade for each student, and displays the information in a formatted table. 
02. The program includes input validation to ensure that the number of students and grades are within specified limits, the entered values are numeric and that grades are between 0 and 100. 
03. The Student count has been limited to 5 and the subject count has been limited to 4
04. The output is printed in a formatted manner and so trailing spaces have been used
05. A print function is available to print headers

|--------------------------------------------------|
|         Student Grading System - Yoobee          |
|--------------------------------------------------|
|    Please Enter the Student and Subject Count    |
|    Student Count should be between 1 and 5       |
|    Subject Count should be between 1 and 4       |
|--------------------------------------------------|
  Enter the number of students: o
Invalid input. Please enter a number.
  Enter the number of students: 2.5
Invalid input. Please enter a number.
  Enter the number of students: 0
Error: Student count must be between 1 and 5.
  Enter the number of students: 8
Error: Student count must be between 1 and 5.
  Enter the number of students: 4
  Enter the number of grades: 0
Error: Subject count must be between 1 and 4.
  Enter the number of grades: 9
Error: Subject count must be between 1 and 4.
  Enter the number of grades: p
Invalid input. Please enter a number.
  Enter the number of grades: 9.1
Invalid input. Please enter a number.
  Enter the number of grades: 3
|--------------------------------------------------|
|              Student Name and Grades             |
|--------------------------------------------------|
  Enter the student's name: Alice
  Enter grade: 98
  Enter grade: p
Invalid input. Please enter a number.
  Enter grade: 87
  Enter grade: 1.5
|--------------------------------------------------|
|              Student Name and Grades             |
|--------------------------------------------------|
  Enter the student's name: Bob
  Enter grade: 87
  Enter grade: 75
  Enter grade: 98
|--------------------------------------------------|
|              Student Name and Grades             |
|--------------------------------------------------|
  Enter the student's name: Cindy
  Enter grade: 88
  Enter grade: 75
  Enter grade: 69
|--------------------------------------------------|
|              Student Name and Grades             |
|--------------------------------------------------|
  Enter the student's name: Derek
  Enter grade: 84
  Enter grade: 65
  Enter grade: 89
|--------------------------------------------------|
|         Student Grading System - Yoobee          |
|--------------------------------------------------|
|            Student Grades and Average            |
|--------------------------------------------------|
|     NAME     |        GRADES        |   AVERAGE  |
|--------------------------------------------------|
|  Alice       | 98.0,87.0,1.5        |   62.17    |
|  Bob         | 87.0,75.0,98.0       |   86.67    |
|  Cindy       | 88.0,75.0,69.0       |   77.33    |
|  Derek       | 84.0,65.0,89.0       |   79.33    |
|--------------------------------------------------|

## Assignment 03 - Rewrite sample code (from activity w3-6) without using initializer & self
# This is possible. Each method is declared as a @staticmethod. This allows them to be called without creating an instance of the class. Each method takes the number directly as a parameter instead of using self.
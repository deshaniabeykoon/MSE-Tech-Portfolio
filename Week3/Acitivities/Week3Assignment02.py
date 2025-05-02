# A Python program that implements a simple student grading system. 
# It allows users to enter student names and their respective grades, calculates the average grade for each student, 
# and displays the information in a formatted table. 
# The program includes input validation to ensure that the number of students and grades are within specified limits, 
# and it also checks that grades are between 0 and 100. 
# The output is presented in a clear and organized manner, making it easy to read and understand.
# The program is structured using classes and methods, promoting code reusability and organization.

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = []

    def __str__(self):
        text = f"Student Name: {self.name}"
        return text
    
    # def display_name(self):
    #     return "Student Name: " + self.name
    
    def add_grade(self):
        while True:
            try:
                grade = float(input("  Enter grade: "))
                if grade < 0 or grade > 100:
                    print("Error: Grade must be between 0 and 100. Please re-enter.")
                else:
                    self.grades.append(grade)
                    break  # Exit the loop on successful input
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_average(self):
        if len(self.grades) == 0:
            print(f"No grades available for {self.name}.")
            return 0
        else:
            average = sum(self.grades) / len(self.grades)
            return average
        
    def show_grades(self):
        if len(self.grades) == 0:
            print(f"No grades available for {self.name}.")
        else:
            #print_headers("seperator")
            limited_name = self.name[:10]  # Limit name to 15 characters
            # Add trailing spaces to ensure a total width of 10 characters for name
            trailing_spaces_name = ' ' * (10 - len(limited_name)) if len(limited_name) < 10 else ''

            grades_str = ','.join(map(str, self.grades))            
            # Add trailing spaces to ensure a total width of 20 characters for grades
            trailing_spaces_grades = ' ' * (19 - len(grades_str)) if len(grades_str) < 19 else ''

            # Add trailing spaces to ensure a total width of 7 characters for average
            trailing_spaces_avg = ' ' * (7 - len(str(self.calculate_average().__round__(2)))) if len(str(self.calculate_average().__round__(2))) < 7 else ''

            print("| ", limited_name, trailing_spaces_name, "|", grades_str, trailing_spaces_grades, "|  ", self.calculate_average().__round__(2), trailing_spaces_avg,"|")

def main():
    def print_headers(header):
        match header:
            case "header":
                print('|--------------------------------------------------|')
                print('|         Student Grading System - Yoobee          |')
                print('|--------------------------------------------------|')
            case "seperator":
                print('|--------------------------------------------------|')
            case "student_header":
                print('|--------------------------------------------------|')
                print('|              Student Name and Grades             |')
                print('|--------------------------------------------------|')
            case "student_avg_header":
                print('|            Student Grades and Average            |')
                print('|--------------------------------------------------|')
                print('|     NAME     |        GRADES        |   AVERAGE  |')
            case _:
                print("Not a valid output")  # Default case

    def validate_count(option):
        while True:
            try:
                count = int(input("  Enter the number of " + ("students" if option == "student" else "grades") + ": "))
                if option == "student" and (count < 1 or count > 5):
                    print("Error: Student count must be between 1 and 5.")
                elif option == "subject" and (count < 1 or count > 4):
                    print("Error: Subject count must be between 1 and 4.")
                else:
                    return count
            except ValueError:
                print("Invalid input. Please enter a number.")

    print_headers("header")
    print("|    Please Enter the Student and Subject Count    |")
    print("|    Student Count should be between 1 and 5       |")
    print("|    Subject Count should be between 1 and 4       |")
    print_headers("seperator")

    students = []
    num_students = validate_count("student") # Validate number of students
    num_grades = validate_count("subject") # Validate number of grades

    for i in range(num_students):
        print_headers("student_header")
        name = input("  Enter the student's name: ")
        student = Student(name)

        for __ in range(num_grades):
            #grade = float(input("  Enter grade: "))
            student.add_grade()

        students.append(student)

    # Display information for all students
    print_headers("header")
    print_headers("student_avg_header")
    print_headers("seperator")
    for student in students:
        student.calculate_average()
        student.show_grades()
    print_headers("seperator")

# The main function serves as the entry point for the program, where user input is collected and processed.
main()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}."

# Demonstration
if __name__ == "__main__":
    student = Student("Alex", 20, 1234)
    print(student.introduce())  # Output: Hi, I'm Alex, 20 years old, and my student ID is 1234.
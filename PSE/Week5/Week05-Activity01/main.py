from database import create_table
from user_manager import add_user, view_users, search_user, delete_user
from course_manager import add_course, view_courses, search_course, delete_course, add_course_user, view_course_users, search_course_user

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("6. Search User by ID and Name")
    print("4. Delete User by ID")

    print("\n==== Course Manager ====")
    print("7. Add Course")
    print("8. View All Courses")
    print("9. Search Course by Name")
    print("10. Delete Course by ID")
    print("11. Search Course by ID and Course Name")
    print("12. Add User to Course")
    print("13. View Users in Course")
    print("14. Search Users in Course by ID and User Name")

    print("5. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-14): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '6':
            user_id = int(input("Enter user ID to search: "))
            name = input("Enter name to search: ")
            users = search_user(user_id,name)
            for user in users:
                print(user)
            if not users:
                print("No user found with that ID and name.")

        elif choice == '7':
            name = input("Enter course name: ")
            unit = int(input("Enter course unit: "))
            add_course(name, unit)
        elif choice == '8':
            courses = view_courses()
            for course in courses:
                print(course)
        elif choice == '9':
            name = input("Enter course name to search: ")
            courses = search_course(name)
            for course in courses:
                print(course)
        elif choice == '10':
            course_id = int(input("Enter course ID to delete: "))
            delete_course(course_id)
        elif choice == '11':
            course_id = int(input("Enter course ID to search: "))
            name = input("Enter course name to search: ")
            courses = search_course(course_id, name)
            for course in courses:
                print(course)
            if not courses:
                print("No course found with that ID and name.")
        elif choice == '12':
            course_id = int(input("Enter course ID to add user to: "))
            user_id = int(input("Enter user ID to add to course: "))
            add_course_user(course_id, user_id)
        elif choice == '13':
            #course_id = int(input("Enter course ID to view users: "))
            users = view_course_users()
            for user in users:
                print(user)
        elif choice == '14':
            course_id = int(input("Enter course ID to search users: "))
            name = input("Enter user name to search: ")
            users = search_course_user(course_id, name)
            for user in users:
                print(user)
            if not users:
                print("No users found with that ID and name in the course.")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

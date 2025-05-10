from database import create_connection
import sqlite3

def add_course(name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print(" Course name must be unique.")
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_course(course_id, name):
    conn = create_connection()
    cursor = conn.cursor()
    if course_id is None and name is not None:
        cursor.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + name + '%',))
    elif course_id is not None and name is None:
        cursor.execute("SELECT * FROM course WHERE id = ?", (course_id,))
    elif course_id is not None and name is not None:
        cursor.execute("SELECT * FROM course WHERE id = ? AND name LIKE ?", (course_id, '%' + name + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
    print("🗑️ Course deleted.")

def add_course_user(course_id, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course_users (course_id, user_id) VALUES (?, ?)", (course_id, user_id))
        conn.commit()
        print(" Course-user relationship added successfully.")
    except sqlite3.IntegrityError:
        print(" Course ID and User ID must be unique.")
    conn.close()

def view_course_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT course_id, course.name as course_name, user_id, users.name as user_name " \
        "FROM course_users " \
        "JOIN course ON course_users.course_id = course.id " \
        "JOIN users ON course_users.user_id = users.id")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_course_user(course_id, user_name):
    conn = create_connection()
    cursor = conn.cursor()
    if course_id is not None and user_name is not None:
        cursor.execute('''
            SELECT course_users.course_id, course.name as course_name, course_users.user_id, users.name as user_name
            FROM course_users
            JOIN course ON course_users.course_id = course.id
            JOIN users ON course_users.user_id = users.id
            WHERE course_users.course_id = ? AND users.name LIKE ?
        ''', (course_id, '%' + user_name + '%'))
    elif course_id is None and user_name is not None:
        cursor.execute('''
            SELECT course_users.course_id, course.name as course_name, course_users.user_id, users.name as user_name
            FROM course_users
            JOIN course ON course_users.course_id = course.id
            JOIN users ON course_users.user_id = users.id
            WHERE users.name LIKE ?
        ''', ('%' + user_name + '%',))
    elif course_id is not None and user_name is None:
        cursor.execute('''
            SELECT course_users.course_id, course.name as course_name, course_users.user_id, users.name as user_name
            FROM course_users
            JOIN course ON course_users.course_id = course.id
            JOIN users ON course_users.user_id = users.id
            WHERE course_users.course_id = ?
        ''', (course_id,))

    #cursor.execute("SELECT course_id, user_id FROM course_users WHERE course_id = ? AND user_id IN (SELECT id FROM users WHERE name LIKE ?)", (course_id, '%' + user_name + '%'))

    # if course_id is None and user_name is not None:
    #     cursor.execute("SELECT * FROM course_users WHERE user_id IN (SELECT id FROM users WHERE name LIKE ?)", ('%' + user_name + '%',))
    # elif course_id is not None and user_name is None:
    #     cursor.execute("SELECT * FROM course_users WHERE course_id = ?", (course_id,))
    # elif course_id is not None and user_name is not None:
    #     cursor.execute("SELECT * FROM course_users WHERE course_id = ? AND user_id IN (SELECT id FROM users WHERE name LIKE ?)", (course_id, '%' + user_name + '%'))
    # if course_id is None and user_id is not None:
    #     cursor.execute("SELECT * FROM course_users WHERE user_id = ?", (user_id,))
    # elif course_id is not None and user_id is None:
    #     cursor.execute("SELECT * FROM course_users WHERE course_id = ?", (course_id,))
    # elif course_id is not None and user_id is not None:
    #     cursor.execute("SELECT * FROM course_users WHERE course_id = ? AND user_id = ?", (course_id, user_id))
    rows = cursor.fetchall()
    conn.close()
    return rows
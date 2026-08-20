from database import create_connection
import sqlite3

def add_enrollment(user, lecture):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO enrollments (user, lecture) VALUES (?, ?)", (user, lecture))
        conn.commit()
        print(" Enrollment added successfully.")
    except sqlite3.IntegrityError:
        print(" Enrollment must be unique.")
    conn.close()
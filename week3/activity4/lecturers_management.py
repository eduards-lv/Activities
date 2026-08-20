from database import create_connection
import sqlite3

def add_lecturer(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" Lecturer added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()


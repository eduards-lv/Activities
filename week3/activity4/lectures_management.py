from database import create_connection
import sqlite3

def add_lecture(name, lecturer, subject):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lectures (name, lecturer, subject) VALUES (?, ?, ?)", (name, lecturer, subject))
        conn.commit()
        print(" Lecture added successfully.")
    except sqlite3.IntegrityError:
        print(" Lecture must be unique.")
    conn.close()
from database import create_connection
import sqlite3

def add_subject(name, descr):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subjects (name, descr) VALUES (?, ?)", (name, descr))
        conn.commit()
        print(" Subject added successfully.")
    except sqlite3.IntegrityError:
        print(" Name must be unique.")
    conn.close()


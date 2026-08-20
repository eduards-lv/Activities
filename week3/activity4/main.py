from database import create_table, create_connection
from user_manager import add_user, view_users, search_user, delete_user
from lectures_management import add_lecture
from subject_management import add_subject
from enrollment_management import add_enrollment
from lecturers_management import add_lecturer


def printtable(tbl):
  conn = create_connection()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM "+tbl)
  rows = cursor.fetchall()
  print("=== "+tbl+" ===")
  for data in rows:
    print(data)
  conn.close()
  print()


def menu():
    print("\n==== User Manager ====")
    print("0. Database Statistics")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Add Lecture")
    print("6. Enroll user to lecture")
    print("7. Add lecturer")
    print("8. Add subject")
    print("9. View data")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (0-9) or press enter to quit: ")
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
        if choice == '5':
            name = input("Enter lecture name: ")
            subject = int(input("Enter the subject of the lecture: "))
            lecturer = int(input("Enter the lecturer of the lecture: "))
            add_lecture(name, subject, lecturer)
        elif choice == '6':
            user = int(input("Enter user ID to enroll: "))
            lecture = int(input("Enter lecture ID to enroll user to: "))
            add_enrollment(user, lecture)
        if choice == '7':
            name = input("Enter the name of lecturer: ")
            email = input("Enter the email of lecturer: ")
            add_lecturer(name, email)
        if choice == '8':
            name = input("Enter the name of subject: ")
            descr = input("Enter the description of subject: ")
            add_subject(name, descr)
        if choice == '9':
          printtable('users')
          printtable('lectures')
          printtable('enrollments')
          printtable('lecturers')
          printtable('subjects')
        if choice == '0':
          conn = create_connection()
          cursor = conn.cursor()
          print("=== Database statistics ===\n\n   Quantity of students in each course:")
          cursor.execute("SELECT count(enrollments.id), lectures.name FROM enrollments left join lectures on enrollments.lecture=lectures.id group by lectures.id")
          rows = cursor.fetchall()
          for data in rows:
            print(data[1]+": "+str(data[0]))
          print()          

          print("=== Quantity of students in more than 1 course ===\n")
          cursor.execute("SELECT count(enrollments.id) as cnt, users.name FROM enrollments left join users on enrollments.user=users.id group by users.id having count(enrollments.id)>1")
          rows = cursor.fetchall()
          for data in rows:
            print(data[1]+" has joined "+str(data[0])+" courses")
          print()          
          conn.close()

        elif choice == '':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

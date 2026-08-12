def isfloat(n):
  """ 
  If string can be converted to integer 
  returns that number, otherwise returns false
  """
  try:
    n=int(n)
    return n;
  except ValueError:
     return False;

def inputint(hint):
  """ 
  Prints hint and asks to enter number.
  Repeats until integer number is entered.
  """
  ret = False
  while ret is False:
    ret = isInt(input(hint))
    if ret is False:
      print("Please enter number")
  return ret 

def inputstr(hint):
  """ 
  Prints hint and asks to enter a string.
  Repeats until string is entered.
  """
  ret = ""
  while ret == "":
    ret = input(hint+": ")
    if ret == "":
      print("Please enter something")
  return ret 

class Student:
  def __init__(this, name, age, address, id):
    this.name=name
    this.age=age
    this.address=address
    this.id=id

class Studentslist:
  def __init__(this):
    """
    Stores list of students in arrray and has functions to sort and print it
    """
    this.data=[]
    #Filling with dummy data
    this.data.append(Student("John Smith", 30, "Test str. 1", 1))
    this.data.append(Student("John Doe", 55, "Test str. 2", 3))
    this.data.append(Student("Jane Doe", 45, "Test str. 3", 4))
    this.data.append(Student("Janeet Doe", 35, "Test str. 4", 5))
    this.data.append(Student("Jonathan Doe", 40, "Test str. 5", 6))
    this.data.append(Student("Jane Smith", 59, "Test str. 6", 4))

  def add(this):
    print("="*20, " Adding new student ", "="*20)
    inputstr("Full name")

  def sort(this):
    this.data.sort(key=lambda student: student.age)
        
  def show(this):
    for i in range(len(this.data)):
      print(this.data[i].name, this.data[i].age, this.data[i].address, this.data[i].id)
     


def main():
  students=Studentslist()
  students.sort()
  students.show()

if __name__ == "__main__":
    main()
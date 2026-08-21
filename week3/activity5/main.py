from database import Database
from currencies import Currencies
from rich import print

class App:
  def __init__(this):
    this.db=Database()
    this.currencies=Currencies()
  
  def showmenu(this):
    print("\n==== User Manager ====")
    print("1. Add currency")
    print("2. Add rate")
    print("3. Add user")
    print("4. Make transaction")
    print("0. Quit")
    return input("Select an option")
    

def main():
  app=App()
  choice=-1
  while choice!='0' and choice!='':
    choice=app.showmenu()
    if choice=='1':
      app.currencies.add()
  print("Bye")
  
if __name__ == "__main__":
    main()
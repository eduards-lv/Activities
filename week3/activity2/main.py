from rich import print
from ucimlrepo import fetch_ucirepo 

def main():
  file = open("junk.txt")
  lines = file.readlines()
  file.close()  
  print("[green]Total lines in file: [bold]"+str(len(lines))+"[/bold][/green]")

  file=open("junk.txt", "a")
  file.write("text file nanalyssis\n")
  file.close()

  file = open("junk.txt")
  lines = file.readlines()
  file.close()  

  file=open("junk.txt", "w")
  for l in lines:
    file.write(l.lower())
  file.close()
  
  

  
if __name__ == "__main__":
    main()
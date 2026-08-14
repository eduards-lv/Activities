from rich import print
from ucimlrepo import fetch_ucirepo 

def main():
  data = open("junk.txt")
  lines = data.readlines()
  data.close()  
  print("Total lines in file: "+str(len(lines)))

  file=open("junk.txt", "a")
  file.write("text file nanalyssis\n")
  file.close()

  file=open("junk.txt", "w")
  for l in lines:
    file.write(l.lower())
  file.close()
  
  

  
if __name__ == "__main__":
    main()
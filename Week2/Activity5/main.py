from rich import print

def isfloat(n):
  try:
    n=float(n)
    return n;
  except ValueError:
     return None;

def inputstr(hint):
  ret = ""
  while ret=="":
    ret = input(hint+": ")
    ret=ret.strip()
  return ret 



class FCconverter:
  def __init__(this):
    this.dataok=False;

  def getdata(this):
    this.dataok=False;
    str=inputstr("Please enter temperature Cxxx or Fxxx")
    scale=str[0]
    if (scale!="F" and scale!="C"):
      print(":cross_mark: [red bold]Temperature must start with F or C![/red bold]")
      return;
    val=str[1:].strip()
    val=isfloat(val)
    if (val is None):
      print(":cross_mark: [red bold]Please enter temperature value as number![/red bold]")
      return;
    this.val=val;
    this.scale=scale;
    this.dataok=True;


def main():
  print("\n[green bold]Hello, this software converts temperature from Celsius to Farenheit and vice versa.[/green bold]\n")
  conv=FCconverter()
  conv.getdata()
  if (conv.dataok):
    print("Data ok")
  else:
    print("You have entered incorrect data, see you later.")


  
if __name__ == "__main__":
    main()
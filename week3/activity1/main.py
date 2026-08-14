from rich import print
from ucimlrepo import fetch_ucirepo 

def main():
  # fetch dataset 
  iris = fetch_ucirepo(id=53) 
   
  # data (as pandas dataframes) 
  X = iris.data.features 
  y = iris.data.targets 

  print("[green]Total number of records is [bold]"+str(len(X))+"[/bold][/green]")
  print("[green]Total number of different flowers is [bold]"+str(y.iloc[:, 0].nunique())+"[/bold][/green]")
  print("[green]The names of all different flowers in the dataset[/green]")
  for name in y.iloc[:, 0].unique():
    print("[green bold]"+name+"[/green bold]")
  # metadata 
  #print(iris.metadata) 
  
  # variable information 
  #print(iris.variables) 
  
  
if __name__ == "__main__":
    main()
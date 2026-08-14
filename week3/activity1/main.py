from ucimlrepo import fetch_ucirepo 

def main():
  # fetch dataset 
  iris = fetch_ucirepo(id=53) 
   
  # data (as pandas dataframes) 
  X = iris.data.features 
  y = iris.data.targets 

  print("Total number of records is", len(X))
  print("Total number of different flowers", y.iloc[:, 0].nunique())
  print("Tha names of all different flowers in the dataset")
  for name in y.iloc[:, 0].unique():
    print(name)
  # metadata 
  #print(iris.metadata) 
  
  # variable information 
  #print(iris.variables) 
  
  
if __name__ == "__main__":
    main()
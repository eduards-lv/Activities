def factorial(n):
  ret=1
  for i in range(n):
    ret=ret*(i+1)
  return ret

def fibonacci(n):
  prev1=0
  prev2=1
  for i in range(n):
    if (i==0):
         print(prev1, " ", end="")
    elif (i==2):
         print(prev2, " ", end="")
    else:
       temp=prev1+prev2
       print(prev1+prev2, " ", end="")
       prev1=prev2
       prev2=temp


def main():
  n = int(input("Please enter number:"))
  print("\n")
  print("Factorial of ", n, " is ",factorial(n))
  print("\n")
  print("Fibonacci sequence of ", n, " numbers is:")
  fibonacci(n)

if __name__ == "__main__":
    main()
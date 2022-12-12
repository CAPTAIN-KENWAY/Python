from art import logo
def add(n1, n2):
  return n1+n2
def subtract(n1, n2):
  return n1-n2
def multiply(n1, n2):
  return n1*n2
def divide(n1, n2):
  return round(n1/n2,1)

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(logo)
  num1=float(input("What is the first number? "))
  for key in operations:
    print(key)
  
  ans='y'
  answer=num1
  while ans=='y':
    operation_symbol=input("Pick an operation: ")
    num=float(input("What's the next number? "))
    calculation_function=operations[operation_symbol]
    answer=calculation_function(num1,num)
    print(f"{num1} {operation_symbol} {num} = {answer}")
    ans=input(f"Type y to continue calculating with {answer}, or type n to start new calculation: ").lower()
    if ans=='y':
      num1=answer
    elif ans=='n': 
      calculator()

calculator()
    
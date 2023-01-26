# python 3
# calculator app
from replit import clear
from art import logo
def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1 , num2):
  return num1 / num2
calc_continue = "N"
result = 0
operators= {
  "+" : "add",
  "-" : "subtract",
  "*" : "multiply",
  "/" : "divide",
}
while True:
  print(logo)
  if calc_continue=='N': 
    number1 = float(input('Type a number : '))
  elif calc_continue=="Y":
    number1 = result
  number2 = float(input('Type second number : '))
  operation_symbol = input('Choose an operator (+ , - , * , /)      :     ')
  operation= operators[operation_symbol]
  if operation == 'add':
    result = add(number1,number2)
  elif operation == 'subtract':
    result = subtract(number1,number2)
  elif operation == 'multiply':
    result = multiply(number1,number2)
  elif operation == 'divide':
    result = divide(number1,number2)
  print(f"\n{number1} {operation_symbol} {number2} is {result}. \n ")
  calc_continue=input('\nIf you are going you use the result for next calculation type Y, else type N, if you want to EXIT type E : \n').upper()
  clear()
  if calc_continue=='E':
    print("Goodbye!")
    print(logo)
    break
  

  



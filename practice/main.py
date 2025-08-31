from task1 import basic_calculator
#display operations to the user
def calculator(): 
 print("select operation:\n1.ADD\n2.Subtract\n3.Multiply\n4.Divide\n5.Square Root\n6.Exponent\n7.Exit ")

#take input from user for operation choice and input handling



#get 2 numbers as input from the user.


while True:

 try:
  operation_choice = int(input("Enter Choice between -> \t1/2/3/4: ").strip())
  num1 = float(input("enter first number: "))
  num2 = float(input("enter second number: "))
  if operation_choice == 1:
    print(f"Result: {num1} + {num2} = {basic_calculator.add(num1, num2)}")
  elif operation_choice == 2:
    print(f"Result: {num1} - {num2} = {basic_calculator.subtract(num1, num2)}") 
  elif operation_choice == 3:
    print(f"Result: {num1} * {num2} = {basic_calculator.multiply(num1, num2)}")
  elif operation_choice == 4:
    print(f"Result: {num1} / {num2} = {basic_calculator.divide(num1, num2)}")
  elif operation_choice == 5:
    num3 = input("Enter the number: ")
    print(f"Result: = {basic_calculator.square_root(num3)}")

  elif operation_choice == 6:
    print(f"Result: {num1} + {num2} = {basic_calculator.exponent_function()}")
  else:
    print("Invalid Choice, Try again.")
 except ValueError:
   print("Only numbers are allowed for this calculator.")
#basic calculator.

#denominator error.
def denominator_error(b):
  if b == 0:
    raise ZeroDivisionError


#for addition
def add(a,b):
 return a+b


#for subtraction.
def subtract(a,b):
  return a-b

#for multiplication
def multiply(a,b):
  return a*b

#for division
def divide(a,b):
  denominator_error(b)
  return a/b

#for square_root
def square_root(a):
  if a < 0:
    raise ValueError
  else:
   return a**0.5

def exponent_function(a,b):
 return a**b

def modulus_function(a,b):
  denominator_error(b)
  return a % b
#   operation_choice = int(input("Enter Choice\t1/2/3/4: "))

# #display operations to the user 
# print("select operation:\n1.ADD\n2.Subtract\n3.Multiply\n4.Divide ")

# #take input from user for operation choice and input handling

 
#   if not operation_choice is int:
#     raise TypeError
# finally:


# #get 2 numbers as input from the user.
#  num1 = float(input("enter first number: "))
#  num2 = float(input("enter second number: "))



  


# if operation_choice == 1:
#   print("Result:", add(num1, num2))
# elif operation_choice == 2:
#   print(f"Result: {subtract(num1, num2)}") 

# elif operation_choice == 3:
#   print(f"Result {multiply(num1, num2)}")

# elif operation_choice == 4:
#   print(f"Result: {divide(num1, num2)}")

# else:
#   print("invalid choice")
#handling errors in python.
#there are 3 categories of errors in python.
#  -syntax error
# it occurs when python interpreter cannot understand your code because you broke python grammar rules., it won't work until you code is fixed.
# types of syntax errors.
# indentation error - incorrect spacing.
#indentaion is paragraphing.
# for i in range(3):
# print(i)

# #missing colon/parenthesis error.
# if 5>3 #missing colon
#  print("hello")
# #invalid syntax - general grammar mistakes.
# print "hello"  #missing parentheses.
#runtime errors. 
#the program is syntactically correct, but an error occurs while it is running.
#runtime errors are also called excepetions.
#they can be handled with try, except, and finally.
#common subtypes of runtime errors.
#- zerodivison error. - dividing by zero
# print (10/0)
# #nameerror - using a variable before defining it.
# print(age)  #age not defined.
# # TypeError - wrong data type in an operation.
# result = "10" + 5 #str + int not allowed
# #valueerror - invalid value for a function.
# # number = int("abc") #cannot convert str to int.
# # index error - accessing list index out of range.
# fruits = ["apple", "banana"]
# print(fruits[3]) #index out of range, meaning that the length of the variable, fruits is 2.
# #keyerror - accesing a dictionary with a missing key.
# data = {"name": "ada"}
# print(data["age"]) #key not found. meaning that the key "age" is not available.
# #filenotfounderror - file does not exist.
# f = open("missing.txt") #file not found.

#handling runtime errors
#python provides exception handling to prevent programs from crashing when unexpected errors occur.
#keywords used are : try, except and finally.
 #the try block is used to wrap code that might raise an error.
#  #if no error occurs, python skips the excpet block.
# try: 
#     x= 10/0
#     print("Result:",  x)

# #the except block.
# it defines what to do if an error occurs inside try.
# it can push specific errors or all errors. 
try: 
    x = 10/0
except ZeroDivisionError:
    print("cannot divide by zero")

    #this is a case of multiple exception.
    try:
        number = int("abc") #valueerror
        result = 10/0 #zerodivisionerror.
    except ValueError:
        print("Invalid Conversion to integer.")
    except ZeroDivisionError:
        print("cannot divide by zero.")

#the finally block.

#always runs, whether an error occured or not.
#useful for cleanup tasks(e.g. closing files, releasing resources.)
try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("closing file if it was opened.")
   
   
    balance = 5000 #starting balance.
    print("welcome to the ATM")
    amount = input("enter your amount to withdraw: ")

    try:
        amount = float(amount) #convert input to number.
        if amount > balance:
            raise ValueError("Insufficient Funds.")
        balance -= amount
        print("Withdrawal Successful. New balance: N", balance)
    except ValueError as e:
        print("error:", e)
    except Exception as e:
        print("unexpected error:", e)
    finally:
        print("transaction session closed.")
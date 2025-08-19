# #control flow is divided into 3 parts.
# #A- conditional statements - (if, if-else, if-elif-else, nested if.)
# #if - is used for executing a block only when the condition is true.
# age = 20
# if age >= 18:
#     print("you are eligible to vote")
#     #usecases 
#     # - checking for eligbility.
#     #validating login attempts
#     #ensuring a minimum purchase requirement.

# #if-else statements.
# #provides 2 alternative paths.
# wallet = 400
# price = 500
# if wallet >= price:
#     print("Transaction Successful")
# else:
#     print("Insufficient Balance")
#     #use-cases
#     # - deciding success or failure of payments
#     # _ granting or denying access to a system.
#     # - determining pass/fail in an exam, etc.

# #- if-elif-else statements.
# #used for multiple conditions.
# score = 85.
# if score >= 70:
#     print('Grade A')
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")

#     #use-cases
#     #student grading systems
#     #assigning ticket categories(VIP, Regular, Student.)
#     #categorizing temperatures (Hot, Warm, Cold,) etc.

# #nested if
# #placing an if inside another if.

# age = 19
# citizen = True

# if age >= 18:
#     if citizen :
#         print("You can Vote")
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("too young to vote")
#use-cases 
#voting eligibility (age + citizenship)
#banking (account active + balance sufficient)
#school admission (age + grade level).

#B-LOOPS.
#for loop
#this is used for iterating over a sequence( strings, list, tuple, dictionary)
# #iterates through each element in a LIST.
# fruits = ["apple", "banana", "Orange"]
# for fruit in fruits:
#     print(f"I like {fruit}")

#     #usecases - 
#     #iterating through shopping lists.
#     #checking products availability.
#     #displaying student names. etc

# #iterates through each element in a tuple, (works like lists but tuples are immutable.)

# coordinates = (0.3456, 0.9876, 0.43215)
# for point in coordinates:
#     print(f"Point: {point}")
# #use cases
# #storing fixed sensor readings.
#displaying fixed seating positions.

#iterates through an element in a dictionary. remmeber that dictionaries have key-value pairs.

# student = {
#     "name": "tunde",
#     "age": 45,
#   "grade": "A"
# }
# for key, value in student.items():
#     print(f"{key}: {value}")
#     #some usecases.
#     #reading database records.
#     #showing profile details.
#     #checking configuration setttings, etc.


# #iterates through elements in a string.
# word = "python"
# for char in word:
#     print(char)

#     #strings are sequence of characters.
#     #some usecases.
#     #counting vowels/consonants.
#     #password validation(checking digits/special chars).
#     #text analysis

#while loop
# a while loop is used to repeatedly execute a block of code as long as a given condition is true. 
#code block.
# - the condition must evaluate to True for the loop continue running.
# - when the condition becomes false the loop stops.

# let the loop start with count = 1
# let it keep printing until count is greater than 5
# let the loop terminate when the condition is no longer true.
#my code.
# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1
#incrementing with 'while'
num = 1
while num <= 10:
    print(num, end = " ")
    num += 1
    #decrementing with 'while'
    timer = 10
    while timer > 0:
        print("Countdown:", timer)
        timer -=1
    
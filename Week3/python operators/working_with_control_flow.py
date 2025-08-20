# # #control flow is divided into 3 parts.
# # #A- conditional statements - (if, if-else, if-elif-else, nested if.)
# # #if - is used for executing a block only when the condition is true.
# # age = 20
# # if age >= 18:
# #     print("you are eligible to vote")
# #     #usecases 
# #     # - checking for eligbility.
# #     #validating login attempts
# #     #ensuring a minimum purchase requirement.

# # #if-else statements.
# # #provides 2 alternative paths.
# # wallet = 400
# # price = 500
# # if wallet >= price:
# #     print("Transaction Successful")
# # else:
# #     print("Insufficient Balance")
# #     #use-cases
# #     # - deciding success or failure of payments
# #     # _ granting or denying access to a system.
# #     # - determining pass/fail in an exam, etc.

# # #- if-elif-else statements.
# # #used for multiple conditions.
# # score = 85.
# # if score >= 70:
# #     print('Grade A')
# # elif score >= 50:
# #     print("Grade B")
# # else:
# #     print("Grade C")

# #     #use-cases
# #     #student grading systems
# #     #assigning ticket categories(VIP, Regular, Student.)
# #     #categorizing temperatures (Hot, Warm, Cold,) etc.

# # #nested if
# # #placing an if inside another if.

# # age = 19
# # citizen = True

# # if age >= 18:
# #     if citizen :
# #         print("You can Vote")
# #     else:
# #         print("You must be a citizen to vote")
# # else:
# #     print("too young to vote")
# #use-cases 
# #voting eligibility (age + citizenship)
# #banking (account active + balance sufficient)
# #school admission (age + grade level).

# #B-LOOPS.
# #for loop
# #this is used for iterating over a sequence( strings, list, tuple, dictionary)
# # #iterates through each element in a LIST.
# # fruits = ["apple", "banana", "Orange"]
# # for fruit in fruits:
# #     print(f"I like {fruit}")

# #     #usecases - 
# #     #iterating through shopping lists.
# #     #checking products availability.
# #     #displaying student names. etc

# # #iterates through each element in a tuple, (works like lists but tuples are immutable.)

# # coordinates = (0.3456, 0.9876, 0.43215)
# # for point in coordinates:
# #     print(f"Point: {point}")
# # #use cases
# # #storing fixed sensor readings.
# #displaying fixed seating positions.

# #iterates through an element in a dictionary. remmeber that dictionaries have key-value pairs.

# # student = {
# #     "name": "tunde",
# #     "age": 45,
# #   "grade": "A"
# # }
# # for key, value in student.items():
# #     print(f"{key}: {value}")
# #     #some usecases.
# #     #reading database records.
# #     #showing profile details.
# #     #checking configuration setttings, etc.


# # #iterates through elements in a string.
# # word = "python"
# # for char in word:
# #     print(char)

# #     #strings are sequence of characters.
# #     #some usecases.
# #     #counting vowels/consonants.
# #     #password validation(checking digits/special chars).
# #     #text analysis

# #while loop
# # a while loop is used to repeatedly execute a block of code as long as a given condition is true. 
# #code block.
# # - the condition must evaluate to True for the loop continue running.
# # - when the condition becomes false the loop stops.

# # let the loop start with count = 1
# # let it keep printing until count is greater than 5
# # let the loop terminate when the condition is no longer true.
# #my code.
# # count = 1
# # while count <= 5:
# #     print("Number:", count)
# #     count += 1
# #incrementing with 'while'
# # num = 1
# # while num <= 10:
# #     print(num, end = " ")
# #     num += 1
# #     #decrementing with 'while'
# #     timer = 10
# #     while timer > 0:
# #         print("Countdown:", timer)
# #         timer -=1
#     # while with user input
#     #     keep asking until the user enters a correct password.
# # password = ""
# # while password != "python123":
# #         password = input("Enter the password: ")
# # print("access granted")

# #understanding while True.
# #- the While True is an infinite loop - it keeps running forever until you explicitly stop it with a break statement or by exiting the program.
# # it is commonly used when:
# #- you  don't know in advance how mnay times you want the loop to run.
# # you want to keep asking the user for input until a valid condition is met.
# # you are building continuous programs like menus, login systems, or simulations.

# #while True:
# #code block
# #must include a break statement to stop


# #keep asking the user for a name until they type "exit."

# # while True:
# #     name =input("enter your name (type exit to quit): ")
# #     if name.lower() == "exit":
# #         print("goodbye!")
# #         break
# #     print(f"hello,{name}")
#     ##use-cases
#     #_ in chat-like applications, forms, or data entry programs where users may input multiple items until they decide to stop.


#     #loop control statements (break, continue and pass)
#     #these keywords help us control the behaviour of loops (for and while).
#     #instead of loops always running all iterations, we can skip steps, stop early or do ntohing intentionally.

#     #1. break.
#     #stops loop immediately. it is used if acondition is met and there's no need to continue looping.

# # for num in range (1,10):
# #         if num == 5:
# #             break
# #         print(num)

#         #the loop stops completely when num == 5.
#         #stop searching when an item is found.
#         #exit when user input matches a condition.
#         #prevent unnecessary iterations.

#         #2.continue
#         #skips the current iteration and moves to the next one.
#         #it is used if you want to ignore some values but keep the loop running.

# for num in range(1,6):
#             if num == 3:
#                 continue
#             print(num)
#         #     #3 is skipped, but the loop continues.
#         #     ##some usecases
#         #     #skip invalid data.
#         #     #ignore unwanted characters (like spaces in a string)

#         #     #3. pass, it does nothing.a placeholder to avoid errors. it is used if you haven't written the code yet but want to keep the structure.
#         #     for num in range(1,6):
#         #         if num == 3:
#         #             pass #do nothing for now
#         #         else:
#         #             print(num)

#                     # at num == 3, python executes pass (nothing happens).
#                     ## some usecases
#                     #writing code structure (to fill in later).

 # try and think through this.
while True:
    print("\nMenu,Pick an Option:")
    print("1.Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = (input("Choose an option: ").strip())
    if choice == "1":
        print("Hello")
        break
    elif choice == "2":
        print("Goodbye")
        break
    elif choice == "3":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice. Try Again.")
        #while true needs a break statement to stop.
        #how does the loop end with any thing either than the options in choice
        


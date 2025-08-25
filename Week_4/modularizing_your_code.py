# # #introduction to modularity, what modular programming means.
# # #modularity is important for debugging, teamwork, readability, reusability.
# # #modularity is a smarter and shorter way of writing the correct code, that is, it runs faster for the business.
# # #all businesses have specific ways they write code to make it run faster, we can't use the code we use to explain a process to run the business or be deployed as the business process so it's important we modularize.
# # #a module can be a function, class or a python file that performs a specific task.
# # #the modules can be combined to build a complete a program.
# # #modular programming = breaking big problems into smaller, manageable solutions.
# # #its important we modularize to debug our code, it's manageable and works faster especially for semantic errors.

# # #modularity is important because it makes it easier to read and understand. Looking at smaller compartemntalised files is easier to read than long lines of code that can get one lost in the process.
# # #i'll use this to complete my ussd task.
# # #reusability
# # #once you write it in can be applied in similar scenarios or for other purposes, like now, the 
# # #function to calculate the area of a circle can be used in the calculation of longitude and latitude calculations or coordinate geometry.

# # #debugging and maintenance, if there's an error you only need to check the specific module where the problem is,
# # # instead of combing through the program, then updating one module doesn't affect the whole system. 
# # #lets say you are building a banking application, if the payment module in the app has a bug, the uer login moodule is unaffected.
# # #which is true because why should the bad network affect my ability to login to the app.
# # #true for teamwork , this allows for easy delegation of tasks, working on all different modules simultaneously, this makes work faster.

# # #yes i understand the wedding concept. further emphasis on people that try to multitask by doing everything themselves, all at once, making work difficult.
# # # functions, (which is the first level of modularity) 
# # # _ defining and calling a function, definition, parameters, arguments, return values, use cases (math operations, repeated tasks, formatting output)

# # #definition of a function.
# # # a function is a block of organized, reusable code that performs a single specific task, in python, we have the inbuilt functions, the user defined functions and lamda function(which is also a type of user ndefined function)
# # # python built-in functions.
# # #built-in functions are functions that come pre-installed with python. you don't need to import any library to use them. They are always available, just like how a phone comes with default apps(calculator, messages, clock). and we have used some of them without even knowing.

# # #common categories of built-in functions 
# # #input and output functions.
# # # displays output print().
# # #takes user input() 
# # # #type conversion functions. 
# # # type conversion functions.
# # # #int(), float(), str(), bool(), list(), dict(), tuple(), set().
# # # mathematical functions 
# # # abs(), #absolute value. 
# # # pow(x,y) #raised to power y.
# # # round() #round numbers to the defined decimal places.
# # # min(), max(), #find smallest/largest.
# # # sequence and collection functions.  
# # #len() #length of a sequence.
# # #sum(), #sum of elements.
# # #sorted(), #sort items,
# # #enumerate() #track index  and value.
# # #utility functions.
# # #type() #shows the type of an object (variables, datatypes, data structures, functions, classes)
# # #id() #returns unique ID of object in memory.
# # # help() #documentation about an object
# # # special built-ins.
# # # range() #generates a sequence of numbers
# # zip() #combines 2 lists element by element.
# # map() #applies a function to all elements in a sequence.
# # filter() #filters elements in a sequence based on condition
# #see examples of use here.
# # #range()
# # for i in range(3):
# #     print(i)
# #zip()
# # names = ["esther","precious","kennie"]
# # scores = [85, 90, 75]
# # for n,s in zip(names, scores):
# #     print(n, "scored", s)

# #     #it's ok, if don't know what lambda is or how use it. I will revisit it.
# # nums =[1,2,3,4]
# # squared = list(map(lambda x: x**2, nums))
# # print(squared)
# # #filter()
# # even_nums = list(filter(lambda x: x% 2==0, nums ))
# # print(even_nums)

# # #student performance and feedback system.
# # #step 1: input student data.
# name1 = input("enter first name: ")
# score1 = int(input("Enter Score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2+ ": "))

# name3 = input("Enter your third name: ")
# score3 = int(input("Enter score for "+ name3 + ": "))

# #step 2: store in lists.
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# #step3: display data.
# print("\nStudent Data:")
# for index, (n,s) in enumerate(zip(names, scores)):
#     print(f"{index+1}. {n} - {s}")

# #step4: summary using built-ins.
# total = sum(scores)
# average = round(total/len(scores), 2)
# highest = max(scores)
# lowest = min(scores)
# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("lowest Score:", lowest)

# # #step 5: ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse = True)
# print(ranked)
# print("\nRanking:")
# # for rank, (score, name) in enumerate(ranked, 1):
    
# #     print(f"{rank}.{name} - {score}")

# # #step 6: check data types.
# # print("\nData Type Checks:")
# # print("Type of names:", type(names))
# # print("Type of scores:", type(scores))
# # print("Type of Scores:", id(names))
# # print("ID of scores list:", id(scores))

# # #step 7: filter passing students (>=50)
# passing = list(filter(lambda s: s>= 50, scores))
# print("\nPassing Scores:", passing)
#what if i want to filter the names of the students who got those scores.

# #step8: map names to uppercase.
# upper_names = list(map(lambda n: n.upper(), names))
# # print("UpperCase Names:", upper_names)

# # #step9: use help() to show documentation of len.
# # print("\nhelp on len():")
# # help(len)


# #user defined function.
# #functions makes our work cleaner, shorter, and easier to manage.
# #def keyword is used in python to define a function.

# #def function_name(takes in input):
# # process block.
# #output block.

# #more explanation.

# # def function_name(input - here, you will insert an item or 
# #                   list of what the function will need to work):

# # "process block - here will contain the logic or what you want the function to do"
# # "output - then here will contain what you want the function to output."
# # "you can either use the "return" keyword or "print()" or yield()

# #defining a function.
# def greet():
#     print("Hello, welcome to AI Fellowship!")

#     #this is how to call a fucntion and it can be called repeatedly.
#     greet()
#     greet()
#     greet()

# #function arguments and parameters.
# #arguments is a placeholder that is inside the function parentheses when defining a function.
# #parameters are the actual values you pass inside the function parentheses when calling the function.
# def greet(name):
#     print("Hello", name, "welcome to python learning!")

# #calling with paramter - the actual name
# greet("class rep")
# greet("ridwan")

# when to use return, print(), yield keywords inside a function.

# a.print()
#  you can use it if you are intrested in displaying your output (not storing.) 
# it does not give back a value you can use later.
# e.g. printing menus, reports, logs. 

# def greet(name):
#     print("hello", name)

# #function call
# result = greet("esther")

# #you will notice it did not store the name.
# print("result:", result)

# b.return
# #you can use it if you want to give it back value,
# return sends a valuee back to the function caller.
# the function ends immediately once it hits return.
# filling a questionnaire and handing it back, the caller now owns the result and can reuse it.
# so you can use return when you need the result for further computation or storage. for example, math calculations, data processing, formatting text.

# def add(a,b):
#     return a+b
# #function call
# result = add(4,6)
# print("the sum is:", result)

#3. yield. this is used for producing a sequence, generators,
# yield works like return, but instead of ending the function, it pauses it and remembers its state.
# next time you call it, it resumes, from where it stopped.
# this creates a generator.
# you can use it when working with large data or infinite sequences.

# def count_up_to(n):
#     i= 1
#     while i<= n:
#         yield i #pause and return i
#         i+= 1
        
        
# #using the generator
# for number in count_up_to(5):
#       print(number)


#       #types of arguments.
#     #positional arguments.
#     #these are the most common and the order matters. values are assigned to the paramters in the same order as they appear.
#     #roll call, line up process.

# def introduce(name, track):
#      print("My name is", name)
#      print("I am learning", track, ".")
#      #function call
# introduce("ngozi", "AI Engineering") #correct order

#      #change the arrangment and watch the output.
# introduce("AI Engineering", "Ngozi") #incorrect order, this will throw a semantic error.

#      #keyword arguments

# #2. keyword arguments
# #here, you explicitly mention the parameter name when calling the function.
# #order doesn't matter, since python kmows which value goes where.
# #think of it like addressing an envelope by name instead of position in line.


def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

#function call
introduce(name= "ngozi", track= "ai engineering")

#change the arrangement and watch the output.
introduce(track = "ai engineering", name = "ngozi") #here you notice that the order does not matter.

#default arguments.
#here you can give parameters a default value.
#even if no value is provided when calling, the default is used.
#think of it like a restaurant menu where rice is served by default if you don't choose otherwise.

def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track,".")

#function call
#without specifying the default argument, but watch the output
introduce("Paul")

#specify the default argument and watch the output
introduce("Tunji Paul", track = "AI Development")

#varying length arguments.
#sometimes we don't know how many arguments will be passed. python provides 2 special symbols(that is nthe asterisk)
#single asterisk for non-keyword arguments or tuples(*args)
#double asterisks for keyword argguments or dictionary(**kwargs)

#a. keyword (tuple)
#- collects extra postional arguments into a tuple.
#think of it like packing extra clothes into a bag.

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("sum:", total)
    #function call
    #take note of the output
    add_numbers(2,4,6)
    add_numbers(10,20,30,40,50)

#keyword argument (dictionary)
# collects extra keyword arguments into a dictionary

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

#function call - take note of the output
student_details(name="peter", track= "AI Engineering", interest = "block chain")

#define student profile function
#ensure to not the order of arrangement of the typpes of argument used.
#this is how to arrange it of you are using everything or some of the together

def participant_profile(name, age, track = "AI DEVELOPMENT", *skills, **extra_info):
    """
    
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    #skills (from *args)
    if skills:
        profile+= "skills: " + ", ".join(skills) + "\n"
    else:
        profile+= "skills: not yet specified\n"
        #extra info (from**kwargs)

    if extra_info:
       profile += "additional info:\n"
       for key, value in extra_info.items():
           profile += f" -{key.capitalize()}:  {value}\n"
    
    
    return profile #do you remeber 'return' and why it is used? we are using it so it can be reused in other places.

 
# #explain each output of the program.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(f"{num1} == {num2}: {num1 == num2}")
# #output1 , displays both values of the given variables  and then compares the result to the second output which,
# #output2  suggests that the first no the user inputed is equal to the second number.
# #explaining the "==" operator in python.

# print(f"{num1} != {num2} : {num1 != num2}")
# #this output suggests that the first no is not equal to the second no. explaining the != operator in python.

# print(f"{num1} > {num2} : {num1>num2}")
# #this output suggests that the first no is greater than the second explaining the greaterthan operator in python.

# print(f"{num1} < {num2} : {num1<num2}")
# #this output suggests that the first no is less than the second no, explaining the less than operator.

#use-cases or scenarios where this program can be applied.

#-The ratio of male to female in AI developers and Engineers.
# -In Sports Betting. Match btw Arsenal and Manutd.
# -In 
#Arsenal vs ManUtd

boluwatife = int(input("how many goals will arsenal score against manutd: "))
tunjipaul = int(input("How many goals will Manutd score arsenal: "))

if boluwatife == tunjipaul:
    print("Arsenal and Manutd Draws")
# else:
#     print("Arsenal Draw Ke!!!")


if boluwatife < tunjipaul:
    print(f"Manutd beats Arsenal by {tunjipaul} goals to {boluwatife}")
# else:
#     print("GGMU!!")

if boluwatife > tunjipaul:
    print(f"Arsenal beats Manutd by {boluwatife} goals to {tunjipaul}")
# else:
#     print("UP GUNNERS!!!")

if boluwatife != tunjipaul:
    print("Over GOALS!!!")
    #it's how to do the over goals and under now. learning for later!!!




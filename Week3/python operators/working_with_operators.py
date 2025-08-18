# #python operators.
# #we have the _comparison, _assignment and logical operators.
# #comparison operators: are used to compare 2 values. The result is always True and False.

# #== equal to
# # #!= not equal to
# # > gretaer than
# # < less than
# # >= greater than or equal to
# # <= less than or equal to.

#e.g.
# a = 10
# b = 20
# # print(a==b) #result is false
# print(a!= b) #result is  true
# print(a>b) #result is false
# print(a<b) #result is true
# print(a>=10) #result is true
# print(b<=25) #True
# #use case example

# score = 75
# print(score >=75) #True
# print(score<50) #False
# print(score==50) #False #N.B: True/False must start with block letter to be recognized in python.

#assignment operators.
# x = 10
# print(x==10)
# print(x)
# x+= 10 #adds 10
# print(x)
# x-= 5 #subtracts 5 from x
# print(x)
# x*= 7 #multiplies x by 7
# print(x)
# x/= 4 #divides x by 5 and gives the value and remainder
# print(x)
# x%= 3 #divides x by 3 but provides only the remainder.
# print(x)
# x=4
# x**= 5 #raises x which is 4 to the power of 5.
# print(x)
# x//= 5 # divides x by 5, floor division
# print(x)

#use case example.

#define variables.

balance = 1000
deposit = 200
withdraw = 500
balance += deposit
balance -= withdraw
print("Updated Balance:", balance) #output = 700.

#logical operators.
#and or not.
x = 10
y= 20
#and operator,
print(x>5 and y >15) #true
print(not(x ==10))
print(x<5 or y>15)

#usecase example1 - scholarship eligibility
#define variables.
age = 17
score = 85
#must be younger than 18 and score above 80.
eligible = (age <18) and (score >80 )
print(eligible)
#event access, usecase example 2.

age = 22
has_ticket = False
can_enter = (age >= 18) and (has_ticket or age < 25)

print(can_enter)
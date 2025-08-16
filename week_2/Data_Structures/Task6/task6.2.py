# task 2 unique name collector
# a program that collects names of people attending a seminar(no duplicates) allowed and displays them in an alphabetical order.
# use input to collect people's names 
name = input("what is your name: ").split()
#convert the list to set.
name_5 = set(name)
#make the set alphabetical with "sorted" function
name_56 = sorted(name_5)
print(name_56)

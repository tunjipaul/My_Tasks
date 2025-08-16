#how to create a list.
#creating an empty list when you don't have elements yet but plan to add later.
#method 1. using square brackets
empty_list = []
print(empty_list) #output: []

#method 2: using the list() constructor
empty_list2 = list()
print(empty_list2) # output: []

#creating a list with initial elements.
#lists can store multiple items separated by commas inside square brackets.

#list of integers.
numbers = [1,2,3,4,5]
print(numbers)

#listofstrings
fruits = ['''apple''', '''banana''', "cherry"]
print(fruits) #output : ['apple' ]

#mixed data types
mixed_list = ["alice", 25, 5.8, True]
print(mixed_list) #output: ["alice", 25, 5.8, True]

#creating a list from another sequence. you can convert strings, tuples, or other iterables into a list.

#from a string (each character becomes an element)
chars =list("hello")
print (chars) #output: ['h', 'e', 'l', 'l', 'o']

#is it possible to convert a variable to list? let's see 

name = "variable"
print(list(name))
#very much possible!

#from a tuple
my_tuple = (10,20,30) 
list_from_tuple = list(my_tuple)
print(list_from_tuple) 
# print(my_tuple, type())

#from a range 
numbers_range = list(range(5))
print(numbers_range)

#creating a list using list comprehension. list comprehensions are a concise way to create lists using a loop in one line. later.

#square of numbers 0-4
squares = [x **2 for x in range(5)]
print(squares) #[0, 1, 4, 9, 16]

#even numbers between 0-10
evens = [x for x in range(11)if x % 2 == 0]
print(evens) #[0,2,4,6,8,10]

#matrix-like list
matrix = [[1,2], [3,4], [5,6]]
print(matrix) #output: [[1,2], [3,4], [5,6]]

#accessing elements in a nested list
print(matrix[0]) #output: [1, 2]
print(matrix[0][1]) #output: 2

#characteristics of a list.
# a list is ordered, meaning it can be indexed.
#allows duplicates, lists can store the same value multiple times.
#mutable lists can be changed. you can modify a list after its created - chnage elements, add new ones, or remove existing ones.
#can contain different data types. - a list can hold integers, srings, floats, booleans, and even other lists.
#can be nested, a list can contain other lists (2D or multi-dimensionational lists)
#dynamic size, it can be chnaged and it moves so you don't need to declare its size before hand.

fruits = ["mango",  "apple", "orange", "apple"]
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[3])
fruits[3] = "grape"
print(fruits)
fruits.append(10)
print(fruits)
print(fruits[0][2])
fruits.append(matrix)
print(fruits)
print(fruits[5][0])
fruits.append(89)
print(fruits)

#list operations 
#concatenation
list1 = [0,1,1,2]
list2 = [4, "3", 5]
result = list1 + list2
print(result) #out put : [0, 1, 1, 2, 4, '3', 5]

#repetition(*)
#repeats elements in a list a given number of times.
nums = [1,2]
list_10 = nums * 3
print(list_10) #output : [1, 2, 1, 2, 1, 2]

#indexing
#accessing elements using their position (starting from 0)
fruits = ["apple", "banana", "cherry"]
print(fruits[0]) #apple
print(fruits[-1]) #cherry because -1, starts counting the elements in the data type from the back.

#slicing - extract a portion of the list.

numbers = [0,1,2,3,4,5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[2:4])
print(numbers[2::])
print(numbers[3:])
print(numbers[:3])
#membership in and not in.
socks = ["white", "black", "yellow"]
print("green" in socks) #false
print("yellow" in socks) #true
#len(), length, counts the number of elements in a list.
items = ["pen", "book", "laptop"] #3
print(len(items))
#min and max (max and min).
integers = [5, 2, 3 ,4 ,6, 7]
print(min(integers)) #2
print(max(integers)) #7
#sum sum(), adds all numerical elements in a list.

numbers5 = [1,2,3,4]
print(sum(numbers5)) #10

#list comprehension, creates a list in a single line.
squares = [x**2 for x in range(5)]
squares_1 = [x**2 for x in range(3)]

print(squares , squares_1)

#copying a list, create a duplicate list.
a = [1, 2, 3]
b = a.copy()
print(b)

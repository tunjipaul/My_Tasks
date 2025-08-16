# tuple, is an ordered, immutable(unchangeable) collection of items in python.
# creating tuples.

# using parentheses()
#example 1: tuple with multiple items.
fruits = ("apple", "banana", "cherry")
print(fruits)

#without parentheses (tuple packing) 
numbers = 1, 2, 3
print(numbers)

# #single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item) 
print(type(single_item))

# #using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

#characteristics of tuples, 
# 1. Ordered – Items have a fixed position.

# 2. Immutable – Cannot change after creation.

# 3. Allow duplicates – Same value can appear multiple times.

# 4. Can contain mixed data types – Strings, integers, lists, etc.

# 5. Can be nested – Tuples inside tuples.

#ordered 
colors = ("red", "green", "blue")
print(colors[0])

#immutable ( uncomment and run. this will cause an error)

# colors[1] = "yellow" #type error

#allow duplicatees
numbers_1 = (1,2,2,3)
print(numbers_1)

#mixed data types 
mixed = ("apple", 3, True, 5.6)

#nested tuples
nested = (("a", "b"), (1,2))
print(nested)

#tuple operations

#indexing

fruits_3 = ("apple", "banana", "cherry")
print(fruits_3[1]) 
print(fruits_3[-1])

#slicing
print(fruits_3[0:2])
print(fruits_3[::-1])

#concatenation
tuple_1 = 1,2
tuple_2 = 3,4
result = tuple_1 + tuple_2
print(result)

#repetition

nums = (1,2)
print(nums * 3)

#membership

fruits_4 = ("apple", "banana", "cherry")
print("banana" in fruits_4)
print("grape" in fruits_4)
print("grape" not in fruits_4)

#iteration
for fruit in fruits_4:
    print(fruit)

    #working with tuples, you can't modify a tuple directly 
    # but you can - convert it to a list, modify it then convert back. 
    # -use built-in functions to work with tuple contents.

    # -unpacking tuples

    person =("john", 25, "nigeria") 
name, age, country = person
print(name)
print(age)
print(country)
#tuples have only 2 mthods, dot count() and dot index()

numbers = (1,2,2,3,4)

print(numbers.count(2)) #2
print(numbers.index(3)) #3

#converting between list and tuple

#tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)

#list back to tuple
t = tuple(lst)
print(t)

#built-in functions with tuples
nums = (4,1,7,3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

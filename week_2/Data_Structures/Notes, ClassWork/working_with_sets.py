#working with sets.

#set is useful when you want to store multiple items but avoid duplicates, they are unordered.

#creating sets. using curly braces.
fruits = {"apple", "banana", "mango"}
print(fruits)

#using the set constructor 

numbers = set([1,2,3,4])
print(numbers)

#creating an empty set (must use set() not {})
empty_set = set()
print(empty_set)

#4 from a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)

#characteristics of sets
# -unordered - no defining sequence or indexing.
# unique elements, duplicates are automatically removed.
#mutable: you can add or remove elements.
#unindexed: you can't access elements using an index like my_set[0]
#supports mathematical set operations like union, intersection, difference, symmetric difference.

#set operations
#adding an element
colors = {"red", "blue"}
colors.add("green")
print(colors)

#removing an element
colors.remove("blue")
colors.discard("yellow")
print(colors)

#pop an element
colors = {"red", "blue", "green"}
removed = colors.pop()
print("removed:", removed)
print("remains:", colors)

#clear a set

colors.clear()
print(colors)

#mathematical set operations
set1 ={1,2,3,4}
set2 = {3,4,5,6}
#union of set
print(set1 | set2)
print(set1.union(set2))

#intersection
print(set1 & set2)
print(set1.intersection(set2))
#3 difference 
print(set1 - set2)
print(set1.difference(set2))

#4symmetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

#working with sets
# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") # Duplicate, ignored automatically
print("Visitors:", visitors)

# Checking if a visitor attended
# (Dont worry if you can't figure this part out yet. We will discuss it properly later in the course.)

name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")
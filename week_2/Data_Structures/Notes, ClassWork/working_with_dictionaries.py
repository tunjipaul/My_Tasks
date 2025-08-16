#creating dictionaries.

#1. using curly braces.
student = { 

    "name": "ada",
    "age" : 20,
    "course": "comp. science"

}
print(student)

#2. using the dict() constructor
student_info = dict(name = "John", age = 25, course = "Maths")
print(student_info)

#3 empty dictionary 
empty_dic = {}
print(empty_dic)

#dictionary comprehension, syntax: {key:value,for item in iterable if condition.}

#create a dictionary of numbers and their squares
squares = {x:x**2 for x in range(1,6)}
print(squares)
square_1 = (x**2 for x in range(0,5))
print(list(square_1))
square_2 = [x**2 for x in range(5)]
print(square_2)

#with condition
#dictionarry of even numbers and their cubes.
evens_cube = {x: x**3 for x in range(1,9) if x % 2 == 0}
print(evens_cube)
#from existing dictionary
students = {"adam": 25, "john": 24, "musa": 45, "jude": 56}
#filter students who passed (score >=50)
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)

#using string keys
names = ["ada", "john", "musa"]
lengths = {name: len(name) for name in names}
print(lengths)

#accessing dictionary items.

#define a dictionary
student = {"name": "ada", "age":20, "course": "comp.science"}
#using key
print(student["name"])
#using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "not found"))

#modifying dictionaries
student["age"] = 21
#change value 
student["grade"] = "A" #Add new key-value pair 
print(student)

#removing items from dictionaries
#1. using pop()
student.pop("age")
print(student)
#using popitem() - removes last inserted key-value
student.popitem()
#using del keyword.
del student["course"]
# #4 using clear(), - removes all items
student.clear()
print(student)
#dictionary methods
#dot keys()
#1. keys()
person = {"name": "emeka", "age": 30}
print(person.keys())
#2.values()
print(person.values())
#3. items()
print(person.items())
#4.update()
person.update({"age": 31, "city": "lagos"})
print(person)

#nested dictionaries

students_2 = {
    "student1": {"name": "ada", "age": 20},
    "student2": {"name": "John", "age": 22}
} 
print(students_2["student1"]["name"]) #access nested data

# looping through dictionaries.
# define a dictionary
students_3 = {
    "name": "ada",
    "age": 20, "course": "comp. science"
}
#loop through keys
for key in students_3:
    print(key)
   #loop through values.
    for values in students_3.values():
        print(values)
        #loop through key-value pairs
        for key, value in students_3.items():
            print(f"{key}: {value}")
            #storing a student's biodata
            student_9 = {
                "name": "chinedu",
                "age": 19,
                "dept": "engineering",
                "subjects": ["maths","physics", "chemistry"],
                "is_full_time": True
            }
            print(f"Name: {student_9['name']}")
            print(f"Subjects: {', '.join(student_9['subjects'])}")
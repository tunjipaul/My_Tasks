# #student bio storage.
# name = input("what is your name: ")
# age = input("how old are you? ")
# gender = input("Gender: ")
# courses = input("Identify your courses: ").split()

# dict["name"] = name
# dict["age"] = age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
courses = input("Enter your courses (separated by commas): ").split(",")

# Store in dictionary
student_bio = {}
student_bio["Name"] = name
student_bio["Age"] = age
student_bio["Gender"] = gender
student_bio["Courses"] = [course.strip() for course in courses] 

print(student_bio)
print(f"\n---Student Bio Data---")
print(f"Name:\t {student_bio['Name']}")
print(f"Age:\t {student_bio['Age']}")
print(f"Gender:\t {student_bio['Gender']}")
print("Courses:")

for course in courses:
    print(f'\t-{course}')
#student bio storage.
name = input("what is your name: ")
age = input("how old are you? ")
gender = input("Gender: ")
courses = input("Identify your courses: ").split()

data = f'name:\nage:\ngender:\ncourses:'
set = f'{name}\n{age}\n{gender}\n{courses}'
student = {
    data:set
}
print(student)
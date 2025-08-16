#task 5, student score tracker
#ask the user for 3 student names.
names = []
scores = []
for i in range(3):
    names.append(input("their names: "))
    scores.append(input("their scores are: "))

print(f"Name - Score")
for i in range(3):
    print(names[i], "-", scores[i])
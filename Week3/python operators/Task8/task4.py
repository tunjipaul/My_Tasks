#student record.
#create empty dictionary
student = { }
#input their name and age.
user_name = input("Enter your name: ").lower().strip()
user_age = int(input("Enter your age: ").strip())

#storing the name and age in the dictionary.
student["name"] = user_name
student["age"] = user_age
#create a list of scores.
user_scores = [70,85,90]
average_scores = sum(user_scores)/len(user_scores)
print(average_scores)

#add the lists of scores to the dictionary.
student["scores"] = user_scores

#check if student has passed with comparison operator.
if average_scores >= 50:
 grade = True
else:
 grade = False

student["Passed"] = grade

if 13 <= user_age <= 19:
 puberty = True
else:
 puberty = False

student["Teenager"] = puberty

print("Student Record: ")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Scores: {user_scores}")
print(f"Passed: {grade}")
print(f"Teenager: {puberty}")
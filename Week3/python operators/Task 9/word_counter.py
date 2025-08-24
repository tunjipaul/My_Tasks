user_name = []
scores = []

for char in range(3):
   user_name.append(input("What are your names: "))
   scores.append(input("the scores: "))

for char in range(3):
 print(f"{user_name[char]} - {scores[char]}")
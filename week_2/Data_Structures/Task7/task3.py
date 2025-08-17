days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(days)
activity_1 = input("What are you doing on Monday: ")
activity_2 = input("What are you doing on Tuesday: ")
activity_3 = input("What are you doing on Wednesday: ")
activities = [activity_1,activity_2,activity_3]
# Use dictionary comprehension 
# {name: len(name) for name in set_of_names}.

day_activity = {
day: activity for day, activity in zip(days, activities)

}
print(day_activity)
#this is interesting. can this be done without the use of zip? i guess using loops?

#task 1, create and display
# dish_1 = input("Favorite dish 1: ")
# dish_2 = input("favorite dish 2: ")
# dish_3 = input("favorite dish 3: ")

# first_tuple = (dish_1,  dish_2, dish_3)
# print(first_tuple)

# print(f"your food choices are: \n{dish_1}\n{dish_2}\n{dish_3} ")

#task 2, tuple and input

# user_name = input("names of your friends without commas: ") .split()
# friends = tuple(user_name)
# print(friends)
# reverse_friends = friends[::-1]
# print(reverse_friends)

#task 3
# user_states = input("enter your preferred states: ").split()
# state_tuple = tuple(user_states)
# print(state_tuple)
# print(state_tuple[0])
# print(state_tuple[4])
# print("lagos" in state_tuple)
# state_tuple_length = len(state_tuple)
# print(state_tuple_length)

# #task4, tuple unpacking.
# user_info_name = input("firstname: ")
# user_info_age = input("age: ")
# user_info_color = input("fav. color: ")
# user_info_home_town = input("home_town: ")
# tuple_info = (user_info_name, user_info_age, user_info_color, user_info_home_town)

# name, age, color, home_town = tuple_info
# print(f"here is your info:\n{name}\n{age}\n{color}\n{home_town}")

#task 5, modify tuple indirectly.
# shopping_list = input("enter 3 items for your list: ").split()
# list_convert_shopping_list = list(shopping_list)
# print(list_convert_shopping_list)
# added_items = input("add 2 more items: ").split()
# print(added_items)
# new_list = (list_convert_shopping_list + added_items)
# print(new_list)
# tupled_new_list = tuple(new_list)
# print(tupled_new_list)
# print("|".join(tupled_new_list))

#task 6. attendace tracker.

# days_of_the_week = input("days of the week: ").split()
# tuple_days_of_the_week = tuple(days_of_the_week)
# months_of_the_year = input("Months of the year: ").split()
# tuple_months_of_the_year = tuple(months_of_the_year)
# student_name = input("enter full name: ")
# gender = input("your gender: ")
# course_track = input("course track: ")
# info = (f"{student_name, gender, course_track,tuple_months_of_the_year,tuple_days_of_the_week}")
# current_month = tuple_months_of_the_year[info[3]]
# current_day = tuple_days_of_the_week[info[4]]

# print(f"find attached the required info: \n{student_name}\n{gender}\n{course_track}\n{current_month}\n{current_day}")

days_of_the_week = ("Mon","Tue", "Wed", "Thur", " Fri", "Sat", "Sun")
months_of_the_year = ("Jan", "Feb" , "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec") 
info_1 = input("Student's Name: ")
info_2 = input("Gender: ")
info_3 = input("Course Track: ")
info_4 = input("Current Month No: ")
info_5 = input("Current Day No: ")

vim = print(f"{info_1} who is {info_2} is in {info_3} marked today on {info_4}/{info_5} ")
print(vim)
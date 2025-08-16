# #task4, tuple unpacking.
user_info_name = input("firstname: ")
user_info_age = input("age: ")
user_info_color = input("fav. color: ")
user_info_home_town = input("home_town: ")
tuple_info = (user_info_name, user_info_age, user_info_color, user_info_home_town)

name, age, color, home_town = tuple_info
print(f"here is your info:\n{name}\n{age}\n{color}\n{home_town}")

#contact quick lookup.
names = ("Paul", "Tunji", "Kenny")

phone_nums = ("07015512567", "07084547118", "09019978821")

name_num = dict(zip([name.lower() for name in names], phone_nums))
print(name_num)

user_name = input("What is your name? ").lower()

#retrieve ooo with .get(), jut learning loops and then this yikes.

confirmation = name_num.get(user_name, "Error!!!Number not found!!!")

print(confirmation)



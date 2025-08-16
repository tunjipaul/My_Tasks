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
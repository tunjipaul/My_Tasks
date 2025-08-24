# # # # 9. Ask the user to enter a sentence and print the number of vowels in it.

sentence = input("give me a sentence: ").strip()
count = 0

for every_character in sentence:
   
   if every_character in "aAeEiIoOuU":
        print(every_character)
        count += 1

print("No of Vowels: ", count)






# days_of_the_week = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
# months_of_the_year = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec")
# user_data = input("Your Name: ")
# gender = input("Sex:" )
# course = input("Course Track:" )
# current_month = int(input("What is this current month: "))
# current_day = int(input("What is today's date: "))

# print(f"Hello {user_data}, your gender is {gender}, your course is {course} and attendance has been marked for {days_of_the_week[current_day]}/{months_of_the_year[current_month - 1]},2025")

# seat_numbers = set(range(1,51))
# # print(seat_numbers)
# booking_number = input("pick a seat no: ")
# removed_seats = seat_numbers.pop(booking_number)
# if removed_seats in booking_number:
#     print("Seat already booked pick another number")
# else:
#     print("Thank you for booking")
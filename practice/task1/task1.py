# # # # collecting user details

# # # #ask the user for their first name and age, print a welcome message using f-string.

# # # user_name = input("what is your first name: ").strip().lower()
# # # user_age = int(input("what is your age: ").strip().lower()) 

# # # print(f"Welcome {user_name}, you are {user_age} years old.")

# # # user_details = {
# # #     "name": input("what is your first name: ").strip().lower(),
# # #      "age" : int(input("how old are you: ").strip().lower())
# # # }

# # # print(f"Welcome {user_details['name']}, you are {user_details['age']} years old.")

# # # # did this using 2 different ways, the normal conventional method(which involves using ) and using dictionaries

# # #price display with typecasting
# # #type casting involves conversion between data types.


# # # ask the user for the price of garri per paint in naira (as a string) and convert it to float.
# # #     display the message showing the amount in naira and kobo using print().

# # # price_of_garri = float(input("what is the price of garri: ").strip())

# # # print("Price of Garri per Paint:\n")
# # # print(f"The price of garri is N{price_of_garri:,.2f}K")

# # # #SCHOOL REGISTRATION FORM.
# # # ASK FOR STUDENTS NAME, CLASS, AND STATE OF ORIGIN , USE STRING CONCAT TO PRINT IN ONE SENTENCE.

# # students_details = {
# #     "name": input("what is your name: ").strip().lower(),
# #     "class": input("what class are you in: ").strip().lower(),
# #     "state_of_origin": input("what state do you hail from: ").strip().lower()
# # }

# # print("Student " + students_details["name"] + " is in " + students_details["class"] + " and is from " + students_details["state_of_origin"] + " state")


# #escape sequence.

# #ask for the name of a nigerian dish and the state it is popular in. print the result in 2 lines and add a tab space before the state name using \t

# # question ={
# #     "name_of_dish": input("What is your favorite dish: ").strip().lower(),
# #     "dish_state": input("what state is it most eaten: ").strip().lower()
# # }

# # print("FAVORITE NIGERIAN DISH:\t", "STATE LOCATED")
# # print(question["name_of_dish"],"\t\t\t", question["dish_state"])

# # #daily market report
# # daily_market_report = {
# #     "market_name": input("which market we dey: ").strip().lower(),
# #     "no_of_trader": int(input("how many traders dey here: ").strip().lower()),
# #     "daily_revenue": int(input("what is their daily revenue: ").strip().lower())
# # }

# # print(f"the daily revenue for {daily_market_report['market_name']} market with {daily_market_report['no_of_trader']} traders is N{daily_market_report['daily_revenue']:,.2f}K")

# #electricity bill formatter.
# bill = {
#     "full_name": input("what is your full name: ").strip().lower(),
#     "units_consumed": int(input("how many units consumed: ").strip().lower()),
#     "cost_per_unit": float(input("how much cost per unit: ").strip().lower())
# }

# total_bill = bill["units_consumed"] * bill["cost_per_unit"]

# print("Electricity Bill Formatter:")
# print(f"Customer's Name: {bill['full_name']}")
# print("-" * 30)
# print(f"Totalbill:\tN{total_bill:,.2f}K")

#mixing data types. #ask the user for: 
#yourage: int.
#your height in meters - float.
#your name - string.

# #transport fare calculator
# transport_fare ={
#     "distance": float(input("how far did you go: ").strip()),
#     "fare": float(input("how much per distance: ").strip())
# }

# total_transport_fare = transport_fare["distance"] * transport_fare["fare"]


# print(f"your transport fare is N{total_transport_fare:,.2f}K")

# #nigeria festival info.
# festival_info ={
# "festival ":input("what is the festival name: ").strip(),
# "location_festival": input("location of festival: ").strip(),
# "month_held": input("what month was it held: ").strip()
# }


# print(f"the '{festival_info['festival ']}\' festival is held at {festival_info['location_festival']} on {festival_info['month_held']} every year.")

#school fees breakdown.

# school_fees_breakdown = {
#     "school_name": input("what is the name of your school: ").strip(),
#     "tuition_fee": float(input("what is the tuition fee: ").strip()),
#     "hostel_fee": float(input("hostel fee price is what: ").strip()),
#     "feeding fee": float(input("how much is feeding fee: ").strip())
# }

# total_school_fees = school_fees_breakdown["tuition_fee"] + school_fees_breakdown["hostel_fee"] + school_fees_breakdown["feeding fee"]

# print(f"Total School Fee for Students at {school_fees_breakdown['school_name']} high school: ")
# print("-" * 40)
# print(f"Tuition Fee: N{school_fees_breakdown['tuition_fee']:,.2f}K")
# print(f"Hostel Fee: N{school_fees_breakdown['hostel_fee']:,.2f}K")
# print(f"Feeding Fee: N{school_fees_breakdown['feeding fee']:,.2f}K")

#nigerian currency converter (advanced)

# nigerian_currency_converter ={
#     "amount_in_naira": float(input("amount in naira: ")),
#     "exchange_rate_in_dollars": float(input("what is your exchange rate for dollars: ")),
#     "exchange_rate_in_pounds": float(input("what is your exchange rate for pounds: "))
# }
# amount_in_dollars = nigerian_currency_converter["amount_in_naira"]/nigerian_currency_converter["exchange_rate_in_dollars"]
# amount_in_pounds = nigerian_currency_converter["amount_in_naira"]/nigerian_currency_converter["exchange_rate_in_pounds"]

# print("NIGERIAN CURRENCY CONVERTER:")
# print("-" * 40)
# print(f"Amount in Naira: N{nigerian_currency_converter['amount_in_naira']:,.2f}K")
# print(f"Amount in Dollars: ${amount_in_dollars:,.2f}")
# print(f"Amount in pounds: E{amount_in_pounds:,.2f}")


#simulated ussd menu interaction.

user_program = ()
# Simulated USSD Menu Interaction
print("This is Task 12")
print("Welcome to your mobile service network!")

code = input("Please dial a USSD code to begin (e.g., *345#): ")

print("\nWelcome to the USSD service menu.")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")

user_option = input("Enter your choice (1, 2, or 3): ")

if user_option == "1":
    print(f"\nThank you for choosing Option 1: Check Balance.")
    print("Your balance inquiry is being processed. You will receive an SMS shortly.")
elif user_option == "2":
    print(f"\nThank you for choosing Option 2: Buy Airtime.")
    credit_balance = float(input("Enter the amount of airtime to buy: "))
    print(f"\nTransaction complete. You have successfully purchased ₦{credit_balance:,.2f} of airtime.")
elif user_option == "3":
    print(f"\nThank you for choosing Option 3: Buy Data.")
    data_needed = float(input("Enter the amount of data to buy (in GB): "))
    print(f"\nTransaction complete. You have successfully purchased {data_needed:,.2f}GB of data.")
else:
    print("\nInvalid option selected. Please try again.")

print("\nThank you for using our service!")
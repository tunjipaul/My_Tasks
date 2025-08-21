#simulated ussd menu interaction.

#design a mock ussd interface and overlap with control structures.

#user runs the program and it displays a welcome screen with a nigerian context greeting.
name = input("What is your name? ").lower().strip()
greeting = print(f"{name}, you're welcome to OTP USSD System!")
user_code = input("Dial the code *007# to proceed: ").strip()

balance = 100000
while True:
    if user_code == "*007#":
         option = int(input("OTP USSD PLATFORM!\n-Choose an option below.\n1.Check Balance\n2.Buy Airtime\n3.Buy Data\n4.Exit: ").strip())
         if option == 1:
             print(f"{name} your bank balance is N{balance:,.2f}")
             
         if option == 2:
             price = int(input("How much airtime do you want to buy: ").strip())
             if price <= balance:
                 balance -= price
                 print(f"Thank you for buying airtime. Your airtime is N{price:,.2f} and balance is N{balance:,.2f}.")
             else:
                 print('Insufficient Funds')
                             
         if option == 3:
             data = int(input("How much data do you want to buy: ").strip())
             if data <= balance:
                 balance -= data
                 print(f"Your data balance is {data}mb and Bank Balance is {balance:,.2f}")
             else:
                 print("Insufficient Funds")
                 
         if option == 4:
             print(f"Thank you for banking with us {name}.")
             break
    else:
     print("Invalid Code. Try again")
     break
     

# print("")
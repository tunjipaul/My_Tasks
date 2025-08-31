#simulated ussd menu interaction.

#design a mock ussd interface and overlap with control structures.

#user runs the program and it displays a welcome screen with a nigerian context greeting.
name = input("What is your name? ").lower().strip()
greeting = print(f"{name}, you're welcome to OTP USSD System!")
user_code = input("Dial the code *007# to proceed: ").strip()

balance = 100000
while True:
    if user_code == "*007#":
         option = int(input("OTP USSD PLATFORM!\n-Choose an option below.\n1.Check Balance\n2.Buy Airtime\n3.Buy Data\n4.Exit\nInput No: ").strip())
         if option == 1:
             print(f"{name} your bank balance is N{balance:,.2f}")
             break
             
         if option == 2:
             price = int(input("How much airtime do you want to buy: ").strip())
             if price <= balance:
                 balance -= price
                 print(f"Thank you for buying airtime. Your airtime is N{price:,.2f} and bank balance is N{balance:,.2f}.")
             else:
                 print('Insufficient Funds')
                             
         if option == 3:
            # data_plan = int(input("Select your preferred data plan:\n1.Daily\n2.Weekly\n3.Monthly\nInput No: ").strip())
            # # if data_plan == 1:
            # #     daily = int(input("1.N100 for 100mb, 1 day.\n2.N200 for 200mb, 2 days.\n3.1000 for 3.2GB, 3 days\nInput no: ").strip())
            # #     if daily == 1:
                    data = int(input("How much data do you want to buy: ").strip())
                    if data == 100:
                        if data <= balance:
                         balance -= data
                        print(f"Your data balance is {data:,.2f}mb and Bank Balance is N{balance:,.2f}")
                    # elif data == 200:
                    #  if data <= balance:
                    #     balance -= data
                    print(f"Your data balance is {data:,.2f}mb and Bank Balance is N{balance:,.2f}")
                    #  elif data == 300:
                    #     if data<= balance:
                    #        balance -= data
         else:
                        print("Insufficient Funds")
                    
            
            
            # weekly = int(input("1.N500 for 1.5GB, 7 days.\n2.N1000 for 3GB, 7 days.\n3.N2000 for 6GB for 14days: ").strip())
            # monthly = int(input("1.N5000 for 10GB, 1 month.\n2.1N0000 for 23GB, 1month.\n3.N20000 for 36GB, 2 months: ").strip())
            
            
                 
         if option == 4:
             print(f"Thank you for banking with us {name}.")
             break
    else:
     print("Invalid Code. Try again")
     break
     
#not done with this code!!! #i'm tired.

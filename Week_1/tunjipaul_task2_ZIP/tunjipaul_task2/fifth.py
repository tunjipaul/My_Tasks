#daily market report
market_name = input("marketname: ")
no_of_traders = int(input("no_of traders: "))
daily_revenue = int(input("daily_revenue: "))
answer = f"the daily market report for {market_name} for {no_of_traders: ,} traders as at {2024} is ₦{daily_revenue:,.2f}  "

print(answer)
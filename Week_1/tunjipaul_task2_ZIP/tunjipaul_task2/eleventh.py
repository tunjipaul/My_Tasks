#advanced nigerian currency converter 

amount_in_naira = float(input("Input the naira amount ₦: "))
exchange_rate_in_dollars = float(input("Input the dollars exchange rate $: "))
exchange_rate_in_pounds = float(input(f"Input the pounds exchange rate £: "))

amount_in_dollars = amount_in_naira/exchange_rate_in_dollars

amount_in_pounds = amount_in_naira/exchange_rate_in_pounds

print(f"Amount in naira is:\t₦{amount_in_naira:,.2f}\nAmount in dollars is:\t${amount_in_dollars:,.2f}\nAmount in pounds is:\t£{amount_in_pounds:,.2f}")

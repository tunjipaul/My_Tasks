#electricity bill formatter
#take the customer full name.
customer_full_name = input("what is your name: ")
#total bill is the product of the units consumed and the unit cost
units_consumed = int(input("how many units did you consume: "))
unit_cost = float(input("what is the cost per unit? "))
total_bill = unit_cost * units_consumed
#final result
result = print(f"hello {customer_full_name},\tyour bill is\t{total_bill: ,.2f}")
print(result)
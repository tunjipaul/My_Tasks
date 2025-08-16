#transport fare calculator
distance_in_km =  int(input("how long is the journey: "))
fare_per_km = int(input("how much for the journey "))

total_fare = distance_in_km * fare_per_km

display = print(f"the price to go from fajol to kobape is N{total_fare:,.2f}K")

print(display)
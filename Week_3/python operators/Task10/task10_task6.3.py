seat = set(range(1,51))
print(seat)
try:

 booking_seat = int(input("Book a seat: "))

 removed_seats = seat.discard(booking_seat)

finally:
 print(f"Remaining Seats: {seat}")
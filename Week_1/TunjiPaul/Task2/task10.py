#schoolfees breakdown

school_name = input("What is your school name? ")
tuition_fee = float(input("what's the tuition fee? "))
hostel_fee = float(input("what is your hostel fee? ")) 
feeding_fee = float(input("what is your feeding fee? "))
total_breakdown = tuition_fee + hostel_fee + feeding_fee

print(f"Here is the school fees breakdown for {school_name}\nSchool Fee:\t{tuition_fee:,.2f}\nHostel Fee:\t{hostel_fee:,.2f}\nFeeding Fee:\t{feeding_fee:,.2f}\n----------------------------\nTOTAL FEE:\t{total_breakdown:,.2f}\n----------------------------")

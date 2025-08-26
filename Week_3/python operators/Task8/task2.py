#task2.

#federal government scholarship key eligibity requirements:
print("Federal Government Scholarship Application for Science Students.")
print(f"-"*65)
name = input("Enter your name: ")
citizenship = input("Are you a nigerian citizen: Yes/No: ")
enrollment_status = input("Are you a full-time undergraduate student in a recognized Nigerian university(Yes/No): ")
scholarship_status = input("Are you a recipient of other scholarships from entities in the oil and gas industry, whether national or international(Yes/No): ").lower().strip()
results = {
    "Biology": input("Grade for Biology -(A,B,C,D,E,F): ").upper(),
    "Physics" : input("Grade for Physics -(A,B,C,D,E,F): ").upper(),
    "Chemistry" :input("Grade for Chemistry -(A,B,C,D,E,F): ").upper(),
    "Mathematics": input("Grade for Mathematics -(A,B,C,D,E,F): ").upper(),
    "English": input("Grade for English -(A,B,C,D,E,F): ").upper(),
    "FurtherMaths": input("Grade for F/Maths -(A,B,C,D,E,F): ").upper(),
    "Geography": input("Grade for Geography -(A,B,C,D,E,F): ").upper(),
    "Civic Education":input("Grade for Civic -(A,B,C,D,E,F): ").upper(),
    "Catering Craft Practice": input("Grade for CCP -(A,B,C,D,E,F): ").upper()
}
maths_required = (results["Mathematics"].upper().strip() == "A") or (results["Mathematics"].upper().strip() == "B")
english_required = (results["English"].upper().strip() == "A") or (results["English"].upper().strip() == "B")
citizenship_eligibility = citizenship.upper().strip() == "YES"
enrollment_status_eligibity = enrollment_status.upper().strip() == "YES"
distinctions_eligible = (list(results.values()).count("A") + list(results.values()).count("B")) >= 5
scholarship_status_eligible = scholarship_status == "no"

all_eligibility = (maths_required and english_required and citizenship_eligibility and enrollment_status_eligibity and distinctions_eligible and scholarship_status_eligible)
print('\n\t\t --- RESULTS --- \n')
print(f"Country Eligibility: {citizenship_eligibility}")
print(f"Enrollment Status Eligibility: {enrollment_status_eligibity}")
print(f"Student on Other Schorlarships: {scholarship_status_eligible}")
print(f"Passed Maths: {maths_required}")
print(f"Passed Enlish: {english_required}")
print(f"Number of Distinctions: {distinctions_eligible}")
if all_eligibility == True:
    print("Eligible")
else:
    print("Not Eligible")
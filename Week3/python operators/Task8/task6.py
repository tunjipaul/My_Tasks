#UNILAG ADMISSION ELIGIBILITY CRITERIA.

#To be eligible for PUTME screening, jamb score must be at least 200. that is, >= 200.
#Jamb Score >= 200.
#ask aspirant for the ff details.
utme_score = int(input("What is your JAMB/UTME score? ").strip())
Olevel_sitting = int(input("How many results are you using:1/2 ").strip())
Olevel_Results = {
    "Biology": input("Grade for Biology --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "Physics" : input("Grade for Physics --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "Chemistry" :input("Grade for Chemistry --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "Mathematics": input("Grade for Mathematics --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "English": input("Grade for English --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "FurtherMaths": input("Grade for F/Maths --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "Geography": input("Grade for Geography --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "Civic Education":input("Grade for Civic --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower(),
    "Catering Craft Practice": input("Grade for CCP --(A1,B2,B3,C4,C5,C6,D7,E8,F9): ").lower()
}


putme = input("Did you partake in the putme exercise:Yes/No ").lower().strip()
departmental_cutoff_score = int(input("What is your cut-off mark ").strip())

if 200 <=departmental_cutoff_score >= 320:
    cutoff = True
else:
    cutoff = False

if utme_score >= 200:
    jamb_score = True
else:
    jamb_score = False

if Olevel_sitting == 1:
    Olevels = True
else:
    Olevels = False

passed_maths = (Olevel_Results["Mathematics"].lower().strip() == "a1") or (Olevel_Results["Mathematics"].lower().strip() == "b2") or (Olevel_Results["Mathematics"].lower().strip() == "c3") or (Olevel_Results["Mathematics"].lower().strip() == "c4") or (Olevel_Results["Mathematics"].lower().strip() == "c5") or (Olevel_Results["Mathematics"].lower().strip() == "c6")
passed_english = (Olevel_Results["English"].lower().strip() == "a1") or (Olevel_Results["English"].lower().strip() == "b2") or (Olevel_Results["English"].lower().strip() == "c3") or (Olevel_Results["English"].lower().strip() == "c4") or (Olevel_Results["English"].lower().strip() == "c5") or (Olevel_Results["English"].lower().strip() == "c6")
if putme == "yes":
    post_Jamb = True
else:
    post_Jamb = False

distinctions_eligible = (list(Olevel_Results.values()).count("a1") + list(Olevel_Results.values()).count("b2") + list(Olevel_Results.values()).count("b3") + list(Olevel_Results.values()).count("c4") + list(Olevel_Results.values()).count("c5") + list(Olevel_Results.values()).count("c6")) >= 5

final_admissions = (post_Jamb and distinctions_eligible and Olevels and passed_english and passed_maths and jamb_score and cutoff)
print("UNILAG ADMISSION ELIGIBILITY CRITERIA.")
print(f"Cutoff: {cutoff}")
print(f"Jamb: {jamb_score}")
print(f"WAEC: {Olevels}")
print(f"English: {passed_english}")
print(f"Maths: {passed_maths}")
print(f"PUTME: {post_Jamb}")
print(f"Distinctions: {distinctions_eligible}")
print(f"Eligibility: {final_admissions}")

#i'm proud of me!!!!!!!!!!!
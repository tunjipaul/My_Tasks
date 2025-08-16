print
#TASK 1 - A PYTHON PROGRAM THAT PRINTS THE FOLLOWING INFORMATION ON SEPARATE LINES.
#FULL NAME
print("Documenting my personal information: \n\n1. MY NAME IS OGOR PAUL OLATUNJI\n2. UNIVERSITY - FUNAAB\n3. LGA - ODEDA\n4. FAV. Food - Egusi with Pounded Yam\n")


#TASK 2 - A PYTHON PROGRAM THAT STORES YOUR NAME AND STATE OF ORIGIN IN VARIABLES AND PRINTS A MESSAGE.

#variables

name = "TunjiPaul"
state_of_origin = "Delta State."

#final result combining variables and strings
print( name + " originates from " + state_of_origin + "\n")

#TASK 3 - SIMPLE TIMETABLE IN A NIGERIAN SECONDARY SCHOOL USING TAB SPACING AND NEW LINES

print("JSS2 TIMETABLE - FEDERAL GOVERNMENT COLLEGE (SAMPLE) \n")

#create a variable and store all the parameters for time and the days of the week.
# time = "8:00-8:40\n8:40-9:20\n9:20-10:00\n10:00-10:20\n10:20-11:00\n11:00-11:40\n11:40-12:20\n12:20-1:00\n1:00-1:40\n1:40-2:20"

# monday = "ENG\nMATHS\nB.Science\nShort Break\nSOS\nAgric.\nB.Studies\nLunch\nCRS\nCOMP."
#using tabspacing and new line code 
print("TIME\t\tMON\t\tTUES\t\tWED\t\tTHUR\t\tFRI\n8:00-8:40\tENG\t\tB.Science\tSOS\t\tMaths\t\tENG.\n8:40-9:20\tMATHS\t\tB.Science\tMaths\t\tENG.\t\tAgric.\n9:20–10:00\tB.Science\tCivic\t\tB.Science\tB.Studies\tMaths\n10:00-10:20\tSHB\t\tSHB\t\tSHB\t\tSHB\t\tSHB\n10:20-11:00\tSOS\t\tENG.\t\tAgric.\t\tCivic\t\tCOMP.\n11:00-11:40\tAgric.\t\tCOMP.\t\tENG\t\tB.science\tSOS\n11:40-12:20\tB.Studies\tAgric.\t\tCRS.\t\tSOS\t\tB.Science\n12:20-1:00\tLunch\t\tLunch\t\tLunch\t\tLunch\t\tLunch\n1:00-1:40\tCRS\t\tB.Studies\tFineArts\tAgric.\t\tCivic\n1:40-2:20\tCOMP.\t\tPHE\t\tB.Studies\tPHE\t\tFineArts\n")

#TASK 4 - python program to store my personal information

#create variables
fullName = "OGOR PAUL OLATUNJI"
level = "graduate"
bestCourse = "Engineering Law."

#result with f- string(formatted)
print(f"My name is {fullName},I'm a {level} and my best course is {bestCourse}" )

#Task5 Write a short 3-line poem about Nigeria and print it using triple quotes
print("""
      A nation guided by chaos, ruled by the worst of us. 
      she is etched in corruption, drenched in barbarism. 
      Nigeria who can save? 
       """)
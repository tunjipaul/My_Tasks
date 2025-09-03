# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"step 1: creating student object...")
#         self.name = name 
#         self.state_of_origin = state
#         self.course = course 
#         self.student_id = self.generate_id()
#         print(f"step 6: {self.name} from {self.state_of_origin} is ready!")
        
#     def generate_id(self):
#         import random
#         return f'unisail{random.randint(1000, 9999)}'
    
# #creating an object , here is what happens:
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")

# print(ayo.name)
# print(ayo.student_id)


# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network 
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")
    
#     def buy_airtime(self, amount):
#         self.airtime += amount #self ensures it goes to the RIGHT person.
#         return f"{self.name} now has ₦{self.airtime} airtime"
    

# #creating multiple users.
# abeeb = PhoneUser("abeeb bakare", "mtn")
# onisemo = PhoneUser("onisemo williams", "airtel")

# #each person's actions affect only their own account.
# print(abeeb.buy_airtime(500)) #tunde now has #500 airtime.
# print(onisemo.buy_airtime(1000)) #blessing now has #1000 airtime
# print(abeeb.airtime) #tunde's airtime.
# print(onisemo.airtime) #onisemo's airtime

#key rules. 
#1. init always takes self as first parameter.
#2. all methods take self as first parameter.
#3. never pass self manually when calling methods.
#4. use self inside methods  to access object's attributes.
#5. self refers to the specific object being used.

#attributes are the characteristics, properties that describe an object, answering the question, what does this object look like, or what information does this object store.

#real-world analogy
#think of a nigerian national ID Card.

# me:  adebayo tosin
# age : 28
# state of origin : lagos
# lga: "ikeja"
#occupation: software developer, these only describe the person not what the person can do.

# #defining attributes of a student.
# class student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0

# #creating a student object
# fathia = student("fathia abdul", "biochemistry", 300, "ogun state")

# #accessing attributes of objects.
# print(fathia.name)
# print(fathia.course)
# print(fathia.state_of_origin)
# print(fathia.level)
# print(fathia.cgpa)

# #type of attributes.
# #instance attributes - unique to each object

# student1 = student("anthony johnson", "engineering", 200, "ogun")
# student2 = student("fadilat hassan", "medicine", 400, "lagos")

# print(student1.name)
# print(student2.name)

#class attributes - shared by all objects of the class.
class student:
    university = "federal university of agriculture, abeokuta."

    def __init__(self, name, course):
        self.name = name
        self.course = course
    

student1 = student("anthony johnson", "engineering")
student2 = student("fadilat hassan", "medicine")

print(student.university)
print(student1.university)
print(student2.university)


#methods --- the actions, what objects can do, not what they are.
#they define what an object can do.
#think of what a nigerian student can do.

#study, #writeexam, #payschoolfees, #registercourses, #attendlectures.

class student:
    def __init__(self, name, course, level):
        #attributes
        self.name = name 
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False

    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    #method: another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
        
        #method: calculates CGPA
    def calculate_cgpa(self, grades):
       if grades:
           self.cgpa = sum(grades) / len(grades)
           return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
       else:
        return "no grades provided"
    

#using methods 
abiodun = student("abiodun akinola", "gistology", 600)
print(abiodun.pay_school_fees())
print(abiodun.register_courses())
print(abiodun.calculate_cgpa(grades= [4.2, 3.8, 4.0, 4.52]))

#types of methods.
#instance methods - work with specific data objects.

#self refers to the specific student.
def pay_school_fees(self):
    return f"{self.name} has paid school fees"

#2. class methods - work with class-level data.
@classmethod
def get_university(cls):
    return cls.university


#3. static methods - don't need object or class data.
@staticmethod
def academic_calendar():
    return "academic session runs from september to july"

#how attributes and methods work together.

#- the relationship
#attributes store the data.
#methods use and modify that data.

class BankAccount:
    def __init__(self, owner, bank_name, balance = 0):
        #attributes, what the account has
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
        #methods - what the account can do
    def deposit(self, amount):
            """add money to the account"""
            if amount > 0:
                self.balance += amount #method changes attribute
                return f"N{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: N{self.balance:,}"
            return "Invalid deposit amount"
    def withdraw(self, amount):
            """Remove money from the account"""
            if amount > 0 and amount <= self.balance:
                self.balance -= amount #method changes attribute
                return f"N{amount:,} withdrawn from {self.owner}'s account. New balance: N{self.balance:,}"
            return "insufficient funds or invalid amount"
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"N{amount:,} transferred from {self.owner} to {recipient}. Remaining Balance: N{self.balance:,}"
        return "Transfer Failed: Insufficient Funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: N{self.balance:,}"
    
    def generate_account_number(self):
        """generate a unique account number"""
        import random
        return f"01{random.randint(10000000,99999999)}"

    
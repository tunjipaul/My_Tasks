import first
import second

#lets use the functions in the first.py file.

print("=== Math Functions ===")
print("5+3 =", first.add(5,3))
print("10-4=", first.subtract(10,4))
print("6*7=", first.multiply(6,7))
print("20/5 =", first.divide(20,5))

#let us use the functions in the second.py file.

print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'python'=", second.reverse_string("python"))
print("character count in sentence =", second.count_characters("python modules are powerful"))
print("word count in sentence =", second.count_words("python modules are powerful"))


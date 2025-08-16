#upper()
name = "ada balogun"
print(name.upper())
#lower()
sentence = "python is amazing"
print(sentence.lower())
#strip 
text = "   Abuja  "
print(text.strip())
print(text)

#replace()
message = "I love Java"
print(message.replace("Java", "boluwatife"))
# swapcase()
text = "hello abeokuta"
print(text.swapcase())
#lstrip
text2 = " Nigeria  "
text3 = "Nigeria   "
#the difference between the lstrip and strip is that the lstrip only clears it from the left
print(text2.lstrip())
print(text3.rstrip())

#using split to create a string into a list using separators
fruit ="mango orange banana"
print(fruit.split())

#using rsplit to create a string into a list using separators.
text4 = "one, two, three, four"
print(text4.rsplit(",",2))

lines = "line1\nline2\nline 3"
print(lines.splitlines())
 
 #joins a list of strings into one string with a specified separator

words = ["I", "love", "python"]
print(" ".join(words))

#center, centers the string within a specified width, padding with spaces or characters.
text = "python"
print(text.center(20, "-"))

#ljust, left aligns the string within a specified width, padding with spaces or characters.

text5 = "python"
print(text5.ljust(10, "*"))

#rjust, right aligns the string within a specified width, padding with spaces or characters.
text6 = "python"
print(text.rjust(10, "*"))

#zfill, pads a numeric string on the left with zeros until it reaches a given length.
num = "4332"
print(num.zfill(6))
 
#isalpha, checks if the string contains only letters

print("lagos".isalpha()) 
print("lagos123".isalpha())

#isdigit() checks if the strings contains only digits

print("12345".isdigit())
print("123a".isdigit())

#isalnum(), checks if the string contains only letters and digits.

print("python3".isalnum())
print("python 3".isalnum())
print("55")
#strings in python

#single quotes
name = 'ada'
#double quotes
greeting = "hello"
#triple quotes( for multi-line strings)
story = '''once upon a time, 

there was a coder named ada.'''
#string with numbers and symbols 
password = "p@ssword123"

print(name, password, greeting, story)

#using double quotes won't allow the system to output the result on a new line without "/n", so triple quotes allows you to write on a new line without the "/n" escape sequence
# storyy = " once upon a time, " \
# "there was a coder named ada"
# print(storyy)

#indexing
word = "python"
print(word[0]) #p
print(word[-2]) #o
print(word[-1]) #n
#the negative signs allows the system to count the variables character from the back. and python start counting from 0.

#slicing

word = "python"

print(word[0:4]) #pyth
#starts counting 4 characters from the front
print(word[2:]) #thon
#removes the first 2 words and prints just the rest
print(word[:3]) #pyt
#removes the last 3 words
print(word[::2]) #pto
#:: the double column picks the first letter and skips the next one.
print(word[::-1])
#re-arranges the word python.

#string concatenation and repetition
#concatenation
a = "hello"
b = "world"
print( a+" "+b) #hello world
#repetition
word = "hi!"
print(word * 3) #hi!#hi!#hi!
#string searching and checking
#membership
text = "python programming"
print('python' in text ) #true
print("java" not in text) #true
text = "hello world"
print(text.find("o"))
print(text.rfind("o"))
print(text.index("world"))
filename = "data.csv"
print(filename.startswith("data")) #true
print(filename.endswith(".csv")) #true 

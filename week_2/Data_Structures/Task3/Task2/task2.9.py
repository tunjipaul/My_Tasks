#enter a sentence and print the vowels in it.
name = input("Your full government name: ")
vowels = ""
for every_character in name:
    if every_character in "aAeEiIoOuU":
         vowels+= every_character
print(vowels)
print(len(vowels))
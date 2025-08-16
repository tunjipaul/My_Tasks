# #task 1 , favorite life quote.
quote = input("what is your favorite quote: ")
quote_titled = quote.title()
print('\'' + quote_titled + '\'')

# #task 2: shopping list manager
empty_list = []
# print(empty_list) #output : []

# #ask the user to enter 3 shopping items (1,by 1)
item_1 = input(" what do you want to buy:  ")
item_2 = input("what do you want to buy: ")
item_3 = input("what do you want to buy: ")
empty_list.append(item_1)
empty_list.append(item_2)
empty_list.append(item_3)
print(empty_list)

# #task 3, word counter.
sentence = input("favorite scipture?: ")
sentence_split = sentence.split()
word_length = len(sentence_split)
print(word_length)

#task 4, name organizer.
name_1 = input("The names:  ").lower().split()
name_1.sort()
print(name_1)
for name in name_1:
    print(name)

#task 5, student score tracker
#ask the user for 3 student names.
names = []
scores = []
for i in range(3):
    names.append(input("their names: "))
    scores.append(input("their scores are: "))

print(f"Name - Score")
for i in range(3):
    print(names[i], "-", scores[i])


#task 6, word analyzer.

user_input = input("input a word: ")
length_of_words = len(user_input)
check_upper = user_input.isupper()
check_lower = user_input.islower()
check_title = user_input.istitle()

reverse_word = user_input[::-1]


print(check_upper, check_lower, check_title, reverse_word)

#task 7, list manipulation

cities = ["ikeja", "new jersey", "new york", "california", "abeokuta"]
new_city = input(" i want to change the 3rd city: ")
cities[2] = new_city
cities.pop()
new_first_city = input("your new first city is: ")
cities.insert(0, new_first_city)
print(cities)